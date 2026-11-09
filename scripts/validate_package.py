#!/usr/bin/env python3
"""Validate ORBIT v1.0 documentation, schemas, source provenance and archive manifest."""
from __future__ import annotations
import argparse, hashlib, json, re, subprocess
from pathlib import Path
import yaml
SOURCE_HASHES={
 'docs/source-material/USER_PROVIDED_DOCUMENTATION_BLUEPRINT.md':'bb6f5f33375401c9db6246da235faabd28b4344dccef8266008c951e90f8232b',
 'docs/source-material/USER_PROVIDED_ORBIT_MASTER_BRIEF.md':'a944b184123f67b02484e9f5143dcbc88c0e531578abba8be1e75a23d1448ebf',
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--root',default=str(Path(__file__).resolve().parents[1])); ns=ap.parse_args()
 root=Path(ns.root).resolve(); errors=[]
 files=sorted(p for p in root.rglob('*') if p.is_file() and p.name!='PACKAGE_MANIFEST.json')
 for p in files:
  rel=p.relative_to(root).as_posix()
  if p.stat().st_size==0: errors.append(f'empty file: {rel}')
  try:
   if p.suffix.lower()=='.json': json.loads(p.read_text(encoding='utf-8'))
   elif p.suffix.lower() in {'.yaml','.yml'}: yaml.safe_load(p.read_text(encoding='utf-8'))
  except Exception as e: errors.append(f'parse error: {rel}: {e}')
  if p.suffix.lower()=='.md':
   c=p.read_text(encoding='utf-8')
   if rel not in SOURCE_HASHES and 'Document baseline:' not in c: errors.append(f'missing v1.0 baseline: {rel}')
   if rel not in SOURCE_HASHES and 'ORBIT v1.0.0-draft' not in c and 'ORBIT 1.0.0-draft' not in c: errors.append(f'baseline version mismatch: {rel}')
   if sum(1 for line in c.splitlines() if re.match(r'^\s*(```|~~~)',line))%2: errors.append(f'unbalanced markdown fences: {rel}')
   for m in re.finditer(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',c):
    raw=m.group(1).strip().split()[0].strip('<>')
    if not raw or raw.startswith(('http://','https://','mailto:','tel:','#','data:')): continue
    target=raw.split('#',1)[0].split('?',1)[0]
    if target and not (p.parent/target).resolve().exists(): errors.append(f'broken local markdown link: {rel} -> {raw}')
 for rel,h in SOURCE_HASHES.items():
  p=root/rel
  if not p.exists() or sha(p)!=h: errors.append(f'user source hash mismatch: {rel}')
 env=(root/'.env.example').read_text(encoding='utf-8') if (root/'.env.example').exists() else ''
 if not re.search(r'^ORBIT_ENV=',env,re.M): errors.append('.env.example missing ORBIT_ENV')
 lock=yaml.safe_load((root/'config/upstreams/upstream-lock.yaml').read_text(encoding='utf-8'))
 entries=lock.get('repositories',[])+lock.get('candidate_repositories',[])
 if len(entries)!=50: errors.append(f'expected 50 pinned upstream repositories, found {len(entries)}')
 if len({x.get('id') for x in entries})!=50: errors.append('upstream IDs are not unique')
 if lock.get('repository_count')!=50: errors.append('upstream lock repository_count must be 50')
 json_lock=json.loads((root/'config/upstreams/upstream-lock.json').read_text(encoding='utf-8'))
 if {x.get('id'):x.get('commit') for x in json_lock.get('repositories',[])}!={x.get('id'):x.get('commit') for x in entries}: errors.append('YAML/JSON upstream lock mismatch')
 if json_lock.get('version')!='1.0.0-draft': errors.append('JSON upstream lock version mismatch')
 reuse=json.loads((root/'config/upstreams/upstream-reuse-register.json').read_text(encoding='utf-8'))
 if {x.get('id'):x.get('commit') for x in reuse.get('upstreams',[])}!={x.get('id'):x.get('commit') for x in entries}: errors.append('upstream reuse register does not match source lock')
 if reuse.get('baseline')!='ORBIT 1.0.0-draft': errors.append('upstream reuse register baseline mismatch')
 roles=yaml.safe_load((root/'roles/ROLE_REGISTRY.yaml').read_text(encoding='utf-8'))
 if len(roles.get('roles',[]))!=30: errors.append('expected 30 role charters/registry entries')
 for item in entries:
  if not re.fullmatch(r'[0-9a-f]{40}',str(item.get('commit',''))): errors.append(f'invalid commit pin: {item.get("id")}')
 maus=next((x for x in entries if x.get('id')=='openmausbot'),{})
 if 'enterprise/' not in maus.get('exclude_paths',[]): errors.append('OpenMausBot enterprise/ missing from excluded paths')
 clone=root/'scripts/clone_upstreams.sh'
 if clone.exists():
  r=subprocess.run(['bash','-n',str(clone)],capture_output=True,text=True)
  if r.returncode: errors.append('clone_upstreams.sh syntax: '+r.stderr)
  s=clone.read_text(encoding='utf-8')
  if 'sparse-checkout' not in s or '!/enterprise/' not in s: errors.append('OpenMausBot enterprise sparse exclusion missing')
  clone_targets=set(re.findall(r'clone_pinned\s+(\S+)\s+(https://github\.com/[^ ]+\.git)',s))
  target_ids={name for name,url in clone_targets}
  locked_ids={x.get('id') for x in entries}
  if target_ids != locked_ids: errors.append('clone checkout folder names do not match the 50 canonical upstream IDs')
  for selector in ['--pydantic-ai','--ollama','--llama-cpp','--docling','--faster-whisper','--graphiti','--mcp-python-sdk','--openai-agents-python','--composio','--playwright','--markitdown','--chroma','--text-embeddings-inference','--transformers','--sherpa-onnx','--semantic-kernel','--home-assistant','--microsoft-agent-framework','--vllm','--sglang','--promptfoo','--haystack','--duckdb','--garak','--graphrag','--guardrails','--milvus','--google-adk','--openai-codex','--gemini-cli','--opensearch','--swe-agent','--faiss','--all-v10-new']:
   if selector not in s: errors.append(f'missing clone selector {selector}')
 for script in ['scripts/orbit_storage.py','scripts/repo_audit.py','scripts/import_upstream_path.py','scripts/orbit_repo_ops.py','scripts/init_orbit_storage.ps1','scripts/create_upstream_worktree.py','scripts/apply_staged_source.py','scripts/create_orbit_app_worktree.py','scripts/clone_upstreams.ps1']:
  if not (root/script).exists(): errors.append('missing operational script '+script)
 for script in ['scripts/apply_staged_source.py','scripts/create_orbit_app_worktree.py','scripts/clone_upstreams.ps1']:
  if not (root/script).exists(): errors.append('missing v1.0 repository operation '+script)
 component=yaml.safe_load((root/'docs/06-security/THIRD_PARTY_COMPONENT_REGISTER.yaml').read_text(encoding='utf-8'))
 component_ids={x.get('id') for x in component.get('components',[])}
 for rid in ['google-adk','openai-codex','gemini-cli','opensearch','swe-agent','faiss']:
  if rid not in component_ids: errors.append(f'component register missing {rid}')
 for rel in ['docs/13-guides/V10_START_HERE.md','docs/13-guides/V10_REPOSITORY_OPERATIONS_AND_SOURCE_CODE_USE.md','docs/02-research/V10_OPEN_SOURCE_FILE_LEVEL_ADOPTION_MAP.md','docs/02-research/ORBIT_REPOSITORY_OPERATIONS_ANALYSIS_V10.md','docs/08-development/V10_CTO_IMPLEMENTATION_WARROOM.md','docs/03-architecture/V10_INTEGRATED_PERSONAL_WORK_OPERATING_SYSTEM.md','docs/09-quality/V10_COMPETITIVE_PARITY_BENCHMARKS.md','docs/10-infrastructure/V10_500GB_STORAGE_OPERATIONS.md']:
  if not (root/rel).exists(): errors.append('missing v1.0 document '+rel)
 apply_helper=(root/'scripts/apply_staged_source.py').read_text(encoding='utf-8') if (root/'scripts/apply_staged_source.py').exists() else ''
 if "sha(src)!=f.get('sha256')" not in apply_helper or 'refusing to overwrite existing target' not in apply_helper or 'never git-adds' not in apply_helper:
  errors.append('apply_staged_source.py missing source hash/overwrite/no-auto-commit safeguards')
 api=yaml.safe_load((root/'docs/04-system-design/API_CONTRACTS.yaml').read_text(encoding='utf-8'))
 manifest_path=root/'PACKAGE_MANIFEST.json'
 if manifest_path.exists():
  m=json.loads(manifest_path.read_text(encoding='utf-8'))
  inventory={x['path']:x for x in m.get('files',[])}; actual={p.relative_to(root).as_posix():p for p in files}
  if set(inventory)!=set(actual): errors.append('manifest inventory mismatch')
  for rel,p in actual.items():
   e=inventory.get(rel)
   if e and (e.get('sha256')!=sha(p) or e.get('size_bytes')!=p.stat().st_size): errors.append(f'manifest hash mismatch: {rel}')
  if m.get('file_count_including_manifest')!=len(files)+1: errors.append('manifest file count mismatch')
  if m.get('version')!='1.0.0-draft': errors.append('manifest version mismatch')
 else: errors.append('manifest missing')
 report={'root':str(root),'files_including_manifest':len(files)+1,'files_checked_excluding_manifest':len(files),'markdown':sum(p.suffix.lower()=='.md' for p in files),'mermaid':sum(p.suffix.lower()=='.mmd' for p in files),'yaml':sum(p.suffix.lower() in {'.yaml','.yml'} for p in files),'json':sum(p.suffix.lower()=='.json' for p in files),'upstreams':len(entries),'api_paths':len(api.get('paths',{})),'errors':errors,'passed':not errors}
 print(json.dumps(report,indent=2)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
