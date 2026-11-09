#!/usr/bin/env python3
"""Create a clean task worktree from an exact pinned upstream checkout; never edits the pinned checkout."""
from __future__ import annotations
import argparse, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
LOCK=ROOT/'config/upstreams/upstream-lock.yaml'
def run_git(repo: Path, *args: str, check: bool=True) -> str:
    p=subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True)
    if check and p.returncode: raise RuntimeError(p.stderr.strip() or p.stdout.strip() or 'git command failed')
    return p.stdout.strip()
def slug(value: str) -> str:
    value=re.sub(r'[^a-zA-Z0-9-]+','-',value.strip().lower()).strip('-')
    if not value or len(value)>48: raise ValueError('task slug must become 1-48 simple characters')
    return value
def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo-id',required=True)
    ap.add_argument('--task',required=True,help='Short task slug, e.g. approval-card-contract')
    ap.add_argument('--created-by',required=True,help='Human owner/reviewer, not a virtual role name')
    ap.add_argument('--upstream-dir',type=Path,default=None)
    ap.add_argument('--workspace-root',type=Path,default=None)
    ap.add_argument('--metadata-dir',type=Path,default=None)
    ap.add_argument('--lock-file',type=Path,default=LOCK,help='Test-only lock override; production uses package lock')
    ns=ap.parse_args()
    if ns.created_by.strip().lower() in {'cto','ceo','agent','ai','assistant','orbit-agent'}:
        ap.error('--created-by must identify a human owner')
    lock=yaml.safe_load(ns.lock_file.read_text(encoding='utf-8'))
    records=lock.get('repositories',[])+lock.get('candidate_repositories',[])
    record=next((x for x in records if x.get('id')==ns.repo_id),None)
    if not record: print('ERROR: repository id not found in upstream lock',file=sys.stderr); return 2
    if record.get('exclude_paths') and 'enterprise/' in record.get('exclude_paths',[]):
        # worktrees are okay only from sparse checkouts which do not contain excluded content
        pass
    home=Path(os.environ.get('ORBIT_HOME','')).expanduser() if os.environ.get('ORBIT_HOME') else None
    upstream=(ns.upstream_dir or (Path(os.environ.get('ORBIT_UPSTREAM_DIR')).expanduser() if os.environ.get('ORBIT_UPSTREAM_DIR') else (home/'01-upstream-checkouts' if home else ROOT/'upstream'))).resolve()
    workspace=(ns.workspace_root or ((home/'02-workspaces'/'upstream-worktrees') if home else (ROOT/'workspaces'/'upstream-worktrees'))).resolve()
    metadata=(ns.metadata_dir or ((home/'00-control'/'worktrees') if home else (ROOT/'worktree-metadata'))).resolve()
    checkout=upstream/ns.repo_id
    if not checkout.is_dir(): print(f'ERROR: source checkout is missing: {checkout}',file=sys.stderr); return 2
    try:
        actual=run_git(checkout,'rev-parse','HEAD')
        origin=run_git(checkout,'remote','get-url','origin')
        status=run_git(checkout,'status','--porcelain')
    except Exception as exc: print(f'ERROR: invalid checkout: {exc}',file=sys.stderr); return 3
    def normalize(url: str) -> str:
        v=url.strip().lower()
        if v.startswith('git@github.com:'): v='https://github.com/'+v.split(':',1)[1]
        return v.removesuffix('.git').rstrip('/')
    if actual != record['commit'] or normalize(origin) != normalize(record['url']):
        print('ERROR: checkout does not match the exact locked origin/commit; re-clone pinned source',file=sys.stderr); return 4
    if status:
        print('ERROR: pinned checkout has working-tree changes; do not create a task worktree from dirty source',file=sys.stderr); return 5
    for excluded in record.get('exclude_paths',[]):
        if (checkout/excluded.rstrip('/')).exists():
            print(f'ERROR: excluded source path is present in checkout: {excluded}; reacquire with required sparse checkout',file=sys.stderr); return 5
    task=slug(ns.task); branch=f"orbit/{ns.repo_id}/{task}"
    dest=(workspace/ns.repo_id/task).resolve()
    try: dest.relative_to(workspace)
    except ValueError: print('ERROR: calculated worktree path escapes workspace root',file=sys.stderr); return 6
    if dest.exists(): print(f'ERROR: destination already exists: {dest}',file=sys.stderr); return 6
    existing=run_git(checkout,'branch','--list',branch,check=False)
    if existing: print(f'ERROR: branch already exists: {branch}',file=sys.stderr); return 6
    dest.parent.mkdir(parents=True,exist_ok=True); metadata.mkdir(parents=True,exist_ok=True)
    try: run_git(checkout,'worktree','add','-b',branch,str(dest),record['commit'])
    except Exception as exc: print(f'ERROR: git worktree creation failed: {exc}',file=sys.stderr); return 7
    record_json={'schema_version':1,'repo_id':ns.repo_id,'origin':record['url'],'pinned_commit':record['commit'],'worktree_commit':actual,'branch':branch,'task':task,'worktree_path':str(dest),'created_by_human':ns.created_by,'created_at_utc':datetime.now(timezone.utc).isoformat(),'state':'isolated_unmerged_worktree','restrictions':record.get('exclude_paths',[])}
    out=metadata/f'{ns.repo_id}-{task}.json'
    out.write_text(json.dumps(record_json,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'created','worktree':str(dest),'branch':branch,'base_commit':actual,'metadata':str(out),'warning':'Changes remain in this isolated upstream worktree. Review licensing and tests; never merge into ORBIT application automatically.'},indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
