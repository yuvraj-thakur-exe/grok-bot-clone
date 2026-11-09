#!/usr/bin/env python3
"""ORBIT pinned upstream registry helper: list, show and verify local checkouts."""
from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]
LOCK=ROOT/'config/upstreams/upstream-lock.yaml'
def all_repos():
 d=yaml.safe_load(LOCK.read_text(encoding='utf-8'))
 return d.get('repositories',[])+d.get('candidate_repositories',[])
def default_upstream_dir():
 if os.environ.get('ORBIT_UPSTREAM_DIR'): return Path(os.environ['ORBIT_UPSTREAM_DIR']).expanduser().resolve()
 if os.environ.get('ORBIT_HOME'): return (Path(os.environ['ORBIT_HOME']).expanduser()/'01-upstream-checkouts').resolve()
 return (ROOT/'upstream').resolve()
def git(path,*args):
 r=subprocess.run(['git','-C',str(path),*args],capture_output=True,text=True)
 return r.stdout.strip() if r.returncode==0 else None
def main():
 ap=argparse.ArgumentParser(description=__doc__); sub=ap.add_subparsers(dest='cmd',required=True)
 l=sub.add_parser('list'); l.add_argument('--recommended-only',action='store_true')
 sh=sub.add_parser('show'); sh.add_argument('repo_id')
 v=sub.add_parser('verify'); v.add_argument('--upstream-dir',type=Path,default=None)
 a=sub.add_parser('audit'); a.add_argument('repository',type=Path)
 ns=ap.parse_args(); repos=all_repos()
 if ns.cmd=='list':
  for x in repos:
   if ns.recommended_only and not any(k in str(x.get('adoption','')) for k in ['recommended','preferred','P1']): continue
   print(f"{x['id']:32} {x['observed_license']:20} {x['commit']}  {x['adoption']}")
  print(f"\n{len(repos)} pinned repositories. Clone only what the current feature needs."); return 0
 if ns.cmd=='show':
  x=next((x for x in repos if x['id']==ns.repo_id),None)
  if not x: print('Unknown repo id. Use list.',file=sys.stderr); return 2
  print(yaml.safe_dump(x,sort_keys=False)); return 0
 if ns.cmd=='verify':
  base=(ns.upstream_dir or default_upstream_dir()).resolve(); failures=[]
  for x in repos:
   p=base/x['id']
   if not p.is_dir(): print(f"NOT_CLONED {x['id']}"); continue
   head=git(p,'rev-parse','HEAD'); origin=git(p,'remote','get-url','origin')
   ok=(head==x['commit'] and origin==x['url'])
   print(f"{'PASS' if ok else 'MISMATCH'} {x['id']} expected={x['commit']} actual={head} origin_ok={origin==x['url']}")
   if not ok: failures.append(x['id'])
  print(f"Verified checkout base: {base}")
  return 1 if failures else 0
 if ns.cmd=='audit':
  script=ROOT/'scripts/repo_audit.py'
  return subprocess.run([sys.executable,str(script),str(ns.repository)]).returncode
 return 2
if __name__=='__main__': raise SystemExit(main())
