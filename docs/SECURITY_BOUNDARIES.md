# ORBIT developer-toolkit security boundaries

## Current local helper safeguards

- Process commands use `create_subprocess_exec` with an argument vector and no shell interpolation.
- Working directories must resolve inside the selected workspace.
- Manifest size, task count, argument count, argument length, timeout, output and parallelism are bounded.
- Task dependency cycles and unknown IDs are rejected before execution.
- Sensitive environment variables cannot be passed through the explicit environment allowlist.
- Child tasks receive a minimal OS environment rather than every inherited variable.
- Workspace-write tasks require a deliberate command-line acknowledgement.
- External side-effect task mode is blocked.
- Context packer skips common credential paths, environment files, key material, symlinks, binary data and build/cache trees; basic secret-pattern redaction is best effort.

## Not a hostile-code sandbox

This toolkit does not isolate a child process from the user's OS account. A malicious Python, Node, Git hook, package lifecycle script or native executable may still access files and network resources available to that user. Do not run untrusted repositories, downloaded skills or model-generated arbitrary commands through this runner.

Production code execution must move to a hardened `SandboxProvider` (disposable container/microVM with no Docker socket, scoped mounts, network-deny default, resource quotas and secret brokering). Desktop control must use a paired Local Desktop Node in a logged-in interactive session. Browser control must use isolated Playwright contexts.

## Approval requirements in the product

External messages, purchases, deletion, public publication, credential changes, privileged account actions, legal acceptance and production deployments require explicit human approval bound to the exact target and arguments. The model is never the policy authority.
