from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from orbit_cli.storage import DEFAULT_LAYOUT, init_storage, storage_status


class StorageTests(unittest.TestCase):
    def test_layout_targets_total_440_gb_and_creates_directories(self) -> None:
        self.assertEqual(sum(DEFAULT_LAYOUT.values()), 440)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "ORBIT-Storage"
            result = init_storage(root, expected_capacity_gb=2, reserve_gb=1)
            self.assertTrue(Path(result["manifest"]).is_file())
            for dirname in DEFAULT_LAYOUT:
                self.assertTrue((root / dirname).is_dir())
            self.assertEqual(set(result["created_directories"]), set(DEFAULT_LAYOUT))
            second = init_storage(root, expected_capacity_gb=2, reserve_gb=1)
            self.assertEqual(second["created_directories"], [])
            status = storage_status(root)
            self.assertIn(status["status"], {"NORMAL", "WARNING", "BLOCK_BULK_WRITES", "CRITICAL", "RESERVE_BREACHED"})
            self.assertGreaterEqual(status["total_gb_decimal"], 0)

    def test_invalid_reserve_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "ORBIT-Storage"
            init_storage(root, expected_capacity_gb=2, reserve_gb=1)
            with self.assertRaises(ValueError):
                storage_status(root, reserve_gb=0)

    def test_relative_path_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                init_storage("relative/orbit", expected_capacity_gb=500, reserve_gb=60)

    def test_existing_manifest_not_overwritten_for_different_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "ORBIT-Storage"
            init_storage(root, expected_capacity_gb=2, reserve_gb=1)
            manifest = root / "orbit-storage.json"
            stored = json.loads(manifest.read_text(encoding="utf-8"))
            stored["root"] = str(root / "different")
            manifest.write_text(json.dumps(stored, indent=2), encoding="utf-8")
            with self.assertRaises(ValueError):
                init_storage(root, expected_capacity_gb=2, reserve_gb=1)


if __name__ == "__main__":
    unittest.main()
