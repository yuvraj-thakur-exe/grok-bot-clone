# ORBIT dedicated 500 GB development volume

All values use decimal GB (1 GB = 1,000,000,000 bytes), which is the unit commonly used by storage manufacturers. A 500 GB drive may appear as approximately 466 GiB in binary-unit displays. Confirm actual mounted capacity before provisioning.

| Folder | Soft target GB |
|---|---:|
| `00-control` | 10 |
| `01-upstream-checkouts` | 100 |
| `02-workspaces` | 100 |
| `03-models` | 90 |
| `04-data-memory` | 35 |
| `05-artifacts` | 25 |
| `06-evaluations` | 20 |
| `07-logs-cache` | 5 |
| `08-backups` | 25 |
| `09-quarantine` | 10 |
| `10-source-intake` | 20 |
| **Allocated soft targets** | **440** |
| **Free reserve** | **60** |
| **Total** | **500** |

## Guardrails

- At 80% used: alert and inspect caches/worktrees/artifacts.
- At 90% used: block model downloads and large builds pending review.
- At 95% used: stop nonessential writes. Do not auto-delete user data, memories, backups or source intake.
- Keep at least one critical backup on a separate physical or approved remote volume; same-drive copies do not protect against disk failure.
- Do not clone all candidate upstreams or download multiple large models by default.
- 500 GB storage does not increase RAM or GPU VRAM and does not make large models runnable on a laptop.
- Quarantine is non-executable. Review and promote content into a clean worktree only after source, license and security checks.

The CLI's allocation targets are advisory; it does not enforce quotas. User data encryption, backup policy and access controls require a separately reviewed deployment configuration.
