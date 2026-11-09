#!/usr/bin/env python3
"""Initialize and inspect an ORBIT storage root. It never formats or partitions disks."""
from __future__ import annotations
import argparse, json, shutil, sys
from pathlib import Path
from datetime import datetime, timezone

FOLDERS = [
    ("00-control", 10, "manifests, operation docs and control files"),
    ("01-upstream-checkouts", 100, "50 pinned upstream repositories and selected worktrees"),
    ("02-workspaces", 100, "ORBIT source worktrees, builds and disposable jobs"),
    ("03-models", 90, "approved model artifacts and inference caches"),
    ("04-data-memory", 35, "encrypted user data, memories and indexes"),
    ("05-artifacts", 25, "generated reports, documents, media and exports"),
    ("06-evaluations", 20, "datasets, traces and benchmark outputs"),
    ("07-logs-cache", 5, "redacted logs and rebuildable caches"),
    ("08-backups", 25, "encrypted snapshots and restore evidence"),
    ("09-quarantine", 10, "untrusted source packages and skills"),
    ("10-source-intake", 20, "explicit upstream code imports pending review"),
]
TOTAL = sum(x[1] for x in FOLDERS)
RESERVE = 500 - TOTAL

def manifest(root: Path):
    return {
        "schema_version": 1,
        "baseline": "ORBIT 1.0.0-draft",
        "root": str(root),
        "capacity_target_gb_decimal": 500,
        "allocation_mode": "soft_targets_not_hard_quotas",
        "target_allocated_gb": TOTAL,
        "free_reserve_target_gb": RESERVE,
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "folders": [{"path": n, "target_gb": g, "purpose": p} for n,g,p in FOLDERS],
        "security": {"encrypt_sensitive_data": True, "secrets_in_model_context": False, "same_disk_is_disaster_backup": False},
        "notes": ["This tool does not partition, format, encrypt or impose quotas.", "A disk's capacity does not increase RAM or VRAM.", "Use a separate physical/cloud destination for critical backup copies."]
    }

def init(path: Path, min_total_gb: float = 450, min_free_gb: float = 200, skip_capacity_check: bool = False):
    if not path.is_absolute():
        raise ValueError("Storage root must be an absolute path")
    path.mkdir(parents=True, exist_ok=True)
    usage = shutil.disk_usage(path)
    # A marketed 500 GB drive is around 465 GiB after decimal/binary conversion and formatting.
    if not skip_capacity_check:
        min_total = min_total_gb * 1_000_000_000
        min_free = min_free_gb * 1_000_000_000
        if usage.total < min_total:
            raise ValueError(f"Target volume is too small: {usage.total/1e9:.1f} GB; need at least {min_total_gb:.0f} GB total")
        if usage.free < min_free:
            raise ValueError(f"Target volume has only {usage.free/1e9:.1f} GB free; need at least {min_free_gb:.0f} GB free")
    for name, _, _ in FOLDERS:
        (path / name).mkdir(exist_ok=True)
    data = manifest(path)
    out = path / ".orbit-storage.json"
    if out.exists():
        raise FileExistsError(f"{out} already exists; refusing to overwrite storage configuration")
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status":"initialized","root":str(path),"folder_count":len(FOLDERS),"target_allocated_gb":TOTAL,"free_reserve_target_gb":RESERVE,"actual_free_gib":round(usage.free/1024**3,1),"manifest":str(out)}, indent=2))

def status(path: Path):
    cfg = path / ".orbit-storage.json"
    if not cfg.exists():
        raise FileNotFoundError(f"No .orbit-storage.json at {path}; run init first")
    data = json.loads(cfg.read_text(encoding="utf-8"))
    rows=[]
    for item in data["folders"]:
        p=path/item["path"]
        size=0
        for f in p.rglob("*"):
            try:
                if f.is_file() and not f.is_symlink(): size += f.stat().st_size
            except OSError: pass
        rows.append({"path":item["path"],"target_gb":item["target_gb"],"used_gb":round(size/1e9,3)})
    usage=shutil.disk_usage(path)
    print(json.dumps({"root":str(path),"volume_total_gib":round(usage.total/1024**3,2),"volume_free_gib":round(usage.free/1024**3,2),"folders":rows},indent=2))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("init"); a.add_argument("path",type=Path); a.add_argument("--min-total-gb",type=float,default=450); a.add_argument("--min-free-gb",type=float,default=200); a.add_argument("--skip-capacity-check",action="store_true",help="test only; never use for real drive initialization")
    b=sub.add_parser("status"); b.add_argument("path",type=Path)
    ns=p.parse_args()
    try:
        if ns.cmd=="init": init(ns.path,ns.min_total_gb,ns.min_free_gb,ns.skip_capacity_check)
        else: status(ns.path)
    except Exception as e:
        print(f"ERROR: {e}",file=sys.stderr); return 2
    return 0
if __name__=="__main__": raise SystemExit(main())
