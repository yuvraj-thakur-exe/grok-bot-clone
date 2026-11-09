#!/usr/bin/env python3
"""Static, non-executing intake report for an Agent Skill folder. Not a malware scanner."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

REQUIRED = {"name", "description"}
RISK_PATTERNS = {
    "shell execution": re.compile(r"\b(subprocess|os\.system|child_process|exec\(|spawn\()", re.I),
    "credential or environment access": re.compile(r"\b(process\.env|os\.environ|API_KEY|SECRET|TOKEN|password)\b", re.I),
    "network access": re.compile(r"\b(requests\.|fetch\(|axios\.|http[s]?://|socket\.)", re.I),
    "filesystem mutation": re.compile(r"\b(writeFile|unlink|rmdir|shutil\.rmtree|open\([^\n]*['\"]w)", re.I),
    "dynamic execution": re.compile(r"\b(eval\(|exec\(|Function\()", re.I),
}

def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        return {}, "Missing YAML frontmatter delimiter"
    end = text.find('\n---', 4)
    if end < 0:
        return {}, "Unterminated YAML frontmatter"
    block = text[4:end]
    result = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if m:
            value = m.group(2).strip().strip('"\'')
            result[m.group(1)] = value
    return result, None

def sha(path: Path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('skill_dir', nargs='?', default=None)
    ap.add_argument('--help-only', action='store_true')
    args = ap.parse_args()
    if not args.skill_dir:
        ap.print_help(); return 0
    root = Path(args.skill_dir).resolve()
    if not root.is_dir():
        print(json.dumps({"error": f"Not a directory: {root}"}, indent=2)); return 2
    skill_file = root/'SKILL.md'
    if not skill_file.is_file():
        print(json.dumps({"error": "SKILL.md is required"}, indent=2)); return 2
    body = skill_file.read_text(encoding='utf-8', errors='replace')
    front, parse_error = parse_frontmatter(body)
    missing = sorted(REQUIRED - set(front))
    files = sorted(p for p in root.rglob('*') if p.is_file())
    findings = []
    for p in files:
        if p.is_symlink():
            findings.append({"severity":"blocker","path":str(p.relative_to(root)),"finding":"symlink in skill package requires manual review"})
            continue
        if p.suffix.lower() in {'.py','.js','.mjs','.cjs','.ts','.sh','.ps1','.bat'}:
            content=p.read_text(encoding='utf-8',errors='replace')
            for label, pat in RISK_PATTERNS.items():
                if pat.search(content):
                    findings.append({"severity":"review","path":str(p.relative_to(root)),"finding":f"potential {label}"})
    license_files=[p.name for p in files if p.name.lower() in {'license','license.md','license.txt','notice','notice.md'}]
    report={
      "skill_directory":str(root),
      "skill_file_sha256":sha(skill_file),
      "frontmatter":front,
      "frontmatter_error":parse_error,
      "missing_required_fields":missing,
      "license_notice_files":license_files,
      "files":[{"path":str(p.relative_to(root)),"size_bytes":p.stat().st_size,"sha256":sha(p)} for p in files],
      "findings":findings,
      "execution_performed":False,
      "approval":"NOT_APPROVED",
      "limitations":["Static pattern checks are heuristic and may miss malicious behavior.","This tool does not establish license rights or prove the package is safe.","Never execute a discovered skill before source, license, dependency and sandbox review."]
    }
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 1 if parse_error or missing else 0

if __name__ == '__main__': raise SystemExit(main())
