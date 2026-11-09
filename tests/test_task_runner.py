from __future__ import annotations

import asyncio
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from orbit_cli.task_runner import execute_manifest, validate_manifest


class TaskManifestTests(unittest.TestCase):
    def _write(self, root: Path, data: dict) -> Path:
        path = root / "tasks.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_valid_dag_is_accepted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "a", "argv": ["@python", "--version"], "cwd": "."},
                {"id": "b", "argv": ["@python", "--version"], "cwd": ".", "depends_on": ["a"]}
            ]})
            tasks, workspace = validate_manifest(path, root)
            self.assertEqual(len(tasks), 2)
            self.assertEqual(workspace, root.resolve())

    def test_shell_string_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "bad", "command": "rm -rf /", "argv": ["echo", "x"]}
            ]})
            with self.assertRaises(ValueError):
                validate_manifest(path, root)

    def test_path_escape_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "bad", "argv": ["echo", "x"], "cwd": "../"}
            ]})
            with self.assertRaises(ValueError):
                validate_manifest(path, root)

    def test_dependency_cycle_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "a", "argv": ["echo", "a"], "depends_on": ["b"]},
                {"id": "b", "argv": ["echo", "b"], "depends_on": ["a"]}
            ]})
            with self.assertRaises(ValueError):
                validate_manifest(path, root)

    def test_sensitive_env_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "bad", "argv": ["echo", "x"], "env_allowlist": ["OPENAI_API_KEY"]}
            ]})
            with self.assertRaises(ValueError):
                validate_manifest(path, root)

    def test_unknown_dependency_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "a", "argv": ["echo", "a"], "depends_on": ["missing"]}
            ]})
            with self.assertRaises(ValueError):
                validate_manifest(path, root)

    def test_local_execution_persists_task_logs_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "first", "argv": ["@python", "-c", "print('first')"]},
                {"id": "second", "argv": ["@python", "-c", "print('second')"], "depends_on": ["first"]}
            ]})
            result = asyncio.run(execute_manifest(path, root, max_parallel=2))
            self.assertEqual([item["status"] for item in result["results"]], ["passed", "passed"])
            run_dir = root / ".orbit" / "runs" / result["run_id"]
            self.assertTrue((run_dir / "run-summary.json").is_file())
            self.assertIn("first", (run_dir / "first.log").read_text(encoding="utf-8"))
            self.assertIn("second", (run_dir / "second.log").read_text(encoding="utf-8"))

    def test_secret_environment_values_are_not_inherited_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "env-check", "argv": ["@python", "-c", "import os; print(os.environ.get('ORBIT_TEST_SECRET', ''))"]}
            ]})
            with patch.dict(os.environ, {"ORBIT_TEST_SECRET": "must-not-leak"}):
                result = asyncio.run(execute_manifest(path, root))
            log = Path(result["results"][0]["log_file"]).read_text(encoding="utf-8")
            self.assertEqual(result["results"][0]["status"], "passed")
            self.assertNotIn("must-not-leak", log)

    def test_workspace_write_requires_explicit_acknowledgement(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self._write(root, {"schema_version": 1, "tasks": [
                {"id": "write-test", "argv": ["@python", "-c", "print('should-not-run')"], "mode": "workspace-write"}
            ]})
            result = asyncio.run(execute_manifest(path, root, allow_workspace_write=False))
            self.assertEqual(result["results"][0]["status"], "approval-required")
            self.assertFalse((root / ".orbit" / "runs" / result["run_id"] / "write-test.log").exists())


if __name__ == "__main__":
    unittest.main()
