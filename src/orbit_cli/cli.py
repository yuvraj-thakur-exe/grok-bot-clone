from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .context import create_context_pack
from .platforms import command_report
from .storage import init_storage, storage_status
from .task_runner import execute_manifest, validate_manifest


def _json_print(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="orbit",
        description="ORBIT cross-platform developer toolkit. Core commands use Python's standard library only.",
    )
    parser.add_argument("--version", action="version", version=f"ORBIT DevKit {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor", help="Inspect host OS, Python and optional developer tools.")

    storage = sub.add_parser("storage", help="Initialize or inspect the dedicated ORBIT development volume.")
    storage_sub = storage.add_subparsers(dest="storage_action", required=True)
    init = storage_sub.add_parser("init", help="Create the ORBIT folder layout and manifest only.")
    init.add_argument("root", help="Absolute path on the verified target drive.")
    init.add_argument("--expected-capacity-gb", type=int, default=500)
    init.add_argument("--reserve-gb", type=int, default=60)
    status = storage_sub.add_parser("status", help="Show capacity, reserve, soft-folder usage and alerts.")
    status.add_argument("root")
    status.add_argument("--reserve-gb", type=int)

    context = sub.add_parser("context-pack", help="Build a bounded, redacted, deterministic code-context pack.")
    context.add_argument("--root", default=".")
    context.add_argument("--paths", nargs="+", default=["README.md", "AGENTS.md", "docs", "src", "apps", "packages"])
    context.add_argument("--output", default=".orbit/context-pack.md")
    context.add_argument("--budget-tokens", type=int, default=30_000)
    context.add_argument("--max-file-bytes", type=int, default=128_000)

    run = sub.add_parser("run", help="Run a validated JSON task DAG with bounded parallelism.")
    run.add_argument("--manifest", default="configs/tasks.example.json")
    run.add_argument("--root", default=".")
    run.add_argument("--max-parallel", type=int, default=3)
    run.add_argument("--allow-workspace-write", action="store_true", help="Explicitly permit tasks marked workspace-write.")
    run.add_argument("--validate-only", action="store_true")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "doctor":
            report = command_report()
            report["toolkit_version"] = __version__
            report["python_minimum"] = "3.11"
            report["python_supported"] = sys.version_info >= (3, 11)
            _json_print(report)
            return 0 if report["python_supported"] else 2

        if args.command == "storage":
            if args.storage_action == "init":
                _json_print(init_storage(args.root, args.expected_capacity_gb, args.reserve_gb))
            else:
                _json_print(storage_status(args.root, args.reserve_gb))
            return 0

        if args.command == "context-pack":
            result = create_context_pack(args.root, args.paths, args.output, args.budget_tokens, args.max_file_bytes)
            print(f"Context pack: {result['output']}")
            print(f"Included files: {len(result['included'])}; skipped: {len(result['skipped'])}; estimated tokens: {result['used_tokens_estimated']}/{result['budget_tokens_estimated']}")
            print(f"Manifest: {Path(result['output'] + '.manifest.json')}")
            if result["skipped"]:
                print("Some files were skipped. Inspect the manifest for reasons.")
            return 0

        if args.command == "run":
            if args.validate_only:
                tasks, root = validate_manifest(args.manifest, args.root)
                print(f"Validated {len(tasks)} tasks for workspace {root}.")
                return 0
            result = asyncio.run(execute_manifest(args.manifest, args.root, args.max_parallel, args.allow_workspace_write))
            _json_print(result)
            return 0 if all(x["status"] in {"passed", "skipped"} for x in result["results"]) else 2

        parser.error("Unknown command.")
    except (ValueError, FileNotFoundError, NotADirectoryError, PermissionError, OSError) as exc:
        print(f"orbit: error: {exc}", file=sys.stderr)
        return 2
    return 0
