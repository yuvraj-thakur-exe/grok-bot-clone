# ORBIT v1.1 upstream pin audit

**Observed:** 2026-11-08 UTC. **Purpose:** reproducible source-intake candidates, not an adoption decision.

The six repositories below were checked through GitHub repository metadata, the `main` branch commit endpoint and the raw root `LICENSE` file. The recorded SHA is the exact observed `main` head at retrieval time. Commit pins are immutable identifiers; the branch name is informational only.

| ID | Repository | Observed commit | Root `LICENSE` | Intended role |
|---|---|---|---|---|
| `openmausbot` | [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot) | `bcad12dfbf4da4cdb19af162caaf64666af6235f` | Apache-2.0 | Product shell and approval-flow reference |
| `openhands-sdk` | [OpenHands/software-agent-sdk](https://github.com/OpenHands/software-agent-sdk) | `51ad22388a154d48353fac7a82cfd5255dbeefc1` | MIT | Disposable coding-worker SDK evaluation |
| `playwright` | [microsoft/playwright](https://github.com/microsoft/playwright) | `07c7069cdbb1f5c7331d3f4d2abd864dcfde745a` | Apache-2.0 | Baseline browser-driver reference |
| `opensandbox` | [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) | `a8d44ecf7338cb810565b299a0ec2d407f36007f` | Apache-2.0 | Sandbox-provider evaluation |
| `openclaw` | [openclaw/openclaw](https://github.com/openclaw/openclaw) | `f4976c968539eda937ce3ffdaaa5146c55bcb1bd` | MIT | Optional gateway/plugin architecture reference |
| `agent-desktop` | [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop) | `b43ac4f6e892ef608f8851428613c4009f0e84c7` | Apache-2.0 | Native desktop accessibility-driver reference |

## Important limits

- Only each repository's root `LICENSE` was checked in this pass. This is not a full legal or file-level license review.
- The nested packages, generated artifacts, bundled dependencies, model weights, datasets, assets and skills may carry different terms.
- Root `NOTICE`, nested `LICENSE` files, copyright headers, dependency licenses, patents, trademarks and model/data terms must be checked before copying or redistribution.
- The OpenMausBot map intentionally excludes `enterprise/`; do not copy its product identity, logo, mascot, illustrations or trade dress.
- OpenClaw in-process native plugins are trusted code and are not an isolation boundary.
- No repository has been cloned, installed, executed, imported or merged into the ORBIT application by this audit.

## Clone discipline

Use `configs/upstream-candidates.lock.json` as a review shortlist. Clone only the repository needed for the current feature, pin by SHA, and use the recorded sparse paths. Inspect the exact commit's README, package manifests, lockfiles, nearest tests, security policy, root and nested notices before installing anything. Record path hashes and dependency closure before source adoption.

After cloning, confirm the checkout's `git rev-parse HEAD` equals the configured SHA. If it does not, reject the checkout rather than silently using a moving branch head.
