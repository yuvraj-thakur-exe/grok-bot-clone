from __future__ import annotations

import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

TEXT_SUFFIXES = {
    ".md", ".mdx", ".txt", ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".sql", ".sh", ".bash", ".zsh",
    ".ps1", ".bat", ".cmd", ".html", ".css", ".scss", ".less", ".go", ".rs", ".java",
    ".c", ".h", ".hpp", ".cpp", ".cs", ".swift", ".kt", ".dart", ".vue", ".svelte",
    ".xml", ".graphql", ".proto", ".dockerfile", ".tf", ".hcl",
}
ALLOWED_DOTFILES = {".gitignore", ".dockerignore", ".editorconfig", ".npmrc.example"}
EXCLUDED_DIRS = {
    ".git", ".hg", ".svn", ".venv", "venv", "env", "node_modules", "__pycache__", ".mypy_cache",
    ".pytest_cache", ".ruff_cache", ".next", ".turbo", ".cache", "dist", "build", "coverage",
    "target", "vendor", "third_party", ".idea", ".vscode", ".orbit",
}
SENSITIVE_PARTS = {
    ".env", ".aws", ".ssh", ".gnupg", "secrets", "secret", "credentials", "credential",
    "private", "certs", "certificates", "tokens", "token-cache",
}
SECRET_PATTERNS = [
    (re.compile(r"(?i)(authorization\s*:\s*bearer\s+)[A-Za-z0-9._~+/-]+=*"), r"\1[REDACTED]"),
    (re.compile(r"(?i)((?:api[_-]?key|access[_-]?token|refresh[_-]?token|client_secret|password)\s*[=:]\s*['\"]?)[A-Za-z0-9._~+/-]{8,}"), r"\1[REDACTED]"),
    (re.compile(r"\b(?:sk-[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,}|xox[baprs]-[A-Za-z0-9-]{16,})\b"), "[REDACTED]"),
    (re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----.*?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", re.DOTALL), "[REDACTED PRIVATE KEY]"),
]

def _safe_relative(root: Path, value: str) -> Path:
    path = Path(value)
    if path.is_absolute():
        raise ValueError(f"Context path must be relative to workspace root: {value}")
    resolved = (root / path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"Context path escapes workspace root: {value}") from exc
    return resolved


def _is_sensitive(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    for part in rel.parts:
        lowered = part.lower()
        if lowered in SENSITIVE_PARTS or lowered.startswith(".env"):
            return True
    if path.suffix.lower() in {".pem", ".key", ".p12", ".pfx", ".keystore", ".jks", ".sqlite", ".db", ".parquet", ".pt", ".pth", ".safetensors"}:
        return True
    if path.name.lower() in {"id_rsa", "id_ed25519", "known_hosts", "authorized_keys"}:
        return True
    return False


def _candidate_files(root: Path, selections: list[str]) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for selection in selections:
        base = _safe_relative(root, selection)
        if base.is_file():
            candidates = [base]
        elif base.is_dir():
            candidates = sorted(base.rglob("*"), key=lambda p: p.as_posix().lower())
        else:
            continue
        for path in candidates:
            if path in seen or path.is_symlink() or not path.is_file():
                continue
            try:
                rel = path.relative_to(root)
            except ValueError:
                continue
            if any(part in EXCLUDED_DIRS for part in rel.parts[:-1]):
                continue
            if _is_sensitive(path, root):
                continue
            if path.name not in ALLOWED_DOTFILES and path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            seen.add(path)
            found.append(path)
    return found


def _git_head(root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True,
            text=True, timeout=3, shell=False,
        )
        return result.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def _redact(content: str) -> tuple[str, int]:
    count = 0
    for pattern, replacement in SECRET_PATTERNS:
        content, replaced = pattern.subn(replacement, content)
        count += replaced
    return content, count


def create_context_pack(
    workspace_root: str | Path,
    selections: list[str],
    output_path: str | Path,
    budget_tokens: int = 30_000,
    max_file_bytes: int = 128_000,
) -> dict[str, Any]:
    root = Path(workspace_root).expanduser().resolve()
    if not root.is_dir():
        raise NotADirectoryError(root)
    if budget_tokens < 500 or budget_tokens > 200_000:
        raise ValueError("budget_tokens must be between 500 and 200000.")
    if max_file_bytes < 256 or max_file_bytes > 2_000_000:
        raise ValueError("max_file_bytes must be between 256 and 2000000.")
    out = Path(output_path).expanduser()
    if not out.is_absolute():
        out = root / out
    out = out.resolve()
    if out == root or out.is_dir():
        raise ValueError("Output must be a file path, not the workspace root or a directory.")
    try:
        out.relative_to(root)
        output_inside_root = True
    except ValueError:
        output_inside_root = False

    manifest_out = out.with_suffix(out.suffix + ".manifest.json")
    files = _candidate_files(root, selections)
    files = [path for path in files if path not in {out, manifest_out}]
    used_tokens = 0
    entries: list[dict[str, Any]] = []
    sections: list[str] = [
        "# ORBIT context pack",
        "",
        f"> Generated: {datetime.now(timezone.utc).isoformat()}",
        f"> Workspace: `{root}`",
        f"> Git HEAD: `{_git_head(root) or 'not available'}`",
        f"> Token budget: {budget_tokens} approximate tokens. Estimate uses UTF-8 characters / 4, not a provider tokenizer.",
        "> Sensitive paths, binary files, symlinks and build/cache folders are excluded. Secret-pattern redaction is best-effort, not a security scanner.",
        "",
    ]
    skipped: list[dict[str, str]] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        try:
            size = path.stat().st_size
            if size > max_file_bytes:
                skipped.append({"path": rel, "reason": f"file exceeds {max_file_bytes} byte limit"})
                continue
            raw = path.read_bytes()
            if b"\x00" in raw:
                skipped.append({"path": rel, "reason": "binary content"})
                continue
            content = raw.decode("utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            skipped.append({"path": rel, "reason": f"read/decode error: {exc.__class__.__name__}"})
            continue

        content, redactions = _redact(content)
        token_cost = max(1, (len(content) + 3) // 4) + 30
        truncated = False
        remaining = budget_tokens - used_tokens
        if token_cost > remaining:
            marker = "\n\n[TRUNCATED: context budget reached]\n"
            available_chars = max(0, (remaining - 30) * 4 - len(marker))
            if available_chars < 256:
                skipped.append({"path": rel, "reason": "remaining context budget too small"})
                continue
            content = content[:available_chars] + marker
            token_cost = max(1, (len(content) + 3) // 4) + 30
            truncated = True

        digest = hashlib.sha256(raw).hexdigest()
        sections.extend([
            f"## `{rel}`",
            "",
            f"- Size: {size} bytes | SHA-256: `{digest}` | Estimated tokens: {token_cost} | Redactions: {redactions}",
            "",
            "```text",
            content.rstrip(),
            "```",
            "",
        ])
        used_tokens += token_cost
        entries.append({"path": rel, "bytes": size, "sha256": digest, "estimated_tokens": token_cost, "redactions": redactions, "truncated": truncated})
        if used_tokens >= budget_tokens:
            break

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(sections), encoding="utf-8")
    manifest = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "workspace_root": str(root),
        "git_head": _git_head(root),
        "budget_tokens_estimated": budget_tokens,
        "used_tokens_estimated": used_tokens,
        "estimator": "UTF-8 character count divided by four, plus 30-token per-file overhead; not provider-exact.",
        "output": str(out),
        "output_inside_workspace": output_inside_root,
        "included": entries,
        "skipped": skipped,
    }
    manifest_out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest
