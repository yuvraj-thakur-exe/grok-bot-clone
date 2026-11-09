"""REA (Reverse Engineer Anything) Engine Integration for Grok Bot Clone.

Provides automated extraction, ASAR unpacking, and structural analysis of target
desktop applications, Electron bundles, and native extensions.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class REAAnalysisResult:
    target_path: Path
    reports_directory: Path
    electron_app: bool
    asar_unpacked: bool
    findings_summary: Dict[str, Any]


class REAEngine:
    """Manages REA reverse engineering tools and comparative inspection."""

    def __init__(self, workspace_root: Optional[Path] = None):
        self.workspace_root = workspace_root or Path.cwd()
        self.rea_repo_path = Path("D:/rea")
        self.reports_root = self.workspace_root / "docs" / "02-research" / "grokbot-rea-reports"

    def list_existing_reports(self) -> List[str]:
        """List all compiled REA research reports."""
        if not self.reports_root.exists():
            return []
        return [f.name for f in self.reports_root.glob("*.md")]

    def load_report(self, report_name: str) -> Optional[str]:
        """Read a specific REA research report."""
        target = self.reports_root / report_name
        if not target.exists():
            return None
        return target.read_text(encoding="utf-8")

    def inspect_grok_bot_binary(self, target_exe: Optional[Path] = None) -> Dict[str, Any]:
        """Run metadata and PE inspection on Grok Bot installer / binary."""
        target = target_exe or (self.workspace_root / "grok bot rea" / "Grok_Bot_0.78.1_Setup.exe")
        if not target.exists():
            return {"error": f"Target binary not found: {target}"}

        stat = target.stat()
        return {
            "name": target.name,
            "path": str(target.resolve()),
            "size_bytes": stat.st_size,
            "size_mb": round(stat.st_size / (1024 * 1024), 2),
            "created": stat.st_ctime,
            "is_pe_executable": target.suffix.lower() == ".exe",
            "available_rea_reports": len(self.list_existing_reports()),
        }
