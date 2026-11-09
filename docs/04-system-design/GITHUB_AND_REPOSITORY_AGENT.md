# GitHub and repository agent design

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

## User journey

1. User explicitly selects a repository or authorizes an organization/repository through an OAuth/GitHub App flow.
2. ORBIT displays repository, branch and requested permission scope.
3. Code worker creates a disposable workspace/worktree snapshot.
4. Agent maps architecture, reads project instructions and runs safe baseline checks.
5. It creates a plan tied to issue/requirements and modifies scoped files.
6. Worker runs tests in sandbox, captures logs and produces a diff.
7. Verification stage checks tests, secret scan, changed files and scope.
8. User reviews diff; ORBIT may create a branch/PR draft only with authorized scope and explicit approval where required.

## Authentication

Prefer GitHub App installation tokens for organization integrations; use fine-grained personal access tokens only for individual/dev flows when necessary. Request the minimum repository and operation permissions. GitHub documents endpoint-specific fine-grained token permissions; do not assume one generic scope unlocks every operation. Store tokens in the connector secret broker and issue short-lived access to the worker.

## Clone behavior

Public repositories may be cloned read-only without credentials when permitted. Private repositories require explicit authorization. Never infer permission from a URL or access to a local parent folder. Do not embed credentials in clone URLs or process command lines. Use credential helpers or ephemeral headers/askpass channels in isolated workers and scrub them after use.

## Branch and file safety

- Never work directly on the user's default branch unless explicitly requested and approved.
- Prefer a new branch/worktree per task.
- Do not overwrite uncommitted user changes; inspect status and stop if workspace state is ambiguous.
- Restrict path writes to the checked-out repository root; defend against symlink traversal.
- Never execute project scripts before inspecting them and choosing a sandbox profile.
- Compare the final diff against the planned file scope and detect accidental large deletions.

## Pull requests

PR creation, pushes and issue comments are externally visible writes. Require explicit permission and approval bound to the repository, branch, title/body and intended side effect. The final report includes commit SHA, branch, diff summary, checks run and known issues.

## Desktop capability boundary for coding agents

A repository coding agent should use the isolated code worker for clone/edit/test/Git tasks. Native desktop control is unnecessary for most code operations and must not be used as a shortcut to reach a host IDE, SSH agent, credentials or private files. A developer may explicitly use desktop UI for an IDE workflow, but only through a paired node, scoped task lease and exact action policy. GitHub API permissions remain separately scoped and must not be inherited by desktop control.

## ORBIT v0.2 alignment

The v0.2 system contract adds desktop device, session, capability, lease, action and observation metadata. All operations are typed and policy checked; see `DESKTOP_CONTROL_API_AND_DATA_CONTRACT.md`.
