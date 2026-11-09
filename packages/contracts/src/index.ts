// ORBIT core contracts v0 (docs/05-system-design/CORE_CONTRACTS.md). Pure schemas/types: no I/O, no repo imports.
import { createHash } from "node:crypto";
import { z } from "zod";

/* ---------- canonical JSON + hashing (stable across key order) ---------- */
export function canonicalJson(v: unknown): string {
  if (v === undefined) return "null";
  if (Array.isArray(v)) return `[${v.map(canonicalJson).join(",")}]`;
  if (v !== null && typeof v === "object") {
    const o = v as Record<string, unknown>;
    return `{${Object.keys(o)
      .filter((k) => o[k] !== undefined)
      .sort()
      .map((k) => `${JSON.stringify(k)}:${canonicalJson(o[k])}`)
      .join(",")}}`;
  }
  return JSON.stringify(v);
}
export const sha256 = (s: string): string => createHash("sha256").update(s).digest("hex");

/* ---------- Task Contract (FR-001) ---------- */
export const ExecutionModeSchema = z.enum(["suggest", "prepare", "execute", "scheduled"]);

export const BudgetSchema = z.object({
  maxCostUsd: z.number().positive().optional(),
  maxDurationSec: z.number().int().positive().default(1800),
  maxToolCalls: z.number().int().positive().default(200),
  maxTokens: z.number().int().positive().optional(),
});

export const AcceptanceCheckSchema = z.discriminatedUnion("kind", [
  z.object({
    kind: z.literal("command"),
    id: z.string().min(1),
    run: z.string().min(1),
    cwd: z.string().optional(),
    expectExit: z.number().int().default(0),
    timeoutSec: z.number().int().positive().default(300),
  }),
  z.object({ kind: z.literal("file_exists"), id: z.string().min(1), path: z.string().min(1) }),
  z.object({
    kind: z.literal("diff_limit"),
    id: z.string().min(1),
    maxFiles: z.number().int().positive().optional(),
    maxLines: z.number().int().positive().optional(),
    denyPaths: z.array(z.string()).default([]),
  }),
  z.object({ kind: z.literal("manual"), id: z.string().min(1), prompt: z.string().min(1) }),
]);

const DEFAULT_APPROVALS = ["external_message", "publish", "delete", "deploy", "payment"];

export const TaskContractSchema = z
  .object({
    version: z.literal(1),
    goal: z.string().min(1),
    scope: z.array(z.string()).default([]),
    nonGoals: z.array(z.string()).default([]),
    inputs: z.record(z.string(), z.unknown()).default({}),
    acceptance: z.array(AcceptanceCheckSchema).min(1),
    allowedTools: z.array(z.string()).default([]),
    mode: ExecutionModeSchema.default("execute"),
    budget: BudgetSchema.default({ maxDurationSec: 1800, maxToolCalls: 200 }),
    approvals: z.object({ require: z.array(z.string()).default(DEFAULT_APPROVALS) }).default({ require: DEFAULT_APPROVALS }),
    deadline: z.string().datetime().optional(),
    deliverables: z.array(z.string()).default([]),
  })
  .superRefine((c, ctx) => {
    const ids = c.acceptance.map((a) => a.id);
    if (new Set(ids).size !== ids.length) ctx.addIssue({ code: "custom", path: ["acceptance"], message: "acceptance check ids must be unique" });
  });
export type TaskContract = z.infer<typeof TaskContractSchema>;
export const hashContract = (c: TaskContract): string => sha256(canonicalJson(c));

/* ---------- Canonical events (FR-005, ADR-0008) ---------- */
export const EVENT_TYPES = [
  "agent.started", "agent.progress", "agent.completed",
  "task.started", "task.progress", "task.completed", "task.failed", "task.cancelled",
  "tool.started", "tool.completed", "tool.failed",
  "approval.requested", "approval.completed",
  "artifact.created", "message.delta", "run.checkpointed", "budget.warning", "handoff.requested",
] as const;
export const EventTypeSchema = z.enum(EVENT_TYPES);
export type EventType = z.infer<typeof EventTypeSchema>;
export const FailureReasonSchema = z.enum(["budget_exceeded", "policy_denied", "engine_unavailable", "verification_failed", "cancelled", "internal"]);

// Only the run controller (source "orbit") may emit these.
const ORBIT_ONLY = (t: string) => t.startsWith("task.") || t === "run.checkpointed" || t === "budget.warning";

export const EventEnvelopeSchema = z
  .object({
    schemaVersion: z.literal(1),
    id: z.string().min(1),
    seq: z.number().int().nonnegative(),
    runId: z.string().min(1),
    taskId: z.string().min(1),
    tenantId: z.string().min(1),
    traceId: z.string().min(1),
    ts: z.string().datetime(),
    type: EventTypeSchema,
    source: z.enum(["orbit", "engine"]),
    engine: z.string().optional(),
    payload: z.record(z.string(), z.unknown()),
  })
  .superRefine((e, ctx) => {
    if (ORBIT_ONLY(e.type) && e.source !== "orbit") ctx.addIssue({ code: "custom", path: ["source"], message: `${e.type} may only be emitted by orbit` });
  });
export type EventEnvelope = z.infer<typeof EventEnvelopeSchema>;

/* ---------- Receipt (FR-010) ---------- */
export const CheckResultSchema = z.object({
  id: z.string().min(1),
  status: z.enum(["pass", "fail", "skipped"]),
  evidenceRef: z.string().optional(),
});
export const ReceiptSchema = z
  .object({
    schemaVersion: z.literal(1),
    taskId: z.string().min(1),
    runId: z.string().min(1),
    contractSha256: z.string().regex(/^[0-9a-f]{64}$/),
    engine: z.object({ id: z.string().min(1), version: z.string().min(1) }),
    model: z.object({ providerId: z.string().optional(), modelId: z.string().optional() }),
    verdict: z.enum(["pass", "partial", "fail"]),
    verified: z.object({
      checks: z.array(CheckResultSchema),
      filesChanged: z.array(z.string()),
      toolCalls: z.object({ total: z.number().int().nonnegative(), byTool: z.record(z.string(), z.number().int().nonnegative()) }),
      approvals: z.array(z.object({ id: z.string(), action: z.string(), decision: z.string(), ruleId: z.string().nullable() })),
      errors: z.array(z.string()),
    }),
    modelSummary: z.string().optional(), // NOT evidence
    usage: z.object({ inputTokens: z.number().int().nonnegative(), outputTokens: z.number().int().nonnegative(), costUsd: z.number().nonnegative().optional() }),
    durationMs: z.number().int().nonnegative(),
    limitations: z.array(z.string()),
    createdAt: z.string().datetime(),
  })
  .superRefine((r, ctx) => {
    if (r.verdict === "pass" && r.verified.checks.some((c) => c.status !== "pass"))
      ctx.addIssue({ code: "custom", path: ["verdict"], message: "verdict 'pass' requires every check to pass (FR-009)" });
  });
export type Receipt = z.infer<typeof ReceiptSchema>;
export const receiptSha256 = (r: Receipt): string => sha256(canonicalJson(r));

/* ---------- Policy (FR-007, ADR-0009) ---------- */
export const PolicyEffectSchema = z.enum(["allow", "ask", "deny"]);
export const PolicyRuleSchema = z.object({
  id: z.string().min(1),
  effect: PolicyEffectSchema,
  action: z.string().min(1),
  resource: z.string().default("*"),
  reason: z.string().optional(),
});
export const HardDenyRuleSchema = z.object({ id: z.string().min(1), action: z.string().min(1), resource: z.string().min(1), reason: z.string().optional() });
export const PolicyDocumentSchema = z
  .object({
    version: z.literal(1),
    semantics: z.string().optional(),
    defaultEffect: PolicyEffectSchema,
    hardDeny: z.array(HardDenyRuleSchema),
    rules: z.array(PolicyRuleSchema),
  })
  .superRefine((p, ctx) => {
    const ids = [...p.hardDeny.map((r) => r.id), ...p.rules.map((r) => r.id)];
    if (new Set(ids).size !== ids.length) ctx.addIssue({ code: "custom", message: "policy rule ids must be unique" });
    const first = p.rules[0];
    // Fail-closed (SEC-002): last-match-wins means the catch-all must come FIRST and must not allow.
    if (!first || first.action !== "*" || first.resource !== "*" || first.effect === "allow")
      ctx.addIssue({ code: "custom", path: ["rules", 0], message: "first rule must be a catch-all '*'/'*' with effect ask or deny" });
    if (p.defaultEffect === "allow") ctx.addIssue({ code: "custom", path: ["defaultEffect"], message: "defaultEffect must not be allow" });
  });
export type PolicyDocument = z.infer<typeof PolicyDocumentSchema>;
export const PolicyRequestSchema = z.object({
  tenantId: z.string().min(1),
  runId: z.string().min(1),
  action: z.string().min(1),
  resources: z.array(z.string()),
  source: z.enum(["engine", "mcp", "orbit"]),
  meta: z.record(z.string(), z.unknown()).optional(),
});
export type PolicyRequest = z.infer<typeof PolicyRequestSchema>;
export const PolicyDecisionSchema = z.object({ effect: PolicyEffectSchema, ruleId: z.string().nullable(), reason: z.string() });
export type PolicyDecision = z.infer<typeof PolicyDecisionSchema>;

/* ---------- EngineAdapter (FR-003) — types only ---------- */
export interface EngineCapabilities { streaming: boolean; interrupt: boolean; resume: boolean; permissions: boolean; usage: boolean }
export interface EngineConfig { binPath?: string; pinVersion: string; workspacePath: string; runDir: string; model?: string; env?: Record<string, string> }
export interface SessionInput { runId: string; taskId: string; model?: string; agent?: string; metadata?: Record<string, string> }
export interface EngineSession { id: string; engineSessionId: string }
export interface EngineTask { idempotencyKey: string; prompt: string }
export interface Checkpoint { engineSessionId: string; lastDurableSeq: number; workspaceHead?: string }
export interface ArtifactRef { kind: "diff" | "file" | "log" | "report"; uri: string; sha256?: string }
export type EngineEvent = { type: EventType; payload: Record<string, unknown>; engineType?: string; durableSeq?: number };
export interface EngineAdapter {
  readonly id: string;
  capabilities(): EngineCapabilities;
  initialize(cfg: EngineConfig): Promise<{ version: string }>;
  createSession(input: SessionInput): Promise<EngineSession>;
  executeTask(session: EngineSession, task: EngineTask): Promise<void>;
  streamEvents(session: EngineSession, opts?: { afterSeq?: number }): AsyncIterable<EngineEvent>;
  interrupt(session: EngineSession): Promise<void>;
  resume(session: EngineSession, from: Checkpoint): Promise<void>;
  collectArtifacts(session: EngineSession): Promise<ArtifactRef[]>;
  closeSession(session: EngineSession): Promise<void>;
  healthCheck(): Promise<{ ok: boolean; version?: string }>;
}
