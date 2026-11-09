from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from orbit_cli.daemon import get_daemon_status, stop_daemon


class DaemonCliTests(unittest.TestCase):
    def test_daemon_status_when_stopped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            status = get_daemon_status(ws)
            self.assertEqual(status["status"], "stopped")
            self.assertFalse(status["running"])

    def test_daemon_status_stale_detection(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            orbit_dir = ws / ".orbit"
            orbit_dir.mkdir(parents=True)
            # Write a manifest with a non-existent PID
            (orbit_dir / "local-exec-daemon.json").write_text(
                json.dumps({"pid": 9999999, "port": 3888}), encoding="utf-8"
            )
            status = get_daemon_status(ws)
            self.assertEqual(status["status"], "stale")
            self.assertFalse(status["running"])

    def test_stop_daemon_when_not_running(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            result = stop_daemon(ws)
            self.assertEqual(result["status"], "not_running")


if __name__ == "__main__":
    unittest.main()
