#!/usr/bin/env python3
"""ORBIT Team Configuration Generator.

Translates ORBIT's 30-role AI workforce registry (roles/ROLE_REGISTRY.yaml)
and charter markdown files into OpenGrokBot's team.json configuration format.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

# Department colors & shapes for visual distinction in OpenGrokBot UI
DEPARTMENT_THEMES = {
    "executive": {"color": "#4f46e5", "shape": "hex", "label": "Executive"},
    "engineering": {"color": "#0ea5e9", "shape": "round", "label": "Engineering"},
    "ai": {"color": "#8b5cf6", "shape": "blob", "label": "AI & ML"},
    "quality": {"color": "#10b981", "shape": "diamond", "label": "Quality & Sec"},
    "business": {"color": "#f59e0b", "shape": "round", "label": "Business"},
    "design": {"color": "#ec4899", "shape": "drop", "label": "Design"},
}

SHORT_NAME_OVERRIDES = {
    "executive.founder-ceo-human": "FOUNDER",
    "executive.cto-principal-architect": "CTO",
    "executive.cpo-product-lead": "PRODUCT",
    "executive.coo-delivery-lead": "DELIVERY",
    "ai.chief-ai-research-officer": "AI_RESEARCH",
    "ai.ai-ml-engineer": "ML_ENG",
    "ai.agent-runtime-engineer": "AGENT_ENG",
    "ai.data-rag-engineer": "RAG_ENG",
    "ai.model-runtime-engineer": "MODEL_ENG",
    "engineering.backend-engineer": "BACKEND",
    "engineering.frontend-engineer": "FRONTEND",
    "engineering.browser-automation-engineer": "BROWSER",
    "engineering.desktop-computer-use-engineer": "DESKTOP",
    "engineering.sandbox-runtime-engineer": "SANDBOX",
    "engineering.repository-operations-engineer": "REPO_OPS",
    "engineering.voice-multimodal-engineer": "VOICE",
    "engineering.integration-connector-engineer": "INTEGRATION",
    "engineering.home-device-integration-engineer": "IOT",
    "engineering.mobile-companion-engineer": "MOBILE",
    "quality.security-privacy-lead": "SECURITY",
    "quality.qa-agent-evaluation-engineer": "QA",
    "quality.devops-sre-engineer": "SRE",
    "quality.data-governance-engineer": "GOVERNANCE",
    "quality.benchmark-performance-engineer": "BENCHMARK",
    "business.opensource-community-lead": "COMMUNITY",
    "business.finance-commercial-analyst": "FINANCE",
    "business.legal-ip-compliance-analyst": "LEGAL",
    "business.customer-success-researcher": "RESEARCHER",
    "design.ux-product-designer": "DESIGN",
    "design.technical-writer": "DOCS",
}


def parse_charter(charter_path: Path) -> Dict[str, str]:
    """Extract mission, scope, and personality essence from a markdown charter."""
    if not charter_path.exists():
        return {"scope": "", "personality": ""}

    text = charter_path.read_text(encoding="utf-8", errors="replace")

    mission_match = re.search(r"## Mission\s*\n+([^\n#]+)", text)
    mission = mission_match.group(1).strip() if mission_match else ""

    scope_match = re.search(r"## Scope and responsibilities\s*\n+([^\n#]+)", text)
    scope = scope_match.group(1).strip() if scope_match else mission

    prohibited_match = re.search(r"## Prohibited actions and guardrails\s*\n+([^\n#]+)", text)
    prohibited = prohibited_match.group(1).strip() if prohibited_match else ""

    return {
        "mission": mission,
        "scope": scope,
        "prohibited": prohibited,
    }


def build_personality(title: str, mission: str, scope: str, prohibited: str) -> str:
    """Build a sharp, concise persona prompt adhering to Ponytail guidelines."""
    prompt = (
        f"You are the {title} in ORBIT / Grok Bot Clone. "
        f"Your mission: {mission}. "
        f"Scope: {scope}. "
    )
    if prohibited:
        prompt += f"Guardrails: {prohibited} "
    prompt += "Be direct, concise, and prioritize verifiable code and receipts over speculation."
    return prompt


def generate_team_config() -> Dict[str, Any]:
    registry_path = WORKSPACE_ROOT / "roles" / "ROLE_REGISTRY.yaml"
    with open(registry_path, "r", encoding="utf-8") as f:
        registry = yaml.safe_load(f)

    roles_data = registry.get("roles", [])

    agents: List[Dict[str, Any]] = []

    for r in roles_data:
        role_id = r["id"]
        # Skip human owner in AI agent list
        if r.get("type") == "human_owner":
            continue

        parts = role_id.split(".")
        dept_key = parts[0] if len(parts) > 1 else "engineering"
        dept_theme = DEPARTMENT_THEMES.get(dept_key, DEPARTMENT_THEMES["engineering"])

        charter_rel = r.get("charter_path", "")
        charter_full = WORKSPACE_ROOT / charter_rel if charter_rel else None
        charter_info = parse_charter(charter_full) if charter_full else {}

        mission = r.get("mission") or charter_info.get("mission", "")
        scope = charter_info.get("scope") or mission
        prohibited = charter_info.get("prohibited", "")

        short_name = SHORT_NAME_OVERRIDES.get(role_id, parts[-1].upper().replace("-", "_"))
        title = r.get("title", short_name)

        personality = build_personality(title, mission, scope, prohibited)

        # Tool allocation based on department
        if dept_key in ("engineering", "ai"):
            tools = ["Read", "Edit", "Write", "Glob", "Grep", "Bash", "WebSearch"]
        elif dept_key == "quality":
            tools = ["Read", "Glob", "Grep", "Bash", "WebSearch"]
        else:
            tools = ["Read", "Glob", "Grep", "WebSearch"]

        # Default model selection
        agent_obj: Dict[str, Any] = {
            "id": role_id.replace(".", "_").replace("-", "_"),
            "name": short_name,
            "role": title,
            "department": dept_theme["label"],
            "scope": scope[:140],
            "color": dept_theme["color"],
            "shape": dept_theme["shape"],
            "provider": "openai",
            "model": "default",
            "effort": "high" if dept_key in ("executive", "quality") else "medium",
            "personality": personality,
            "tools": tools,
            "permissionMode": "dontAsk",
            "mcpServers": [],
            "inheritClaudeSettings": False,
            "autoApproveTools": False,
            "muted": False,
            "approvals": "ask-dangerous" if dept_key == "quality" else "auto",
        }
        agents.append(agent_obj)

    # Standard skill list
    skills = {
        "standup": {
            "name": "Daily Standup",
            "description": "Report current blockers, recent achievements, and next priorities.",
            "body": "Give a 3-bullet standup: 1) What was finished today, 2) Current blocker, 3) Next immediate task.",
        },
        "qa-checklist": {
            "name": "QA Verification Checklist",
            "description": "Run unit tests and verification gates before approving changes.",
            "body": "Run all tests with receipts, verify boundary safety, and check license compliance.",
        },
        "desktop-control": {
            "name": "Desktop Computer Control",
            "description": "Execute bounded GUI actions via desktop computer use harness.",
            "body": "Inspect active window, verify workspace boundaries, and perform requested desktop operation.",
        },
        "rea-audit": {
            "name": "Reverse-Engineering Audit",
            "description": "Inspect binary or extracted application bundle using REA.",
            "body": "Analyze IPC handlers, manifest schemas, and extract verification receipts.",
        },
    }

    team_config = {
        "company": "ORBIT / Grok Bot Clone",
        "owner": {
            "id": "user",
            "name": "Yuvraj",
            "title": "Founder / CEO",
        },
        "workspace": ".",
        "agents": agents,
        "mcpServers": {
            "rea": {
                "type": "stdio",
                "command": "python",
                "args": ["-m", "rea.server"],
            }
        },
        "settings": {
            "maxTurnsPerReply": 8,
            "streamResponses": True,
            "approvalMode": "ask-dangerous",
        },
        "providers": {
            "openai": {
                "kind": "openai",
                "label": "OpenAI / OpenRouter / Ollama / Grok",
                "baseUrl": "https://api.openai.com/v1",
                "models": ["gpt-4o", "gpt-4o-mini", "o3-mini", "grok-beta"],
            },
            "gemini": {
                "kind": "gemini",
                "label": "Google Gemini (Antigravity)",
                "models": ["gemini-2.5-pro", "gemini-2.5-flash"],
            },
            "claude": {
                "kind": "claude",
                "label": "Anthropic Claude",
                "models": ["claude-3-7-sonnet", "claude-3-5-haiku", "claude-opus-5"],
            },
        },
        "skills": skills,
    }

    return team_config


def main() -> None:
    team_data = generate_team_config()

    # Save to config/team.orbit.json
    out_dir = WORKSPACE_ROOT / "config"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "team.orbit.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(team_data, f, indent=2)
    print(f"Generated ORBIT team config with {len(team_data['agents'])} agents at {out_path}")

    # Also update upstream/opengrokbot/team.json if present
    upstream_team_path = WORKSPACE_ROOT / "upstream" / "opengrokbot" / "team.json"
    with open(upstream_team_path, "w", encoding="utf-8") as f:
        json.dump(team_data, f, indent=2)
    print(f"Updated upstream OpenGrokBot team config at {upstream_team_path}")


if __name__ == "__main__":
    main()
