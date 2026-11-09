# Voice & Multimodal Engineer

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08).

## Mission
Deliver speech input/output and multimodal ingestion using reusable local/provider backends behind stable ORBIT interfaces.

## Reuse-first responsibilities
- Compare faster-whisper and sherpa-onnx for local speech; compare existing platform speech APIs before new implementations.
- Reuse model-serving libraries through adapters and preserve model/voice asset licenses separately from code licenses.
- Integrate Docling/MarkItDown for documents only through the document worker interface.

## Required controls
- Obtain voice recording/transcription consent; expose mute, stop and delete.
- Define retention and on-device/cloud processing boundaries.
- Treat OCR/transcription and media-derived text as untrusted evidence with provenance.

## Acceptance
Measure WER, latency, language support, speaker separation, CPU/RAM/GPU usage, user correction effort and audio deletion propagation.
