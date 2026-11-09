# Assumptions and Constraints

> **Document baseline:** ORBIT 1.0.0-draft (2026-11-08). Earlier version labels are historical unless explicitly marked current.

| ID | Assumption / constraint | Status / validation |
|---|---|---|
| ASM-001 | Small team/open-source start | Assumed; confirm maintainer capacity |
| ASM-002 | Hosted APIs optional; local endpoint support | Requirement; test compatible local model |
| ASM-003 | Browser/code jobs never run in API process | Architectural rule |
| ASM-004 | PostgreSQL authoritative | Proposed; validate deployment needs |
| ASM-005 | Redis non-authoritative | Must prove task durability without Redis |
| ASM-006 | Temporal preferred for durable workflows | Prototype retries, timers and approval waits |
| ASM-007 | Private repos and accounts may be connected | Define OAuth scope and vault design |
| ASM-008 | Competitor private flows not verified | Public docs only unless authorized account supplied |
| ASM-009 | Docker alone may not isolate hostile multi-tenant code | Evaluate gVisor/Firecracker/Kata before public code execution |
| ASM-010 | Search HTML/availability may change | Adapters, rate limits and fallback |
| ASM-011 | MCP protocol has breaking/versioned changes | Pin and contract-test supported versions |
| ASM-012 | Tor not an MVP dependency | Separate optional lawful-use track only |

## ORBIT v0.2 alignment

The v0.2 product baseline adds optional native desktop access through a paired Local Desktop Node. It does not change ORBIT’s core mission or move desktop control into the first MVP. Keep product objectives focused on verified, safe task completion.
