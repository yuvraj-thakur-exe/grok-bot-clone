"""Isolated smoke tests for ORBIT repository/storage utilities; no upstream source is executed."""
from __future__ import annotations
import hashlib, json, os, re, subprocess, sys, tempfile, unittest, yaml
from pathlib import Path
PACK = Path(__file__).resolve().parents[2]
SCRIPTS = PACK / "scripts"

def run(*args, env=None):
    return subprocess.run([sys.executable, *map(str,args)], cwd=PACK, env=env, capture_output=True, text=True)

class RepositoryOperationsTests(unittest.TestCase):
    def make_git_repo(self, root: Path) -> Path:
        root.mkdir(parents=True)
        subprocess.run(["git","init",str(root)],check=True,capture_output=True)
        subprocess.run(["git","-C",str(root),"config","user.email","test@example.invalid"],check=True)
        subprocess.run(["git","-C",str(root),"config","user.name","ORBIT test"],check=True)
        (root/"src").mkdir(); (root/"src"/"module.py").write_text("def answer(): return 42\n")
        (root/"enterprise").mkdir(); (root/"enterprise"/"restricted.py").write_text("must not stage\n")
        (root/".env").write_text("NOT_A_REAL_SECRET=placeholder-only\n")
        subprocess.run(["git","-C",str(root),"add","."],check=True)
        subprocess.run(["git","-C",str(root),"commit","-m","test fixture"],check=True,capture_output=True)
        subprocess.run(["git","-C",str(root),"remote","add","origin","https://github.com/example/fixture.git"],check=True)
        return root

    def make_lock(self, root: Path, repo: Path, repo_id="fixture-repo", commit=None):
        sha = commit or subprocess.run(["git","-C",str(repo),"rev-parse","HEAD"],capture_output=True,text=True,check=True).stdout.strip()
        lock=root/"lock.yaml"
        lock.write_text(yaml.safe_dump({'repositories':[{'id':repo_id,'url':'https://github.com/example/fixture.git','commit':sha,'observed_license':'MIT','exclude_paths':[]}] }))
        return lock, sha

    def test_storage_init_and_status(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/"orbit-drive"
            a=run(SCRIPTS/"orbit_storage.py","init",target,"--skip-capacity-check")
            self.assertEqual(a.returncode,0,a.stderr)
            m=json.loads((target/".orbit-storage.json").read_text())
            self.assertEqual(m["target_allocated_gb"],440)
            self.assertEqual(m["free_reserve_target_gb"],60)
            self.assertEqual(sum(x["target_gb"] for x in m["folders"]),440)
            b=run(SCRIPTS/"orbit_storage.py","status",target)
            self.assertEqual(b.returncode,0,b.stderr)

    def test_repo_ops_list_and_show(self):
        a=run(SCRIPTS/"orbit_repo_ops.py","list")
        self.assertEqual(a.returncode,0,a.stderr)
        self.assertIn("50 pinned repositories",a.stdout)
        b=run(SCRIPTS/"orbit_repo_ops.py","show","openmausbot")
        self.assertEqual(b.returncode,0,b.stderr)
        self.assertIn("enterprise/",b.stdout)

    def test_import_stages_one_file_with_sha256_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout"); intake=root/"intake"; lock,_=self.make_lock(root,repo)
            a=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",repo,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://github.com/example/fixture/blob/main/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,0,a.stderr)
            dst=intake/"fixture-repo"/"src"/"module.py"
            self.assertTrue(dst.exists())
            expected=hashlib.sha256(dst.read_bytes()).hexdigest()
            manifest=json.loads((intake/"fixture-repo"/"IMPORT_MANIFEST.json").read_text())
            self.assertEqual(manifest["imports"][0]["files"][0]["sha256"],expected)
            self.assertEqual(manifest["imports"][0]["status"],"staged_not_merged")

    def test_import_refuses_enterprise_and_path_escape(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout"); intake=root/"intake"; lock,_=self.make_lock(root,repo)
            base=[SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",repo,"--approved-by","human-reviewer","--license-evidence","https://github.com/example/fixture/blob/main/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed"]
            a=run(*base,"--path","enterprise/restricted.py")
            self.assertEqual(a.returncode,3)
            b=run(*base,"--path","../outside.py")
            self.assertEqual(b.returncode,2)

    def test_import_refuses_unpinned_commit(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout"); lock,_=self.make_lock(root,repo,commit='0'*40)
            a=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",repo,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",root/"intake","--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,4)
            self.assertIn("does not match pinned commit",a.stderr)

    def test_import_requires_human_reviewer_and_review_flags(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout"); lock,_=self.make_lock(root,repo)
            a=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",repo,"--path","src/module.py","--approved-by","cto","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock)
            self.assertNotEqual(a.returncode,0)
            self.assertIn("human reviewer",a.stderr)

    def test_worktree_created_from_pinned_clean_checkout(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=root/"upstream"; upstream.mkdir(); repo=self.make_git_repo(upstream/"fixture-repo"); lock,_=self.make_lock(root,repo)
            a=run(SCRIPTS/"create_upstream_worktree.py","--repo-id","fixture-repo","--task","approval-ui","--created-by","human-reviewer","--upstream-dir",upstream,"--workspace-root",root/"workspaces","--metadata-dir",root/"metadata","--lock-file",lock)
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertTrue((root/"workspaces"/"fixture-repo"/"approval-ui"/"src"/"module.py").exists())
            meta=json.loads((root/"metadata"/"fixture-repo-approval-ui.json").read_text())
            self.assertEqual(meta["state"],"isolated_unmerged_worktree")
            self.assertEqual(meta["pinned_commit"],meta["worktree_commit"])

    def test_worktree_refuses_dirty_pinned_checkout(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=root/"upstream"; upstream.mkdir(); repo=self.make_git_repo(upstream/"fixture-repo"); lock,_=self.make_lock(root,repo)
            (repo/"src"/"module.py").write_text("dirty\n")
            a=run(SCRIPTS/"create_upstream_worktree.py","--repo-id","fixture-repo","--task","dirty-test","--created-by","human-reviewer","--upstream-dir",upstream,"--workspace-root",root/"workspaces","--metadata-dir",root/"metadata","--lock-file",lock)
            self.assertEqual(a.returncode,5)


    def test_import_refuses_symlink_source(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout")
            (repo/"src"/"linked.py").symlink_to(repo/"src"/"module.py")
            subprocess.run(["git","-C",str(repo),"add","src/linked.py"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(repo),"commit","-m","add symlink"],check=True,capture_output=True)
            lock,_=self.make_lock(root,repo)
            a=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",repo,"--path","src/linked.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",root/"intake","--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,3)
            self.assertIn("symlink",a.stderr)

    def test_worktree_refuses_checkout_containing_excluded_path(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=root/"upstream"; upstream.mkdir(); repo=self.make_git_repo(upstream/"fixture-repo")
            lock,_=self.make_lock(root,repo)
            data=yaml.safe_load(lock.read_text()); data['repositories'][0]['exclude_paths']=['enterprise/']; lock.write_text(yaml.safe_dump(data))
            a=run(SCRIPTS/"create_upstream_worktree.py","--repo-id","fixture-repo","--task","restricted-test","--created-by","human-reviewer","--upstream-dir",upstream,"--workspace-root",root/"workspaces","--metadata-dir",root/"metadata","--lock-file",lock)
            self.assertEqual(a.returncode,5)
            self.assertIn("excluded source path",a.stderr)

    def test_audit_writes_redacted_report_outside_pack(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=self.make_git_repo(root/"checkout"); out=root/"reports"
            a=run(SCRIPTS/"repo_audit.py",repo,"--output-dir",out)
            self.assertEqual(a.returncode,0,a.stderr)
            reports=list(out.glob("*.md")); self.assertEqual(len(reports),1)
            self.assertIn("Secret-pattern flags",reports[0].read_text())

    def test_apply_staged_source_copies_exact_files_with_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=self.make_git_repo(root/"upstream"); intake=root/"intake"; lock,_=self.make_lock(root,upstream)
            staged=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",upstream,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(staged.returncode,0,staged.stderr)
            target=root/"orbit-app"; target.mkdir(); subprocess.run(["git","init",str(target)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(target),"config","user.name","ORBIT test"],check=True)
            (target/"README.md").write_text("baseline\n"); subprocess.run(["git","-C",str(target),"add","."],check=True); subprocess.run(["git","-C",str(target),"commit","-m","base"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"checkout","-b","orbit/fixture-repo/apply-test"],check=True,capture_output=True)
            a=run(SCRIPTS/"apply_staged_source.py","--repo-id","fixture-repo","--source-path","src/module.py","--target-root",target,"--target-path","src/upstream-module.py","--applied-by","human-reviewer","--change-id","module-copy-1","--intake-root",intake,"--lock-file",lock,"--expected-manifest-sha256",hashlib.sha256((intake/"fixture-repo"/"IMPORT_MANIFEST.json").read_bytes()).hexdigest(),"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,0,a.stderr)
            self.assertTrue((target/"src/upstream-module.py").exists())
            p=target/"docs/source-provenance/fixture-repo-module-copy-1.json"
            record=json.loads(p.read_text()); self.assertEqual(record["status"],"copied_into_orbit_worktree_uncommitted")
            self.assertEqual(record["files"][0]["sha256"],hashlib.sha256((target/"src/upstream-module.py").read_bytes()).hexdigest())

    def test_apply_staged_source_refuses_overwrite_and_dirty_target(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=self.make_git_repo(root/"upstream"); intake=root/"intake"; lock,_=self.make_lock(root,upstream)
            staged=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",upstream,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(staged.returncode,0,staged.stderr)
            target=root/"orbit-app"; target.mkdir(); subprocess.run(["git","init",str(target)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(target),"config","user.name","ORBIT test"],check=True)
            (target/"README.md").write_text("base\n"); subprocess.run(["git","-C",str(target),"add","."],check=True); subprocess.run(["git","-C",str(target),"commit","-m","base"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"checkout","-b","feature/test"],check=True,capture_output=True)
            dest=target/"src/upstream-module.py"; dest.parent.mkdir(); dest.write_text("user code\n")
            a=run(SCRIPTS/"apply_staged_source.py","--repo-id","fixture-repo","--source-path","src/module.py","--target-root",target,"--target-path","src/upstream-module.py","--applied-by","human-reviewer","--change-id","module-copy-1","--intake-root",intake,"--lock-file",lock,"--expected-manifest-sha256",hashlib.sha256((intake/"fixture-repo"/"IMPORT_MANIFEST.json").read_bytes()).hexdigest(),"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,5)  # dirty target refused before considering overwrite

    def test_apply_staged_source_refuses_tampered_intake(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=self.make_git_repo(root/"upstream"); intake=root/"intake"; lock,_=self.make_lock(root,upstream)
            staged=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",upstream,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(staged.returncode,0,staged.stderr)
            (intake/"fixture-repo/src/module.py").write_text("tampered\n")
            target=root/"orbit-app"; target.mkdir(); subprocess.run(["git","init",str(target)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(target),"config","user.name","ORBIT test"],check=True)
            (target/"README.md").write_text("base\n"); subprocess.run(["git","-C",str(target),"add","."],check=True); subprocess.run(["git","-C",str(target),"commit","-m","base"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"checkout","-b","orbit/test/copy"],check=True,capture_output=True)
            a=run(SCRIPTS/"apply_staged_source.py","--repo-id","fixture-repo","--source-path","src/module.py","--target-root",target,"--target-path","src/upstream-module.py","--applied-by","human-reviewer","--change-id","module-copy-1","--intake-root",intake,"--lock-file",lock,"--expected-manifest-sha256",hashlib.sha256((intake/"fixture-repo"/"IMPORT_MANIFEST.json").read_bytes()).hexdigest(),"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,4)
            self.assertFalse((target/"src/upstream-module.py").exists())

    def test_create_orbit_app_worktree_from_clean_repository(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=root/"orbit-app"; repo.mkdir(); subprocess.run(["git","init",str(repo)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(repo),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(repo),"config","user.name","ORBIT test"],check=True)
            (repo/"README.md").write_text("base\n"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-m","base"],check=True,capture_output=True)
            a=run(SCRIPTS/"create_orbit_app_worktree.py","--repo",repo,"--task","first-integration","--created-by","human-reviewer","--workspace-root",root/"workspaces","--metadata-dir",root/"metadata")
            self.assertEqual(a.returncode,0,a.stderr)
            worktree=root/"workspaces/first-integration"; self.assertTrue((worktree/"README.md").exists())
            meta=json.loads((root/"metadata/first-integration.json").read_text()); self.assertEqual(meta["feature_branch"],"orbit/app/first-integration")
            self.assertEqual(__import__("subprocess").run(["git","-C",str(repo),"branch","--show-current"],capture_output=True,text=True).stdout.strip(),"master" if __import__("subprocess").run(["git","-C",str(repo),"branch","--show-current"],capture_output=True,text=True).stdout.strip()=="master" else "main")

    def test_create_orbit_app_worktree_refuses_dirty_source(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); repo=root/"orbit-app"; repo.mkdir(); subprocess.run(["git","init",str(repo)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(repo),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(repo),"config","user.name","ORBIT test"],check=True)
            (repo/"README.md").write_text("base\n"); subprocess.run(["git","-C",str(repo),"add","."],check=True); subprocess.run(["git","-C",str(repo),"commit","-m","base"],check=True,capture_output=True)
            (repo/"dirty.txt").write_text("uncommitted\n")
            a=run(SCRIPTS/"create_orbit_app_worktree.py","--repo",repo,"--task","dirty-task","--created-by","human-reviewer","--workspace-root",root/"workspaces","--metadata-dir",root/"metadata")
            self.assertEqual(a.returncode,4)

    def test_apply_staged_source_refuses_existing_target_on_clean_worktree(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=self.make_git_repo(root/"upstream"); intake=root/"intake"; lock,_=self.make_lock(root,upstream)
            staged=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",upstream,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(staged.returncode,0,staged.stderr)
            target=root/"orbit-app"; target.mkdir(); subprocess.run(["git","init",str(target)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(target),"config","user.name","ORBIT test"],check=True)
            (target/"README.md").write_text("base\n"); (target/"src").mkdir(); (target/"src/upstream-module.py").write_text("existing\n")
            subprocess.run(["git","-C",str(target),"add","."],check=True); subprocess.run(["git","-C",str(target),"commit","-m","base"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"checkout","-b","orbit/fixture-repo/no-overwrite"],check=True,capture_output=True)
            a=run(SCRIPTS/"apply_staged_source.py","--repo-id","fixture-repo","--source-path","src/module.py","--target-root",target,"--target-path","src/upstream-module.py","--applied-by","human-reviewer","--change-id","module-copy-1","--intake-root",intake,"--lock-file",lock,"--expected-manifest-sha256",hashlib.sha256((intake/"fixture-repo"/"IMPORT_MANIFEST.json").read_bytes()).hexdigest(),"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,6)
            self.assertEqual((target/"src/upstream-module.py").read_text(),"existing\n")

    def test_apply_staged_source_refuses_changed_manifest_digest(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); upstream=self.make_git_repo(root/"upstream"); intake=root/"intake"; lock,_=self.make_lock(root,upstream)
            staged=run(SCRIPTS/"import_upstream_path.py","--repo-id","fixture-repo","--checkout",upstream,"--path","src/module.py","--approved-by","human-reviewer","--license-evidence","https://example.invalid/LICENSE","--lock-file",lock,"--output-root",intake,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(staged.returncode,0,staged.stderr)
            manifest_path=intake/"fixture-repo"/"IMPORT_MANIFEST.json"; original=hashlib.sha256(manifest_path.read_bytes()).hexdigest()
            content=json.loads(manifest_path.read_text()); content["review_note"]="tampered"; manifest_path.write_text(json.dumps(content))
            target=root/"orbit-app"; target.mkdir(); subprocess.run(["git","init",str(target)],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"config","user.email","test@example.invalid"],check=True); subprocess.run(["git","-C",str(target),"config","user.name","ORBIT test"],check=True)
            (target/"README.md").write_text("base\n"); subprocess.run(["git","-C",str(target),"add","."],check=True); subprocess.run(["git","-C",str(target),"commit","-m","base"],check=True,capture_output=True)
            subprocess.run(["git","-C",str(target),"checkout","-b","orbit/fixture-repo/manifest-check"],check=True,capture_output=True)
            a=run(SCRIPTS/"apply_staged_source.py","--repo-id","fixture-repo","--source-path","src/module.py","--target-root",target,"--target-path","src/upstream-module.py","--applied-by","human-reviewer","--change-id","manifest-check","--intake-root",intake,"--lock-file",lock,"--expected-manifest-sha256",original,"--license-reviewed","--security-reviewed","--tests-reviewed")
            self.assertEqual(a.returncode,4)
            self.assertIn("manifest SHA-256",a.stderr)

    def test_clone_checkout_directory_names_match_locked_ids(self):
        lock=yaml.safe_load((PACK/"config/upstreams/upstream-lock.yaml").read_text())
        expected={item["id"]:item["url"].removesuffix(".git") for item in lock["repositories"]+lock["candidate_repositories"]}
        script=(SCRIPTS/"clone_upstreams.sh").read_text()
        observed={url.removesuffix(".git"):name for name,url in re.findall(r"clone_pinned\s+(\S+)\s+(https://github\.com/[^ ]+\.git)",script)}
        self.assertEqual(set(observed.values()),set(expected.keys()))
        self.assertEqual({v:k for k,v in observed.items()},expected)
        self.assertIn("--all-v10-new",script)

if __name__ == "__main__": unittest.main(verbosity=2)
