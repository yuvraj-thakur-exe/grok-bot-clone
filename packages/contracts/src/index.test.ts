import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import {
  EVENT_TYPES, EventEnvelopeSchema, PolicyDocumentSchema, ReceiptSchema, TaskContractSchema,
  canonicalJson, hashContract, receiptSha256,
} from "./index";

const read = (rel: string) => readFileSync(new URL(rel, import.meta.url), "utf8");
const contract = { version: 1, goal: "add sum()", acceptance: [{ kind: "command", id: "tests", run: "npm test" }] };
const receipt = {
  schemaVersion: 1, taskId: "tsk_1", runId: "run_1", contractSha256: "a".repeat(64),
  engine: { id: "opencode", version: "2.2.5" }, model: {}, verdict: "pass",
  verified: { checks: [{ id: "tests", status: "pass" }], filesChanged: ["a.ts"], toolCalls: { total: 1, byTool: { shell: 1 } }, approvals: [], errors: [] },
  usage: { inputTokens: 1, outputTokens: 1 }, durationMs: 5, limitations: [], createdAt: "2026-11-02T00:00:00.000Z",
};

describe("TaskContract (FR-001)", () => {
  it("applies safe defaults", () => {
    const c = TaskContractSchema.parse(contract);
    expect(c.mode).toBe("execute");
    expect(c.budget).toEqual({ maxDurationSec: 1800, maxToolCalls: 200 });
    expect(c.approvals.require).toContain("deploy");
  });
  it("rejects missing or duplicate acceptance checks", () => {
    expect(TaskContractSchema.safeParse({ ...contract, acceptance: [] }).success).toBe(false);
    const dup = { ...contract, acceptance: [contract.acceptance[0], contract.acceptance[0]] };
    expect(TaskContractSchema.safeParse(dup).success).toBe(false);
  });
  it("hash is stable across key order and changes with content", () => {
    const a = TaskContractSchema.parse(contract);
    const b = TaskContractSchema.parse(JSON.parse(JSON.stringify({ acceptance: contract.acceptance, goal: contract.goal, version: 1 })));
    expect(hashContract(a)).toBe(hashContract(b));
    expect(hashContract({ ...a, goal: "other" })).not.toBe(hashContract(a));
    expect(canonicalJson({ b: 1, a: undefined, c: [2, { z: 1, y: 2 }] })).toBe('{"b":1,"c":[2,{"y":2,"z":1}]}');
  });
});

describe("events (FR-005)", () => {
  it("every canonical type is documented in CORE_CONTRACTS.md", () => {
    const doc = read("../../../docs/05-system-design/CORE_CONTRACTS.md");
    for (const t of EVENT_TYPES) expect(doc, t).toContain(`\`${t}\``);
  });
  it("task.* events may only come from orbit", () => {
    const base = { schemaVersion: 1, id: "e1", seq: 0, runId: "r", taskId: "t", tenantId: "ten", traceId: "x", ts: "2026-11-02T00:00:00.000Z", payload: {} };
    expect(EventEnvelopeSchema.safeParse({ ...base, type: "task.completed", source: "engine" }).success).toBe(false);
    expect(EventEnvelopeSchema.safeParse({ ...base, type: "task.completed", source: "orbit" }).success).toBe(true);
    expect(EventEnvelopeSchema.safeParse({ ...base, type: "tool.started", source: "engine", engine: "opencode" }).success).toBe(true);
  });
});

describe("receipt (FR-010, FR-009)", () => {
  it("valid receipt parses and hash changes when a field changes", () => {
    const r = ReceiptSchema.parse(receipt);
    expect(receiptSha256(r)).toMatch(/^[0-9a-f]{64}$/);
    expect(receiptSha256({ ...r, durationMs: 6 })).not.toBe(receiptSha256(r));
  });
  it("verdict pass is impossible with a failing check", () => {
    const bad = { ...receipt, verified: { ...receipt.verified, checks: [{ id: "tests", status: "fail" }] } };
    expect(ReceiptSchema.safeParse(bad).success).toBe(false);
  });
});

describe("policy (FR-007, SEC-002)", () => {
  it("config/policy.default.json is valid and fail-closed", () => {
    const p = PolicyDocumentSchema.parse(JSON.parse(read("../../../config/policy.default.json")));
    expect(p.defaultEffect).toBe("ask");
    expect(p.hardDeny.map((r) => r.id)).toContain("hd-sudo");
  });
  it("rejects a policy whose first rule is not a non-allow catch-all", () => {
    const p = JSON.parse(read("../../../config/policy.default.json"));
    expect(PolicyDocumentSchema.safeParse({ ...p, rules: p.rules.slice(1) }).success).toBe(false);
    expect(PolicyDocumentSchema.safeParse({ ...p, defaultEffect: "allow" }).success).toBe(false);
  });
});
