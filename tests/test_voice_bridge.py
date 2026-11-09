from __future__ import annotations

import tempfile
import unittest
import wave
from pathlib import Path

from antigravity_platform.runtime_bridge.voice_bridge import (
    OmniVoiceBridge,
    VOICE_PROFILES,
    generate_mock_wav,
)


class VoiceBridgeTests(unittest.TestCase):
    def test_mock_wav_generation_is_valid_pcm(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            wav_path = Path(tmp) / "test.wav"
            generate_mock_wav(wav_path, duration_s=0.5, sample_rate=16000)
            self.assertTrue(wav_path.exists())

            with wave.open(str(wav_path), "rb") as w:
                self.assertEqual(w.getnchannels(), 1)
                self.assertEqual(w.getframerate(), 16000)
                self.assertEqual(w.getsampwidth(), 2)
                self.assertEqual(w.getnframes(), 8000)

    def test_voice_bridge_synthesize_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            ws = Path(tmp)
            bridge = OmniVoiceBridge(workspace_root=ws)

            out_wav = ws / "speech.wav"
            res = bridge.synthesize("Hello world", role_id="cto", output_path=out_wav)
            self.assertTrue(res.success)
            self.assertEqual(res.role_id, "cto")
            self.assertTrue(Path(res.output_path).exists())

    def test_role_profile_selection(self) -> None:
        bridge = OmniVoiceBridge()
        cto_profile = bridge.get_role_profile("executive.cto_principal_architect")
        self.assertEqual(cto_profile["gender"], "male")
        self.assertIn("authoritative", cto_profile["instruct"])

        qa_profile = bridge.get_role_profile("quality.qa_agent_evaluation_engineer")
        self.assertEqual(qa_profile["gender"], "female")
        self.assertIn("analytical", qa_profile["instruct"])


if __name__ == "__main__":
    unittest.main()
