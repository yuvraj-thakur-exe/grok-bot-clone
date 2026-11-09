from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from orbit_cli.context import create_context_pack


class ContextPackTests(unittest.TestCase):
    def test_pack_includes_code_and_excludes_sensitive_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("ORBIT project overview", encoding="utf-8")
            (root / "src").mkdir()
            (root / "src" / "main.py").write_text("print('hello')", encoding="utf-8")
            (root / ".env").write_text("API_KEY=super-secret-key-123", encoding="utf-8")
            out = root / ".orbit" / "context.md"
            result = create_context_pack(root, ["README.md", "src", ".env"], out, budget_tokens=2000)
            content = out.read_text(encoding="utf-8")
            self.assertIn("README.md", content)
            self.assertIn("src/main.py", content)
            self.assertNotIn("super-secret-key-123", content)
            self.assertEqual(len(result["included"]), 2)
            self.assertTrue(Path(str(out) + ".manifest.json").exists())

    def test_token_budget_bounds_included_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.md").write_text("x" * 10000, encoding="utf-8")
            result = create_context_pack(root, ["a.md"], root / "pack.md", budget_tokens=500)
            self.assertLessEqual(result["used_tokens_estimated"], 500)
            self.assertTrue(result["included"][0]["truncated"])

    def test_previous_output_and_manifest_are_not_reingested(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source.md").write_text("source material", encoding="utf-8")
            output = root / "pack.md"
            create_context_pack(root, ["."], output, budget_tokens=1000)
            result = create_context_pack(root, ["."], output, budget_tokens=1000)
            included_paths = {item["path"] for item in result["included"]}
            self.assertEqual(included_paths, {"source.md"})

    def test_common_token_shapes_are_redacted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            secret = "sk-" + "A" * 28
            (root / "config.md").write_text(f"token = {secret}", encoding="utf-8")
            output = root / "pack.md"
            result = create_context_pack(root, ["config.md"], output, budget_tokens=1000)
            packed = output.read_text(encoding="utf-8")
            self.assertNotIn(secret, packed)
            self.assertGreaterEqual(result["included"][0]["redactions"], 1)


if __name__ == "__main__":
    unittest.main()
