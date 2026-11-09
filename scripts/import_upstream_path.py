#!/usr/bin/env python3
"""Stage a file/directory from an exact pinned upstream source into ORBIT source-intake."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path
from datetime import datetime, timezone
import yaml

ROOT=Path(__file__).resolve().parents[1]
DEFAULT_LOCK=ROOT/'config/upstreams/upstream-lock.yaml'
SKIP_DIRS={'.git','node_modules','.venv','venv','dist','build','coverage','__pycache__','enterprise'}
SECRET_NAMES={'.env','.env.local','.env.production','id_rsa','id_ed25519','credentials.json','secrets.json'}

def digest(p: Path):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def git(checkout: Path, *args):
    return subprocess.run(['git','-C',str(checkout),*args],capture_output=True,text=True,check=True).stdout.strip()

def normalized_remote(url: str) -> str:
    value=url.strip().lower()
    if value.startswith('git@github.com:'):
        value='https://github.com/'+value.split(':',1)[1]
    return value.removesuffix('.git').rstrip('/')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo-id',required=True)
    ap.add_argument('--checkout',required=True,type=Path)
    ap.add_argument('--path',required=True,help='Exact relative path inside the pinned upstream checkout')
    ap.add_argument('--approved-by',required=True,help='Human reviewer; virtual role names are refused')
    ap.add_argument('--license-evidence',required=True,help='URL or local path to license/NOTICE evidence reviewed')
    ap.add_argument('--lock-file',type=Path,default=DEFAULT_LOCK,help='Test-only override; production must use the package lock')
    ap.add_argument('--output-root',type=Path,default=None)
    ap.add_argument('--license-reviewed',action='store_true')
    ap.add_argument('--security-reviewed',action='store_true')
    ap.add_argument('--tests-reviewed',action='store_true')
    ns=ap.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{1,79}',ns.repo_id):
        ap.error('--repo-id must be a simple registry identifier; no path separators are allowed.')
    if ns.approved_by.strip().lower() in {'cto','ceo','agent','ai','assistant','orbit-agent'}:
        ap.error('--approved-by must identify a human reviewer, not a virtual agent role.')
    if not (ns.license_reviewed and ns.security_reviewed and ns.tests_reviewed):
        ap.error('All three review acknowledgements are required before staging.')
    if not ns.license_evidence.strip(): ap.error('--license-evidence cannot be empty.')
    try:
        lock=yaml.safe_load(ns.lock_file.read_text(encoding='utf-8'))
    except Exception as exc:
        print(f'ERROR: unable to read upstream lock: {exc}',file=sys.stderr); return 2
    entries=lock.get('repositories',[])+lock.get('candidate_repositories',[])
    record=next((x for x in entries if x.get('id')==ns.repo_id),None)
    if not record:
        print(f'ERROR: {ns.repo_id} is not present in the pinned upstream lock',file=sys.stderr); return 2
    checkout=ns.checkout.resolve(); raw_path=Path(ns.path)
    if raw_path.is_absolute() or '..' in raw_path.parts or not raw_path.parts:
        print('ERROR: --path must be a normalized relative path without ..',file=sys.stderr); return 2
    candidate=checkout/raw_path
    cursor=checkout
    for part in raw_path.parts:
        cursor=cursor/part
        if cursor.is_symlink():
            print('ERROR: source path traverses a symlink',file=sys.stderr); return 3
    source=candidate.resolve()
    try: source.relative_to(checkout)
    except ValueError: print('ERROR: source path escapes repository checkout',file=sys.stderr); return 2
    if not source.exists() or source.is_symlink(): print('ERROR: source path missing or symlink',file=sys.stderr); return 2
    parts=raw_path.parts
    if any(x.lower() in SKIP_DIRS for x in parts): print('ERROR: restricted/generated/dependency path cannot be imported',file=sys.stderr); return 3
    if source.is_file() and (source.name.lower() in SECRET_NAMES or source.suffix.lower() in {'.pem','.p12','.pfx','.key'}):
        print('ERROR: secret-like file cannot be imported',file=sys.stderr); return 3
    try:
        commit=git(checkout,'rev-parse','HEAD')
        origin=git(checkout,'remote','get-url','origin')
    except Exception as exc:
        print(f'ERROR: checkout must be a Git repository with origin and a resolvable commit: {exc}',file=sys.stderr); return 4
    if commit != record.get('commit'):
        print(f"ERROR: checkout commit {commit} does not match pinned commit {record.get('commit')}",file=sys.stderr); return 4
    if normalized_remote(origin) != normalized_remote(record.get('url','')):
        print(f"ERROR: checkout origin {origin} does not match locked origin {record.get('url')}",file=sys.stderr); return 4
    excluded=set(record.get('exclude_paths',[]))
    normalized_path=raw_path.as_posix().lstrip('./')
    if any(normalized_path==x.rstrip('/') or normalized_path.startswith(x.rstrip('/')+'/') for x in excluded):
        print(f'ERROR: source path is in an upstream excluded path: {normalized_path}',file=sys.stderr); return 3
    destroot=(ns.output_root or (Path(os.environ['ORBIT_HOME'])/'10-source-intake' if os.environ.get('ORBIT_HOME') else ROOT/'source-intake')).resolve()
    dest=destroot/ns.repo_id/raw_path
    try: dest.resolve().relative_to(destroot)
    except ValueError: print('ERROR: destination escapes source-intake root',file=sys.stderr); return 5
    dest.parent.mkdir(parents=True,exist_ok=True)
    if dest.exists(): print(f'ERROR: destination exists: {dest}',file=sys.stderr); return 5
    copied=[]
    if source.is_file():
        shutil.copy2(source,dest); copied.append({'path':normalized_path,'sha256':digest(source),'size_bytes':source.stat().st_size})
    else:
        dest.mkdir(parents=True,exist_ok=True)
        for item in source.rglob('*'):
            rel=item.relative_to(source)
            if any(x.lower() in SKIP_DIRS for x in rel.parts) or item.is_symlink(): continue
            target=dest/rel
            if item.is_dir(): target.mkdir(parents=True,exist_ok=True)
            elif item.is_file():
                if item.name.lower() in SECRET_NAMES or item.suffix.lower() in {'.pem','.p12','.pfx','.key'}: continue
                target.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(item,target)
                copied.append({'path':(raw_path/rel).as_posix(),'sha256':digest(item),'size_bytes':item.stat().st_size})
    manifest={
      'schema_version':1,'status':'staged_not_merged','repo_id':ns.repo_id,'origin':origin,'commit':commit,
      'locked_url':record.get('url'),'locked_commit':record.get('commit'),'observed_license':record.get('observed_license'),
      'source_path':normalized_path,'destination':str(dest),'approved_by_human':ns.approved_by,
      'license_evidence':ns.license_evidence,'review_acknowledgements':{'license':True,'security':True,'tests':True},
      'created_at_utc':datetime.now(timezone.utc).isoformat(),'files':copied,
      'disclaimer':'Human acknowledgements are not legal certification. Source is staged, not merged; dependency closure, notices, tests and ORBIT review remain required.'
    }
    mp=destroot/ns.repo_id/'IMPORT_MANIFEST.json'; mp.parent.mkdir(parents=True,exist_ok=True)
    existing=[]
    if mp.exists():
        try: existing=json.loads(mp.read_text(encoding='utf-8')).get('imports',[])
        except Exception: existing=[]
    existing.append(manifest); mp.write_text(json.dumps({'schema_version':1,'imports':existing},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'staged_not_merged','destination':str(dest),'manifest':str(mp),'manifest_sha256':digest(mp),'file_count':len(copied),'commit':commit,'license':record.get('observed_license')},indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
