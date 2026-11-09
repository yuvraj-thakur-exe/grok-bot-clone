# Project Charter

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

**Status:** Draft baseline · **Version:** 0.1.0

## Mission
Build an open-source, self-hostable AI agent platform that plans and executes digital work across research, browser, files, code and integrations while remaining observable, permissioned, recoverable and user-controlled.

## Problem
AI chat often produces answers but does not reliably complete multi-step work across tools. Agent frameworks expose primitives without a coherent product experience for persistence, approvals, secure execution, evidence, recoverability and operations.

## Product thesis
A user describes an outcome, inspects the plan, watches execution, approves risky actions, recovers interrupted tasks, inspects sources/artifacts and reuses a verified workflow. The execution infrastructure and trust model are the product.

## Objectives
1. Dependable AI workspace. 2. Multi-provider/local-model support. 3. Central policy enforcement for tools. 4. Isolated browser/code workers. 5. Durable tasks, checkpoints, artifacts and audit. 6. Evidence-backed research and file intelligence. 7. Controlled memory, skills, routines and specialist delegation. 8. Simple local installation and extensibility.

## Constraints
Small initial team; changing provider APIs/pricing; fragile browser automation; high cost of safe multi-tenant arbitrary code execution; open-source licensing and supply-chain obligations.

## Success definition
A bounded task completes end-to-end with a traceable plan, real tool execution, evidence/artifacts, recoverable status and no unauthorized side effect, confirmed by repeatable evaluations.

## ORBIT v0.2 alignment

The v0.2 product baseline adds optional native desktop access through a paired Local Desktop Node. It does not change ORBIT’s core mission or move desktop control into the first MVP. Keep product objectives focused on verified, safe task completion.
