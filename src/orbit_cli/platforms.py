from __future__ import annotations

import os
import platform
import shutil
import sys
from typing import Any


def platform_id() -> str:
    if sys.platform.startswith("win"):
        return "windows"
    if sys.platform == "darwin":
        return "macos"
    if sys.platform.startswith("linux"):
        return "linux"
    return "unknown"


def command_report() -> dict[str, Any]:
    commands = ("git", "node", "npm", "pnpm", "uv", "docker", "pwsh", "powershell", "bash", "zsh", "task")
    return {
        "os": platform_id(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python": sys.version.split()[0],
        "python_executable": sys.executable,
        "is_wsl": bool(os.environ.get("WSL_DISTRO_NAME")),
        "commands": {name: shutil.which(name) for name in commands},
    }
