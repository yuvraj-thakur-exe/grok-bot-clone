#!/usr/bin/env python3
"""Create a clean feature worktree from the actual ORBIT application repository.

Does not edit the source checkout, commit, push, merge, or execute project commands.
"""
from __future__ import annotations
import argparse, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def git(repo:Path,*args:str,check=True)->str:
    p=subprocess.run(['git','-C',str(repo),*args],capture_output=True,text=True)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip() or p.stdout.strip() or 'git command failed')
    return p.stdout.strip()

def slug(raw:str)->str:
    s=re.sub(r'[^A-Za-z0-9-]+','-',raw.strip().lower()).strip('-')
    if not s or len(s)>48: raise ValueError('task slug must become 1-48 alphanumeric/hyphen characters')
    return s

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',required=True,type=Path,help='Path to the existing actual ORBIT application Git checkout')
    ap.add_argument('--task',required=True,help='Task slug, e.g. integrate-browser-adapter')
    ap.add_argument('--created-by',required=True,help='Human maintainer; virtual agent roles are refused')
    ap.add_argument('--workspace-root',type=Path,default=None)
    ap.add_argument('--metadata-dir',type=Path,default=None)
    ap.add_argument('--base-ref',default=None,help='Optional existing local branch/ref; default is current HEAD')
    ns=ap.parse_args()
    if ns.created_by.strip().lower() in {'cto','ceo','agent','ai','assistant','orbit-agent','security lead','qa agent'}:
        ap.error('--created-by must identify a human owner/reviewer')
    try: task=slug(ns.task)
    except ValueError as e: ap.error(str(e))
    repo=ns.repo.resolve()
    try:
        top=Path(git(repo,'rev-parse','--show-toplevel')).resolve()
        current=git(repo,'branch','--show-current')
        dirty=git(repo,'status','--porcelain')
        base=ns.base_ref or git(repo,'rev-parse','HEAD')
        git(repo,'rev-parse','--verify',f'{base}^{{commit}}')
    except Exception as e:
        print(f'ERROR: --repo must be an existing Git checkout: {e}',file=sys.stderr); return 2
    if top!=repo:
        print('ERROR: --repo must be the Git repository root, not a subdirectory',file=sys.stderr); return 2
    if not current:
        print('ERROR: source repository is detached; check out the intended base branch first',file=sys.stderr); return 3
    if dirty:
        print('ERROR: actual ORBIT source checkout is dirty; preserve/review changes before creating worktree',file=sys.stderr); return 4
    if ns.base_ref:
        try: git(repo,'merge-base','--is-ancestor',ns.base_ref,'HEAD')
        except Exception:
            print('ERROR: explicit base-ref must be reachable from current HEAD in this workflow',file=sys.stderr); return 3
    home=Path(os.environ.get('ORBIT_HOME','')).expanduser() if os.environ.get('ORBIT_HOME') else None
    workspace=(ns.workspace_root or ((home/'02-workspaces'/'orbit-app-worktrees') if home else (ROOT/'workspaces'/'orbit-app-worktrees'))).resolve()
    metadata=(ns.metadata_dir or ((home/'00-control'/'worktrees'/'orbit-app') if home else (ROOT/'worktree-metadata'/'orbit-app'))).resolve()
    dest=(workspace/task).resolve()
    try: dest.relative_to(workspace)
    except ValueError: print('ERROR: destination escapes workspace root',file=sys.stderr); return 5
    if dest.exists(): print(f'ERROR: destination already exists: {dest}',file=sys.stderr); return 5
    branch=f'orbit/app/{task}'
    if git(repo,'branch','--list',branch,check=False): print(f'ERROR: branch already exists: {branch}',file=sys.stderr); return 5
    workspace.mkdir(parents=True,exist_ok=True); metadata.mkdir(parents=True,exist_ok=True)
    try: git(repo,'worktree','add','-b',branch,str(dest),base)
    except Exception as e: print(f'ERROR: could not create application worktree: {e}',file=sys.stderr); return 6
    remote=git(repo,'remote','get-url','origin',check=False) or None
    record={'schema_version':1,'kind':'orbit_application_feature_worktree','repo_root':str(repo),'origin':remote,'base_ref':base,'source_branch':current,'feature_branch':branch,'task':task,'worktree_path':str(dest),'created_by_human':ns.created_by,'created_at_utc':datetime.now(timezone.utc).isoformat(),'state':'clean_feature_worktree','restrictions':['no auto git add/commit/push/merge','no secret copying','review all imported upstream licenses and provenance']}
    out=metadata/f'{task}.json'; out.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'created','worktree':str(dest),'branch':branch,'base_ref':base,'metadata':str(out),'next':'Use this feature worktree as --target-root for apply_staged_source.py.'},indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
