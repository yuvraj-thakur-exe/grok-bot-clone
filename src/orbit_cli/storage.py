from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GB = 1_000_000_000  # Decimal GB, matching drive-manufacturer capacity labels.

DEFAULT_LAYOUT: dict[str, int] = {
    "00-control": 10,
    "01-upstream-checkouts": 100,
    "02-workspaces": 100,
    "03-models": 90,
    "04-data-memory": 35,
    "05-artifacts": 25,
    "06-evaluations": 20,
    "07-logs-cache": 5,
    "08-backups": 25,
    "09-quarantine": 10,
    "10-source-intake": 20,
}


def _validate_storage_root(path: str | Path) -> Path:
    root = Path(path).expanduser()
    if not root.is_absolute():
        raise ValueError("Storage root must be an absolute path on the verified target volume.")
    resolved = root.resolve(strict=False)
    if resolved == Path(resolved.anchor) or resolved == Path.home().resolve():
        raise ValueError("Refusing to initialize a filesystem root or the user's home directory.")
    if resolved.exists() and not resolved.is_dir():
        raise ValueError("Storage path exists but is not a directory.")
    if resolved.parent.exists() and not resolved.parent.is_dir():
        raise ValueError("Storage parent is not a directory.")
    return resolved


def init_storage(path: str | Path, expected_capacity_gb: int = 500, reserve_gb: int = 60) -> dict[str, Any]:
    if expected_capacity_gb <= 0 or reserve_gb <= 0 or reserve_gb >= expected_capacity_gb:
        raise ValueError("Capacity and reserve must be positive; reserve must be smaller than capacity.")
    root = _validate_storage_root(path)
    if not root.parent.exists():
        raise ValueError("The target volume or parent directory must already exist. Mount/format it manually first.")

    # Deliberately creates directories only. No disk formatting, partitioning, mounting,
    # encryption, quota changes, broad deletion, or implicit model/repository downloads.
    root.mkdir(parents=False, exist_ok=True)
    created_directories: list[str] = []
    for dirname in DEFAULT_LAYOUT:
        target = root / dirname
        existed = target.exists()
        target.mkdir(exist_ok=True)
        if not existed:
            created_directories.append(dirname)

    manifest_path = root / "orbit-storage.json"
    usage = shutil.disk_usage(root)
    manifest = {
        "schema_version": 1,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "root": str(root),
        "expected_capacity_gb_decimal": expected_capacity_gb,
        "reserve_gb_decimal": reserve_gb,
        "soft_targets_gb_decimal": DEFAULT_LAYOUT,
        "soft_targets_total_gb": sum(DEFAULT_LAYOUT.values()),
        "note": "Targets are advisory. This helper does not format, partition, encrypt, mount, or enforce quotas.",
    }
    if manifest_path.exists():
        try:
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise ValueError(f"Existing {manifest_path.name} is not valid JSON; refusing to overwrite it.") from exc
        if existing.get("root") != str(root):
            raise ValueError("Existing storage manifest points to a different root; refusing to overwrite it.")
        manifest = existing
    else:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    warnings: list[str] = []
    if usage.total < expected_capacity_gb * GB * 0.97:
        warnings.append(
            f"Mounted volume reports {usage.total / GB:.1f} decimal GB, below the {expected_capacity_gb} GB target. "
            "Confirm the correct disk before downloading repositories or models."
        )
    return {"root": str(root), "created_directories": created_directories, "manifest": str(manifest_path), "warnings": warnings}


def storage_status(path: str | Path, reserve_gb: int | None = None) -> dict[str, Any]:
    if reserve_gb is not None and (not isinstance(reserve_gb, int) or isinstance(reserve_gb, bool) or reserve_gb <= 0):
        raise ValueError("reserve_gb must be a positive integer.")
    root = _validate_storage_root(path)
    if not root.exists():
        raise FileNotFoundError(f"Storage root does not exist: {root}")
    usage = shutil.disk_usage(root)
    manifest_path = root / "orbit-storage.json"
    if reserve_gb is None and manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            reserve_gb = int(manifest.get("reserve_gb_decimal", 60))
        except (OSError, ValueError, json.JSONDecodeError):
            reserve_gb = 60
    reserve_gb = 60 if reserve_gb is None else reserve_gb
    if not isinstance(reserve_gb, int) or isinstance(reserve_gb, bool) or reserve_gb <= 0:
        raise ValueError("Configured reserve_gb must be a positive integer.")

    used = usage.total - usage.free
    used_pct = (used / usage.total * 100) if usage.total else 0.0
    free_gb = usage.free / GB
    if used_pct >= 95:
        level = "CRITICAL"
        action = "Stop nonessential writes and recover capacity. Do not delete user data automatically."
    elif used_pct >= 90:
        level = "BLOCK_BULK_WRITES"
        action = "Block model downloads and large builds until storage is reviewed."
    elif used_pct >= 80:
        level = "WARNING"
        action = "Alert the operator and review large caches, worktrees, and artifacts."
    else:
        level = "NORMAL"
        action = "Continue; keep the reserve available."
    if free_gb < reserve_gb and level == "NORMAL":
        level = "RESERVE_BREACHED"
        action = "Free space is below the configured reserve; pause bulk downloads and builds."

    folder_usage: dict[str, float | None] = {}
    for dirname in DEFAULT_LAYOUT:
        folder = root / dirname
        if folder.exists():
            total_bytes = 0
            for item in folder.rglob("*"):
                try:
                    if item.is_file() and not item.is_symlink():
                        total_bytes += item.stat().st_size
                except OSError:
                    continue
            folder_usage[dirname] = round(total_bytes / GB, 3)
        else:
            folder_usage[dirname] = None

    return {
        "root": str(root),
        "total_gb_decimal": round(usage.total / GB, 2),
        "used_gb_decimal": round(used / GB, 2),
        "free_gb_decimal": round(free_gb, 2),
        "used_percent": round(used_pct, 1),
        "reserve_gb_decimal": reserve_gb,
        "reserve_remaining_gb_decimal": round(free_gb - reserve_gb, 2),
        "status": level,
        "recommended_action": action,
        "folders_gb_decimal": folder_usage,
    }
