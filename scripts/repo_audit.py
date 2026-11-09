#!/usr/bin/env python3
"""Create a static inventory report for a local Git repository without executing its code."""
from __future__ import annotations
import argparse, json, re, subprocess, sys, os
from pathlib import Path
from datetime import datetime, timezone

IGNORE={'.git','node_modules','.venv','venv','__pycache__','.next','dist','build','target','coverage','.pytest_cache','.mypy_cache','.ruff_cache','vendor','upstream'}
SUFFIX={'.ts':'TypeScript','.tsx':'TypeScript React','.js':'JavaScript','.jsx':'JavaScript React','.mjs':'JavaScript','.cjs':'JavaScript','.py':'Python','.go':'Go','.rs':'Rust','.java':'Java','.kt':'Kotlin','.cs':'C#','.cpp':'C++','.c':'C','.h':'C/C++ header','.hpp':'C++ header','.md':'Markdown','.yaml':'YAML','.yml':'YAML','.json':'JSON','.sql':'SQL','.sh':'Shell','.ps1':'PowerShell','.html':'HTML','.css':'CSS','.toml':'TOML'}
LICENSE_NAMES={'LICENSE','LICENSE.md','LICENSE.txt','COPYING','NOTICE','LICENSING.md'}
SECRET_PATTERNS=[
 ('PRIVATE_KEY',re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')),
 ('GITHUB_TOKEN',re.compile(r'\bgh[pousr]_[A-Za-z0-9_]{20,}\b')),
 ('SLACK_TOKEN',re.compile(r'\bxox[baprs]-[A-Za-z0-9-]{15,}\b')),
 ('AWS_ACCESS_KEY',re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
 ('GENERIC_SECRET_ASSIGNMENT',re.compile(r'(?i)\b(api[_-]?key|access[_-]?token|client[_-]?secret|password)\b\s*[:=]\s*["\'][^"\']{12,}["\']')),
]

def git(root,*args):
    try:
        r=subprocess.run(['git','-C',str(root),*args],capture_output=True,text=True,timeout=20)
        return r.stdout.strip() if r.returncode==0 else None
    except Exception: return None

def ignored(p): return any(part in IGNORE for part in p.parts)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('repository',type=Path)
    ap.add_argument('--output-dir',type=Path,default=None)
    ap.add_argument('--max-files',type=int,default=100000)
    ns=ap.parse_args()
    root=ns.repository.resolve()
    if not root.is_dir(): print(f"Not a directory: {root}",file=sys.stderr); return 2
    commit=git(root,'rev-parse','HEAD')
    origin=git(root,'remote','get-url','origin')
    branch=git(root,'branch','--show-current') or '(detached or unavailable)'
    status=git(root,'status','--porcelain')
    counts={}; largest=[]; projects=[]; license_files=[]; ci_files=[]; tests=[]; sensitive=[]; secret_findings=[]; total=0; bytes_total=0
    for p in root.rglob('*'):
        try:
            rel=p.relative_to(root)
            if ignored(rel): continue
            if p.is_symlink(): continue
            if not p.is_file(): continue
            total+=1
            size=p.stat().st_size; bytes_total+=size
            ext=p.suffix.lower(); lang=SUFFIX.get(ext,'Other')
            counts[lang]=counts.get(lang,0)+1
            largest.append((size,rel.as_posix()))
            name=p.name.lower()
            if p.name.upper() in LICENSE_NAMES: license_files.append(rel.as_posix())
            if '.github/workflows/' in rel.as_posix().replace('\\','/') or rel.name=='Jenkinsfile': ci_files.append(rel.as_posix())
            if re.search(r'(^|/)(tests?|__tests__|spec)(/|$)|(^|/)(test_|.*_test\.)',rel.as_posix(),re.I): tests.append(rel.as_posix())
            if name.startswith('.env') and name != '.env.example' or name in {'id_rsa','id_ed25519','credentials.json','secrets.json'} or ext in {'.pem','.p12','.pfx'}:
                sensitive.append(rel.as_posix())
            if ext in {'.ts','.tsx','.js','.jsx','.mjs','.cjs','.py','.go','.rs','.sh','.ps1','.yaml','.yml','.json','.toml'} and size < 2_000_000:
                try: txt=p.read_text(encoding='utf-8',errors='ignore')
                except OSError: txt=''
                for rule,pattern in SECRET_PATTERNS:
                    for m in pattern.finditer(txt):
                        line=txt.count('\n',0,m.start())+1
                        secret_findings.append({'rule':rule,'path':rel.as_posix(),'line':line,'value_printed':False})
                        if len(secret_findings)>500: break
            if name in {'package.json','pyproject.toml','go.mod','cargo.toml','pom.xml','composer.json','requirements.txt','pnpm-workspace.yaml'}:
                projects.append(rel.as_posix())
            if total>=ns.max_files: break
        except (OSError,PermissionError): continue
    files_at_root=sorted([x.name for x in root.iterdir() if x.is_file()])[:100]
    result={
      'generated_at_utc':datetime.now(timezone.utc).isoformat(),'repository_path':str(root),'origin':origin,'commit':commit,'branch':branch,
      'git_worktree_clean':not bool(status),'git_status_lines':len(status.splitlines()) if status else 0,
      'files_scanned':total,'total_bytes':bytes_total,'languages':dict(sorted(counts.items(),key=lambda x:-x[1])),
      'root_files':files_at_root,'project_manifests':sorted(projects),'license_and_notice_files':sorted(set(license_files)),
      'ci_files':sorted(set(ci_files))[:150],'test_paths_sample':sorted(set(tests))[:300],
      'largest_files': [{'bytes':b,'path':p} for b,p in sorted(largest,reverse=True)[:30]],
      'sensitive_filename_flags':sorted(set(sensitive)), 'secret_pattern_flags':secret_findings[:500],
      'limitations':['Static inventory only; no source code executed.','Secret checks are heuristic; absence of findings is not proof of no secrets.','Nested licenses and dependencies require manual/package-scanner review.','This report does not establish security or legal clearance.']
    }
    outdir=(ns.output_dir or (Path(os.environ['ORBIT_HOME'])/'00-control'/'repo-audits' if os.environ.get('ORBIT_HOME') else Path(__file__).resolve().parents[1]/'reports'/'repo-audits')).resolve(); outdir.mkdir(parents=True,exist_ok=True)
    slug=re.sub(r'[^A-Za-z0-9._-]+','-',root.name).strip('-') or 'repo'
    tag=(commit or 'no-git')[:12]
    jpath=outdir/f'{slug}-{tag}.json'; mpath=outdir/f'{slug}-{tag}.md'
    jpath.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    md=['# Repository audit: '+root.name,'',f"- Path: `{root}`",f"- Origin: `{origin or 'unavailable'}`",f"- Commit: `{commit or 'not a Git checkout'}`",f"- Branch: `{branch}`",f"- Clean worktree: `{result['git_worktree_clean']}`",f"- Files scanned: {total}",f"- Total bytes: {bytes_total}",'','## Languages','']
    md += [f'- {k}: {v}' for k,v in result['languages'].items()]
    md += ['', '## Project manifests',''] + [f'- `{x}`' for x in result['project_manifests']]
    md += ['', '## License/notice files',''] + [f'- `{x}`' for x in result['license_and_notice_files']]
    md += ['', '## Sensitive filename flags',''] + ([f'- `{x}`' for x in result['sensitive_filename_flags']] or ['- None detected by filename heuristic'])
    md += ['', '## Secret-pattern flags (values never printed)',''] + ([f"- `{x['path']}:{x['line']}` — {x['rule']}" for x in result['secret_pattern_flags']] or ['- None detected by limited patterns'])
    md += ['', '## Limitations',''] + [f'- {x}' for x in result['limitations']]
    mpath.write_text('\n'.join(md)+'\n',encoding='utf-8')
    print(json.dumps({'status':'completed','report_markdown':str(mpath),'report_json':str(jpath),'files_scanned':total,'warnings':len(sensitive)+len(secret_findings),'git_clean':result['git_worktree_clean']},indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
