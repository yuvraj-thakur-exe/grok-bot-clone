#!/usr/bin/env python3
"""Apply a previously reviewed upstream source-intake entry into a clean ORBIT feature worktree.

This copies verified files only. It refuses overwrites, dirty/detached targets and non-feature branches.
It never git-adds, commits, pushes or merges the result.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import yaml
ROOT=Path(__file__).resolve().parents[1]
VIRTUAL={'cto','ceo','agent','ai','assistant','orbit-agent','security lead','qa agent'}
def sha(p:Path)->str:
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
 return h.hexdigest()
def git(root:Path,*args:str,check=True):
 p=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True)
 if check and p.returncode: raise RuntimeError(p.stderr.strip() or p.stdout.strip() or 'git failed')
 return p.stdout.strip()
def safe_rel(value:str)->PurePosixPath:
 p=PurePosixPath(value.replace('\\','/'))
 if p.is_absolute() or not p.parts or any(x in {'..','.'} for x in p.parts): raise ValueError(f'unsafe relative path: {value}')
 return p
def main()->int:
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repo-id',required=True); ap.add_argument('--source-path',required=True,help='Exact source path recorded in IMPORT_MANIFEST.json')
 ap.add_argument('--target-root',required=True,type=Path,help='Existing clean ORBIT Git feature worktree')
 ap.add_argument('--target-path',required=True,help='New path relative to target-root; must not exist')
 ap.add_argument('--applied-by',required=True,help='Human reviewer/implementer, not an AI role')
 ap.add_argument('--change-id',required=True,help='Short audit identifier, e.g. browser-adapter-v1')
 ap.add_argument('--intake-root',type=Path,default=None); ap.add_argument('--import-index',type=int,default=-1)
 ap.add_argument('--expected-manifest-sha256',required=True,help='SHA-256 printed by import_upstream_path.py; protects the reviewed staging manifest')
 ap.add_argument('--lock-file',type=Path,default=ROOT/'config/upstreams/upstream-lock.yaml',help='Test-only override; production uses the package lock')
 ap.add_argument('--license-reviewed',action='store_true'); ap.add_argument('--security-reviewed',action='store_true'); ap.add_argument('--tests-reviewed',action='store_true')
 ns=ap.parse_args()
 if ns.applied_by.strip().lower() in VIRTUAL: ap.error('--applied-by must identify a human reviewer, not a virtual agent')
 if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{1,79}',ns.repo_id): ap.error('invalid --repo-id')
 if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{1,79}',ns.change_id): ap.error('invalid --change-id')
 if not(ns.license_reviewed and ns.security_reviewed and ns.tests_reviewed): ap.error('all review acknowledgements are required')
 try: source_rel=safe_rel(ns.source_path); target_rel=safe_rel(ns.target_path)
 except ValueError as e: print(f'ERROR: {e}',file=sys.stderr); return 2
 home=Path(os.environ['ORBIT_HOME']).expanduser() if os.environ.get('ORBIT_HOME') else ROOT
 intake=(ns.intake_root or home/'10-source-intake').resolve()
 manifest_path=intake/ns.repo_id/'IMPORT_MANIFEST.json'
 if not manifest_path.is_file(): print(f'ERROR: import manifest not found: {manifest_path}',file=sys.stderr); return 2
 if not re.fullmatch(r'[0-9a-f]{64}',ns.expected_manifest_sha256): print('ERROR: expected manifest SHA-256 must be 64 lowercase hex characters',file=sys.stderr); return 2
 if sha(manifest_path)!=ns.expected_manifest_sha256: print('ERROR: import manifest SHA-256 does not match the reviewed value',file=sys.stderr); return 4
 try: manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
 except Exception as e: print(f'ERROR: cannot parse import manifest: {e}',file=sys.stderr); return 2
 imports=manifest.get('imports',[])
 try: item=imports[ns.import_index]
 except (IndexError,TypeError): print('ERROR: requested import entry does not exist',file=sys.stderr); return 2
 if item.get('repo_id')!=ns.repo_id or item.get('status')!='staged_not_merged': print('ERROR: manifest entry is not a staged source entry for this repo',file=sys.stderr); return 3
 try:
  lock=yaml.safe_load(ns.lock_file.read_text(encoding='utf-8'))
  locked=next((x for x in lock.get('repositories',[])+lock.get('candidate_repositories',[]) if x.get('id')==ns.repo_id),None)
 except Exception as e: print(f'ERROR: unable to read source lock: {e}',file=sys.stderr); return 3
 if not locked or item.get('locked_url')!=locked.get('url') or item.get('locked_commit')!=locked.get('commit') or item.get('observed_license')!=locked.get('observed_license'):
  print('ERROR: staging manifest does not match the current pinned source lock',file=sys.stderr); return 3
 if item.get('source_path')!=source_rel.as_posix(): print('ERROR: source path does not exactly match manifest entry',file=sys.stderr); return 3
 if not item.get('license_evidence') or not item.get('approved_by_human') or item.get('approved_by_human','').strip().lower() in VIRTUAL or not all(item.get('review_acknowledgements',{}).get(k) is True for k in ('license','security','tests')): print('ERROR: staged entry lacks review evidence',file=sys.stderr); return 3
 if not re.fullmatch(r'[0-9a-f]{40}',str(item.get('commit',''))) or item.get('commit')!=item.get('locked_commit'): print('ERROR: manifest commit does not match its locked commit',file=sys.stderr); return 3
 def normalize_remote(value:str)->str:
  v=value.strip().lower()
  if v.startswith('git@github.com:'): v='https://github.com/'+v.split(':',1)[1]
  return v.removesuffix('.git').rstrip('/')
 if not item.get('origin') or normalize_remote(item.get('origin',''))!=normalize_remote(item.get('locked_url','')): print('ERROR: manifest origin does not match locked origin',file=sys.stderr); return 3
 if not item.get('files'): print('ERROR: staged entry has no file hashes',file=sys.stderr); return 3
 selected=[]
 prefix=source_rel.as_posix().rstrip('/')+'/'
 for f in item['files']:
  rel=safe_rel(f.get('path',''))
  rels=rel.as_posix()
  if source_rel.as_posix()!=rels and not rels.startswith(prefix): print(f'ERROR: manifest file is outside selected source path: {rels}',file=sys.stderr); return 3
  src=intake/ns.repo_id/Path(*rel.parts)
  cur=intake/ns.repo_id
  for part in rel.parts:
   cur=cur/part
   if cur.is_symlink(): print(f'ERROR: staged source contains symlink: {rels}',file=sys.stderr); return 3
  if not src.is_file() or src.is_symlink(): print(f'ERROR: staged source file missing or unsafe: {rels}',file=sys.stderr); return 3
  if src.stat().st_size!=f.get('size_bytes') or sha(src)!=f.get('sha256'): print(f'ERROR: staged source hash/size mismatch: {rels}',file=sys.stderr); return 4
  target_rel_file=target_rel if source_rel.as_posix()==rels else PurePosixPath(target_rel.as_posix()+'/'+rels[len(prefix):])
  selected.append((src,target_rel_file.as_posix(),sha(src),src.stat().st_size))
 target=ns.target_root.resolve()
 try:
  gitroot=Path(git(target,'rev-parse','--show-toplevel')).resolve()
  branch=git(target,'branch','--show-current')
  dirty=git(target,'status','--porcelain')
 except Exception as e: print(f'ERROR: target must be a Git worktree: {e}',file=sys.stderr); return 5
 if gitroot!=target: print('ERROR: --target-root must be the Git worktree root',file=sys.stderr); return 5
 if not branch or branch in {'main','master','develop'} or not (branch.startswith('orbit/') or branch.startswith('feature/')): print(f'ERROR: target branch must be an orbit/* or feature/* work branch, found: {branch or "detached"}',file=sys.stderr); return 5
 if dirty: print('ERROR: target worktree must be clean before applying upstream files',file=sys.stderr); return 5
 for _,dstrel,_,_ in selected:
  p=target/Path(*PurePosixPath(dstrel).parts)
  try:p.resolve().relative_to(target)
  except ValueError: print('ERROR: target path escapes worktree',file=sys.stderr); return 6
  cur=target
  for part in PurePosixPath(dstrel).parts:
   cur=cur/part
   if cur.is_symlink(): print(f'ERROR: target path traverses symlink: {dstrel}',file=sys.stderr); return 6
  if p.exists(): print(f'ERROR: refusing to overwrite existing target: {p}',file=sys.stderr); return 6
 provenance_rel=PurePosixPath('docs/source-provenance')/f'{ns.repo_id}-{ns.change_id}.json'
 provenance=target/Path(*provenance_rel.parts)
 if provenance.exists(): print(f'ERROR: provenance record already exists: {provenance}',file=sys.stderr); return 6
 copied=[]; created_dirs=[]
 try:
  for src,dstrel,digest,size in selected:
   dest=target/Path(*PurePosixPath(dstrel).parts)
   missing=[]; cur=dest.parent
   while cur!=target and not cur.exists(): missing.append(cur); cur=cur.parent
   dest.parent.mkdir(parents=True,exist_ok=True); created_dirs.extend(missing)
   shutil.copy2(src,dest); copied.append(dest)
  provenance.parent.mkdir(parents=True,exist_ok=True)
  record={'schema_version':1,'status':'copied_into_orbit_worktree_uncommitted','repo_id':ns.repo_id,'upstream_url':item.get('locked_url'),'upstream_commit':item.get('commit'),'observed_license':item.get('observed_license'),'license_evidence':item.get('license_evidence'),'source_path':source_rel.as_posix(),'target_root':str(target),'target_branch':branch,'target_path':target_rel.as_posix(),'applied_by_human':ns.applied_by,'change_id':ns.change_id,'applied_at_utc':datetime.now(timezone.utc).isoformat(),'review_flags':{'license':True,'security':True,'tests':True},'files':[{'target_path':dst,'sha256':digest,'size_bytes':size} for _,dst,digest,size in selected],'notice':'Files are copied but not git-added, committed, merged or released. Preserve required copyright, license, NOTICE and modification statements.'}
  provenance.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
 except Exception as e:
  for p in copied:
   try:p.unlink()
   except OSError:pass
  for d in sorted(set(created_dirs),key=lambda x:len(x.parts),reverse=True):
   try:d.rmdir()
   except OSError:pass
  try:
   if provenance.exists(): provenance.unlink()
  except Exception:pass
  print(f'ERROR: copy failed and created files were rolled back: {e}',file=sys.stderr); return 7
 print(json.dumps({'status':'copied_uncommitted','files':len(copied),'target_root':str(target),'branch':branch,'provenance':str(provenance),'next':'Review the copied diff, restore notices/dependency closure, run tests, then create a normal human-reviewed commit.'},indent=2))
 return 0
if __name__=='__main__': raise SystemExit(main())
