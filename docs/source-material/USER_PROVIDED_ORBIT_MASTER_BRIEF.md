You should build something bigger than a basic Grok chatbot. Build an open-source AI agent platform that can research, browse websites, operate a computer, write code, manage files, coordinate specialist agents, learn workflows, and execute tasks autonomously.

The important distinction: Grok Bot is not merely a chat interface. Its documented capabilities include persistent cloud computers, browser and terminal access, multiple cooperating Bots, persistent context, learned skills, and scheduled routines. Grok also supports web search, X Search, code execution, image generation, file collections, and custom tools.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.x.ai\&sz=32)

SpaceXSI Docs+2



My recommendation is to compete through execution quality, openness, privacy, speed, flexibility, and reliability, rather than pretending an open-source wrapper around an API is a new foundation model.

# Master engineering prompt



Ready to use

For Codex / Antigravity / Claude Code



Copy the complete prompt below into your coding agent.

# PROJECT: ORBIT AI

## Build an Open-Source AI Agent Platform That Can Compete With Grok Bot

### YOUR ROLE

Act as a world-class AI systems architect, senior full-stack engineer, AI researcher, reverse engineer, browser automation engineer, security engineer, DevOps engineer, product designer, and experienced open-source maintainer.

You have extensive experience building:

- AI assistants and agentic systems.
- Multi-agent orchestration frameworks.
- Browser automation and computer-use agents.
- LLM inference and model-routing systems.
- Persistent memory and retrieval systems.
- Cloud execution environments.
- Developer tools and open-source infrastructure.
- Production-grade SaaS platforms.

Think like the engineering team responsible for building a serious competitor to Grok Bot.

Do not produce a superficial chatbot, UI mockup, or collection of disconnected features.

Build a functional, modular, secure, extensible, production-oriented open-source AI agent platform.

**Your mission is to research the original product, understand its workflows, identify its limitations, design a better architecture, and implement a genuinely useful competing product.**

---

# PART 1. COMPETITOR RESEARCH AND REVERSE ENGINEERING

Before writing code, investigate the existing product.

Target:

- [https://grok.com/](https://grok.com/)
- [https://docs.x.ai/grok/overview](https://docs.x.ai/grok/overview)
- [https://docs.x.ai/grok-bot/overview](https://docs.x.ai/grok-bot/overview)
- [https://docs.x.ai/developers/](https://docs.x.ai/developers/)
- [https://docs.x.ai/grok-bot/bots](https://docs.x.ai/grok-bot/bots)
- [https://docs.x.ai/grok-bot/computer-and-apps](https://docs.x.ai/grok-bot/computer-and-apps)
- [https://docs.x.ai/grok-bot/skills-routines-and-automations](https://docs.x.ai/grok-bot/skills-routines-and-automations)
- [https://docs.x.ai/grok-bot/approvals-security-and-privacy](https://docs.x.ai/grok-bot/approvals-security-and-privacy)

### A. Browser-based product investigation

Use the available browser and browser automation tools.

Visit the official websites and investigate their publicly observable functionality.

Inspect:

1. Landing page and navigation.
2. Authentication and onboarding screens, where publicly accessible.
3. Chat interface.
4. Message composer and attachment handling.
5. Model selection and reasoning controls.
6. Web research functionality.
7. File uploads and document analysis.
8. Voice interaction.
9. Image and video capabilities.
10. Bot creation and management.
11. Bot memory and persistent context.
12. Browser and computer interaction.
13. Terminal and filesystem workflows.
14. Connected applications.
15. Multi-agent coordination.
16. Skills and reusable workflows.
17. Scheduling and automation.
18. User approvals and permissions.
19. Settings, usage, and subscription controls.

Do not assume a feature exists merely because another AI product has it.

### B. Inspect the real interface

For each publicly available workflow:

- Capture screenshots.
- Record the visible interaction sequence.
- Identify navigation patterns.
- Inspect loading states.
- Observe streaming behavior.
- Identify empty states and failure states.
- Record responsive behavior.
- Inspect accessibility and keyboard navigation.
- Record useful browser console errors when accessible.
- Inspect public network behavior only where legally and technically permitted.

Use browser developer tools, Playwright, screenshots, accessibility snapshots, and public documentation where available.

When access requires authentication, use only an account and access explicitly provided by the user. Never bypass authentication, CAPTCHAs, subscription restrictions, or access controls.

Do not steal credentials, extract private data, or reproduce proprietary source code.

### C. Reverse-engineering research report

Create:

`docs/research/GROK_COMPETITOR_ANALYSIS.md`

Include:

| Category       | What to investigate                      |
| -------------- | ---------------------------------------- |
| User interface | Layout, navigation, usability            |
| Conversation   | Streaming, message handling, context     |
| Models         | Model selection and reasoning            |
| Research       | Search, browsing, citations              |
| Browser agent  | Navigation, clicking, forms, screenshots |
| Computer use   | Terminal, filesystem, execution          |
| Memory         | Persistence and retrieval                |
| Agents         | Creation, delegation, coordination       |
| Skills         | Workflow learning and reuse              |
| Automation     | Scheduling and event triggers            |
| Connectors     | Applications and external tools          |
| Security       | Approvals, credentials, isolation        |
| Performance    | Latency, responsiveness, concurrency     |
| Limitations    | UX problems and missing functionality    |

For each feature, document:

- What it does.
- How the user interacts with it.
- What happens behind the interface, based on available evidence.
- What the implementation would require.
- What can be improved.
- What remains unverified.

Include screenshots in:

`docs/research/screenshots/`

Do not copy proprietary branding, illustrations, icons, or exact interface assets. Create an original identity and design system.

---

# PART 2. PRODUCT VISION

Working name: ORBIT AI.

Tagline:

"An AI teammate that doesn't just answer. It gets work done."

Build a platform that allows users to create persistent AI agents capable of performing real-world digital tasks.

The platform should combine:

1. AI conversations.
2. Autonomous task execution.
3. Browser automation.
4. Computer use.
5. Persistent workspaces.
6. Multi-agent collaboration.
7. Long-term memory.
8. Reusable skills.
9. Scheduled routines.
10. File and document intelligence.
11. Code execution.
12. Web research.
13. External integrations.
14. Model flexibility.
15. User-controlled security.

### Core philosophy

The platform must be:

- Open source.
- Provider agnostic.
- Self-hostable.
- Modular.
- Privacy conscious.
- Extensible through plugins.
- Fast and responsive.
- Reliable during long-running tasks.
- Suitable for both individuals and development teams.

The system must not require an xAI subscription or an xAI API key to function.

Support multiple model providers through a consistent adapter architecture.

---

# PART 3. FEATURES THAT CAN MAKE ORBIT BETTER

Do not simply copy the competitor.

Develop features that can provide an actual competitive advantage.

## 1. Universal AI Model Router

Build a model-provider abstraction.

Support:

- OpenAI-compatible APIs.
- xAI.
- Anthropic.
- Google Gemini.
- OpenRouter.
- Ollama.
- Local models.
- Additional providers through adapters.

Capabilities:

- Automatic provider selection.
- Model capability detection.
- Cost-aware routing.
- Latency-aware routing.
- Intelligent fallback.
- Streaming.
- Per-task model selection.
- User-defined model preferences.
- Provider health monitoring.

Create routing policies:

FAST MODE:\
Use a fast model for simple questions and short operations.

BALANCED MODE:\
Balance response quality, latency, and cost.

DEEP MODE:\
Use stronger reasoning models for complex research, architecture, analysis, and coding.

Never silently downgrade important tasks without making the selected model and limitations transparent.

## 2. Autonomous AI Agents

Users must be able to create independent agents.

Each agent should have:

- Name.
- Avatar.
- Role.
- Instructions.
- Model configuration.
- Tools.
- Permissions.
- Memory.
- Workspace.
- Conversation history.
- Execution history.
- Skills.
- Scheduled routines.

Example agents:

- Research Agent.
- Coding Agent.
- Browser Agent.
- Data Analyst.
- Security Researcher.
- Project Manager.
- Testing Agent.
- Documentation Agent.

Agents should maintain their identity and context between conversations.

## 3. Persistent Computer Environment

This is one of the most important features.

Give every workspace an isolated execution environment containing:

- Browser.
- Terminal.
- Filesystem.
- Python.
- Node.js.
- Git.
- Package managers.
- Code editor or file viewer.
- Screenshot capability.
- Download and upload handling.

An agent should be able to:

1. Understand a task.
2. Create a plan.
3. Open a browser.
4. Navigate a website.
5. Read information.
6. Fill permitted forms.
7. Download files.
8. Execute scripts.
9. Create files.
10. Run tests.
11. Inspect results.
12. Report completion.

Use Playwright as a primary browser automation engine.

Combine DOM and accessibility-tree inspection with screenshot-based computer interaction.

Support task checkpoints, execution recovery, browser-state persistence, and task replay.

The user must be able to watch the agent's activity.

Show:

- Current website.
- Browser screenshot.
- Current action.
- Tool being executed.
- Execution status.
- Task progress.
- Errors.
- Approval requests.

Never bypass CAPTCHA or human verification. Pause and request human intervention.

## 4. Multi-Agent Intelligence

Develop an agent coordination engine.

Example:

User:\
"Research five competitors and create a market analysis."

Coordinator delegates:

Research Agent:\
Collects market information.

Browser Agent:\
Visits competitor websites.

Data Agent:\
Extracts and structures data.

Analysis Agent:\
Compares findings.

Verification Agent:\
Checks evidence and citations.

Writing Agent:\
Creates the final report.

Coordinator:\
Combines validated results.

Requirements:

- Parallel execution.
- Agent-to-agent messaging.
- Shared task context with access controls.
- Task delegation.
- Dependency tracking.
- Failure recovery.
- Execution limits.
- Agent cancellation.
- Human approval.
- Results aggregation.

Do not build multiple agents as separate chat windows without actual coordination.

## 5. Persistent Memory Engine

Build a real memory system.

Memory types:

- User preferences.
- Agent instructions.
- Project context.
- Long-term facts.
- Task history.
- Workflow knowledge.
- Important files.
- Decision history.

Implement:

- Memory extraction.
- Relevance scoring.
- Semantic retrieval.
- Memory summarization.
- Memory updates.
- Conflict detection.
- Expiration policies.
- Memory inspection.
- Memory correction.
- Memory deletion.
- Export and portability.

Use PostgreSQL and pgvector where appropriate.

Never treat old memory as authoritative evidence for changing external facts.

## 6. Skills and Workflow Learning

Users should be able to teach agents workflows.

Example:

"Every Monday, visit these websites, collect new information, compare prices, and prepare a report."

The system should be able to convert successful workflows into reusable skills.

Every skill should contain:

- Skill name.
- Description.
- Required inputs.
- Required tools.
- Workflow steps.
- Decision rules.
- Expected output.
- Validation rules.
- Failure handling.
- Permission boundaries.

Support importing, exporting, versioning, and sharing skills.

A demonstrated workflow must be reviewed and tested before being trusted or scheduled.

## 7. Autonomous Routines

Support:

- Scheduled execution.
- Daily routines.
- Weekly routines.
- Custom cron schedules.
- Webhook triggers.
- GitHub events.
- Email events.
- Task-completion triggers.
- Monitoring-based triggers.

Users should be able to pause, edit, inspect, and delete routines.

Show the complete execution history.

## 8. Advanced Web Research

Build an independent research subsystem.

Capabilities:

- Web search.
- Page extraction.
- Multi-source research.
- Search query generation.
- Source comparison.
- Citation generation.
- Contradiction detection.
- Source credibility assessment.
- Research reports.
- Follow-up research.
- Freshness checks.

Each important factual claim should link to its evidence.

Use supported search providers and official APIs.

Support X search through authorized APIs or providers. Do not build a system dependent on scraping private X endpoints.

## 9. AI Coding Agent

Create a dedicated coding environment.

Capabilities:

- Inspect Git repositories.
- Understand codebases.
- Create implementation plans.
- Edit multiple files.
- Generate code.
- Run commands.
- Install dependencies.
- Run tests.
- Inspect failures.
- Fix bugs.
- Create branches.
- Review diffs.
- Generate documentation.
- Create pull-request drafts.

Add:

- Repository indexing.
- Code search.
- Dependency analysis.
- Architecture mapping.
- Regression testing.
- Git history understanding.
- Sandbox execution.

Never execute untrusted repository code directly on the host machine.

## 10. File Intelligence

Support:

- PDF.
- DOCX.
- XLSX.
- CSV.
- TXT.
- Markdown.
- JSON.
- Images.
- Audio.
- Code files.

Functions:

- Document summarization.
- Question answering.
- Semantic search.
- Table extraction.
- Document comparison.
- Report generation.
- Citation references.
- Multiple file analysis.

Support document collections and project-level knowledge bases.

## 11. Multimodal Intelligence

Design provider-independent interfaces for:

- Image understanding.
- Image generation.
- Image editing.
- Speech-to-text.
- Text-to-speech.
- Real-time voice conversations.
- Video understanding.
- Video generation where supported.

Capabilities must be clearly labeled according to provider support.

Do not fake unavailable media generation features.

## 12. MCP and Plugin Ecosystem

Implement Model Context Protocol support.

Allow users to connect external tools through:

- MCP servers.
- Custom function definitions.
- OpenAPI integrations.
- OAuth applications.
- Community plugins.

Build a plugin marketplace architecture.

Every plugin must declare:

- Name.
- Description.
- Required permissions.
- Input schema.
- Output schema.
- Authentication requirements.
- Risk classification.
- Version.
- Execution limits.

---

# PART 4. ARCHITECTURE

Do not build a monolithic application.

Use a modular architecture.

Suggested stack:

### Frontend

- Next.js.
- React.
- TypeScript.
- Tailwind CSS.
- shadcn/ui.
- Zustand or an equivalent state solution.
- Streaming UI.
- Accessible components.

### Backend

- Python.
- FastAPI.
- Pydantic.
- Async architecture.
- REST APIs.
- WebSocket or Server-Sent Events.

### Database

- PostgreSQL.
- pgvector.
- Redis.
- S3-compatible object storage or MinIO.

### AI Layer

- Provider adapter interface.
- Model router.
- Tool registry.
- Agent execution engine.
- Memory service.
- Retrieval service.
- Multi-agent coordinator.

### Automation

- Playwright.
- Browser workers.
- Sandboxed code execution.
- Durable job orchestration.
- Scheduler.

Evaluate Temporal for durable long-running workflows. Use a simpler implementation only when it provides the required persistence and recovery guarantees.

### Deployment

- Docker.
- Docker Compose.
- Environment-based configuration.
- CI/CD.
- Health checks.
- Structured logging.
- Metrics and tracing.

Use current stable package versions after checking official documentation.

---

# PART 5. BACKEND ARCHITECTURE

Organize backend modules around clear responsibilities.

Suggested structure:

backend/\
app/\
api/\
agents/\
orchestration/\
llm/\
providers/\
memory/\
research/\
browser/\
computer/\
tools/\
skills/\
routines/\
files/\
connectors/\
approvals/\
security/\
storage/\
database/\
telemetry/\
configuration/

frontend/\
app/\
components/\
features/\
hooks/\
lib/\
services/\
stores/\
types/

workers/\
browser-worker/\
code-worker/\
agent-worker/\
scheduler/

infrastructure/\
docker/\
scripts/\
deployment/

docs/\
research/\
architecture/\
api/\
security/\
development/

tests/\
unit/\
integration/\
end-to-end/\
evaluation/

This is a starting point, not permission to create meaningless empty folders.

Implement actual modules with working responsibilities.

### Core database entities

Design proper schemas for:

- Users.
- Workspaces.
- Agents.
- Conversations.
- Messages.
- Tasks.
- Task runs.
- Execution steps.
- Tool invocations.
- Approvals.
- Memories.
- Skills.
- Routines.
- Connectors.
- Artifacts.
- Provider configurations.
- Usage events.
- Audit events.

Implement migrations, indexes, ownership relationships, and tenant isolation.

---

# PART 6. SECURITY AND RELIABILITY

Security must be a core architectural feature.

Implement:

1. Authentication.
2. Workspace isolation.
3. Role-based authorization.
4. Secure secret storage.
5. OAuth token handling.
6. Sandboxed browser workers.
7. Sandboxed code execution.
8. Tool permission checks.
9. Rate limiting.
10. Audit logs.
11. Execution timeouts.
12. Resource limits.
13. Network access controls.
14. Input validation.
15. File upload validation.
16. Secure session handling.

### Human approval requirements

Require approval before consequential actions such as:

- Sending emails or external messages.
- Publishing content.
- Purchasing products.
- Making financial transactions.
- Deleting important files.
- Changing account permissions.
- Deploying production changes.
- Accepting legal terms.

Show the user exactly what action will happen before requesting approval.

### Browser security

Treat web pages, emails, files, and documents as untrusted input.

Protect against:

- Prompt injection.
- SSRF.
- Malicious downloads.
- Unauthorized domain access.
- Credential leakage.
- Session hijacking.
- Cross-tenant data access.

Never place provider API keys or passwords in prompts, browser logs, or normal conversation history.

Pause when a website requires a human verification step.

---

# PART 7. MAKE IT EXTREMELY FAST

The product must feel responsive, not like a collection of background scripts.

Implement a measurable performance strategy.

### Speed improvements

1. Stream model output.
2. Stream task progress.
3. Use asynchronous execution.
4. Cache safe and reusable results.
5. Cache model metadata.
6. Use warm execution workers where economical.
7. Parallelize independent research tasks.
8. Avoid unnecessary model calls.
9. Use smaller models for straightforward operations.
10. Compress old conversation context.
11. Retrieve only relevant memories.
12. Deduplicate tool requests.
13. Implement cancellation.
14. Use request timeouts.
15. Add provider fallback.
16. Monitor slow database queries.
17. Lazy-load expensive UI components.
18. Avoid unnecessary frontend rerenders.

### Performance targets

Establish measurable baselines.

Suggested initial targets:

| Metric                         | Initial target                |
| ------------------------------ | ----------------------------- |
| Cached API request p95         | Under 150 ms                  |
| UI usable after load           | Under 2.5 seconds             |
| Fast-model first-token latency | Target under 1.5 seconds      |
| Task progress updates          | Near real-time                |
| Failed-task recovery           | Checkpoint based              |
| Provider failure handling      | Automatic fallback where safe |

These are engineering targets, not guarantees. Measure actual results separately for local execution, cloud execution, and each model provider.

Create:

`docs/PERFORMANCE_BENCHMARKS.md`

Do not sacrifice answer quality or security just to improve a benchmark.

---

# PART 8. UI/UX DESIGN

Create a premium, distinctive AI workspace.

Do not reproduce Grok's exact interface.

Design a modern interface with:

### Main sidebar

- New Chat.
- My Agents.
- Projects.
- Tasks.
- Research.
- Files.
- Skills.
- Automations.
- Connectors.
- Model Settings.
- Usage.
- Settings.

### Main conversation area

- Streaming responses.
- Markdown rendering.
- Code blocks.
- Citations.
- File attachments.
- Tool execution cards.
- Agent status.
- Approval cards.
- Generated artifacts.
- Message editing.
- Conversation search.

### Execution panel

- Current task.
- Current agent.
- Browser preview.
- Terminal output.
- Files created.
- Execution timeline.
- Tool calls.
- Approval requests.

### Visual system

Use:

- Clean typography.
- Carefully designed spacing.
- Strong contrast.
- Restrained accent colors.
- Excellent dark and light themes.
- Smooth transitions.
- Responsive layouts.
- Useful loading states.
- Accessible controls.

Avoid excessive gradients, distracting animations, empty dashboard cards, and unnecessary visual clutter.

Prioritize usability over decoration.

---

# PART 9. FEATURES THAT COULD GIVE US A REAL ADVANTAGE

Implement a clear differentiation strategy.

### A. Open model freedom

Users can switch providers or run local models without changing the application.

### B. Local-first execution

Offer local browser automation, local files, and local model support.

### C. Transparent task execution

Show users exactly what the agent did, what evidence it collected, what files it created, and which tools it used.

### D. Reliable task recovery

Long-running tasks should recover from worker restarts using checkpoints, durable state, and idempotent execution.

### E. Agent evaluation laboratory

Create an evaluation system that measures:

- Task completion rate.
- Research accuracy.
- Citation correctness.
- Tool selection quality.
- Browser task success.
- Coding task success.
- Recovery rate.
- Latency.
- Token usage.
- Cost per successful task.

### F. Public skill ecosystem

Let developers publish, version, share, and install reusable agent skills.

### G. Privacy dashboard

Allow users to inspect and control:

- Stored memories.
- Connected services.
- Saved files.
- Agent permissions.
- Execution history.
- Usage data.
- Data retention.

### H. Developer ecosystem

Provide:

- Public API.
- Python SDK.
- TypeScript SDK.
- MCP support.
- Plugin development tools.
- Example agents.
- Self-hosting instructions.

These are potential differentiators. Validate them with actual users rather than assuming more features automatically means a better product.

---

# PART 10. DEVELOPMENT EXECUTION PLAN

Do not attempt to implement every feature simultaneously.

Build in phases.

### PHASE 0: Research

- Inspect Grok and Grok Bot.
- Review official documentation.
- Investigate publicly accessible workflows.
- Capture screenshots.
- Build a feature comparison matrix.
- Identify opportunities.
- Write the technical specification.

Deliver:

- Competitor analysis.
- Product requirements.
- Architecture proposal.
- Risk assessment.

### PHASE 1: Foundation

- Inspect the existing repository.
- Preserve existing useful work.
- Establish development tooling.
- Set up frontend and backend.
- Set up database and migrations.
- Implement authentication.
- Implement provider abstraction.
- Implement streaming chat.

Deliver a working chat application.

### PHASE 2: AI Agent Engine

- Create agents.
- Define tool schemas.
- Implement the agent execution loop.
- Implement tool calling.
- Persist execution state.
- Add task progress events.
- Add error handling.

Deliver agents that can actually use tools.

### PHASE 3: Research and Files

- Web search.
- Page extraction.
- Citation rendering.
- File uploads.
- Document parsing.
- Retrieval.
- Research reports.

Deliver a useful research assistant.

### PHASE 4: Computer Use

- Persistent workspace.
- Browser worker.
- Playwright interaction.
- Screenshots.
- Terminal.
- Filesystem.
- Code sandbox.
- Execution timeline.

Deliver an agent that completes permitted browser and computer tasks.

### PHASE 5: Memory and Skills

- Long-term memory.
- Memory management.
- Skill creation.
- Workflow testing.
- Skill import/export.
- Scheduled routines.

Deliver persistent agents that improve through reusable workflows.

### PHASE 6: Multi-Agent System

- Coordinator.
- Specialist agents.
- Delegation.
- Parallel tasks.
- Shared project context.
- Result validation.
- Agent collaboration UI.

Deliver genuine multi-agent coordination.

### PHASE 7: Advanced Capabilities

- MCP.
- External connectors.
- Voice.
- Image understanding.
- Image generation.
- Video support where providers permit.
- Plugin ecosystem.

### PHASE 8: Production Readiness

- Security audit.
- Performance benchmarks.
- Integration tests.
- E2E tests.
- Load tests.
- Documentation.
- Docker deployment.
- CI pipeline.
- Backup and recovery.

---

# PART 11. TESTING AND EVALUATION

Every feature must have real tests.

Create test scenarios for:

1. Basic conversation.
2. Streaming.
3. Provider switching.
4. Provider failure.
5. Web research with citations.
6. File upload and analysis.
7. Persistent memory retrieval.
8. Browser navigation.
9. Form interaction on a permitted test website.
10. Code execution in a sandbox.
11. Multi-agent delegation.
12. Task recovery.
13. Routine scheduling.
14. Approval enforcement.
15. Cross-workspace isolation.
16. Prompt injection handling.
17. Malicious file handling.
18. Concurrent tasks.

Build an evaluation dashboard that tracks task success, time, quality, cost, and failure reasons.

Where authorized access to the original product exists, compare equivalent tasks using the same input and record methodology and limitations.

Never invent competitor test results.

---

# PART 12. OPEN-SOURCE STANDARD

Prepare the repository for public release.

Include:

- Apache-2.0 license, subject to dependency compatibility.
- README.md.
- CONTRIBUTING.md.
- CODE_OF_CONDUCT.md.
- SECURITY.md.
- .env.example.
- Docker Compose.
- API documentation.
- Architecture documentation.
- Setup instructions.
- Example configurations.
- Example agents.
- Test suite.
- CI workflows.
- Issue templates.
- Pull request template.

Never commit API keys, credentials, user data, or private browser state.

Make the platform easy for developers to install and contribute to.

---

# PART 13. FINAL ENGINEERING RULES

Follow these rules throughout the project.

1. Research before implementation.
2. Inspect the existing repository before editing.
3. Do not delete working functionality.
4. Do not create fake buttons.
5. Do not create placeholder features and label them complete.
6. Do not hardcode API keys.
7. Do not assume a model supports every capability.
8. Do not expose internal reasoning traces.
9. Do not execute untrusted code outside a sandbox.
10. Do not bypass website security.
11. Write clean, typed, maintainable code.
12. Add tests with each meaningful feature.
13. Update documentation whenever architecture changes.
14. Use actual working integrations.
15. Handle loading, failure, and retry states.
16. Validate database migrations.
17. Verify the frontend and backend together.
18. Report limitations honestly.

If a provider key is unavailable, build the adapter and a mock provider for tests, clearly mark the live integration as unconfigured, and continue implementing the rest.

Do not repeatedly ask me to approve routine technical decisions. Choose sensible defaults, record your decisions, and continue.

Do not stop after creating a plan. After the research and architecture documents, begin implementation and verify each phase.

---

# FINAL DELIVERABLES

At completion, provide:

1. Complete source code.
2. Organized repository structure.
3. Working frontend.
4. Working backend.
5. Database migrations.
6. Agent execution engine.
7. Browser automation implementation.
8. Provider integrations.
9. Agent and tool registry.
10. Memory subsystem.
11. Skills and routines.
12. Security implementation.
13. Automated tests.
14. Docker deployment.
15. Complete documentation.
16. Architecture diagrams.
17. Competitor research report.
18. Performance benchmark report.
19. Setup and deployment instructions.
20. Organized ZIP archive of the complete project.

Your final report must distinguish:

- Implemented and tested.
- Implemented but not live-configured.
- Partially implemented.
- Planned but not implemented.
- Blocked by external requirements.

Include actual test results, command output, known issues, and the next development priorities.

**The final objective is not to make another chatbot that looks like Grok. Build an independent, open-source AI execution platform that can perform useful work reliably, safely, and efficiently.**

Start with Phase 0. Use the browser. Research the real product. Produce evidence-based findings. Then build the system.

## What makes this architecture competitive?

These are the five areas I would prioritize rather than spending months polishing a chat interface.

[BrowserOS: Free Agentic Browser That Works — Oscar Le](https://images.openai.com/static-rsc-4/M_IV7eNaPnq_SWy9aO4Mm9XpxfjU7_YzqA7tF02urBcADI8VXCK8zK9OUfp-fkEts6_ILm1nUBJCuw8Sj6AEtzwF7seTe5mS_mzfot5x88_JASTVPMMh1Yg9pZ3dMCcLs2otBaBBpfah1ZNkwVfdhgV5YfxgPiSldmaOINfWCm8?purpose=inline)

1\. Computer-use engine

Persistent browser, terminal, filesystem, screenshots, task recovery, and execution history.

Highest priority

[AI Orchestration Engine - HES](https://images.openai.com/static-rsc-4/6DIX5O0f4FWJXbziQcwVcmqnJdu_WaVUi6corLtuWAwBgHVOu7jHMhkncqEvv71bvmeSXUfa5W7QKxdIMFCXS4hff2oJZRKCTWwg2-4xJ_a-SI1pJxnWHooXDc8aIDy-S341k0l2tZ8G2rnfhPQLmaFvHVQ75GO4zo35Ca_m5C4?purpose=inline)

2\. Multi-agent orchestration

Agents delegate work, communicate, run in parallel, and verify each other's results.

[22 Pages in Claude Design, 40,000 Lines of Code, and Three Rounds of Review: Redesigning a Dashboard the Hard Way | its-boris.com](https://images.openai.com/static-rsc-4/rFHY-WSH6s3tnsnz4CND5OGeFrThAVzavcOo6AUHpT62OLbB7ARXMYceKEjlV2Z2BA2BBxk7BBiZDBzS9ufwskmSKTyUTypZN7ZrovWYHi4gEHmWEEwnGOatnXaz1_KQUa_31mOkvOVE5NDNw_J6hjGFe2GPmt-iPGoF0hLyVJM?purpose=inline)

3\. Universal model router

Switch between paid APIs and local models while controlling cost, speed, and quality.

[Pallix | AI Visibility & Citation Intelligence](https://images.openai.com/static-rsc-4/WzN00fptyZb8dH-u_r7RrJH0Eek_z7g9E2hJaH9zy4rBPXp-OGpUDeU96Bm8hdiPNUvyh_g9cPkSYWjQgY9DFnVV0GpLrHk_5l1wypi1Q6aOleMKFi9uViBYcVJNgBkxEFTZQKyLGRWR0SQGEBQFfcmBJ088c2aVBdKma5JOqx0?purpose=inline)

4\. Evidence-based research

Search, compare sources, check claims, and produce reports with citations.

[Capafy - AI Agents Tool](https://images.openai.com/static-rsc-4/64NswzIyIvi6Sxh4dQl5trZFDybD5ZTcHoaySjrK-xRaFlREKqvJ2ymFkbvgZWabNQHIwYJPGyi19mebhNJ4vim9xJW9YNZDVWmvkaFFoiWCGJ7dPsj5jcsABURXVbh9JzJAbYLSjVdtYTnUh5upRdyWQbXGhCNZYp7Za1s5mxU?purpose=inline)

5\. Open skill ecosystem

Reusable workflows, community plugins, MCP integrations, and scheduled execution.

These priorities align with documented Grok Bot capabilities such as persistent computer access, reusable skills, and scheduled routines.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.x.ai\&sz=32)

SpaceXSI Docs+1



## Recommended implementation strategy

Do not try to train a frontier model from scratch for this project. That would consume enormous resources before you even have a working agent.

Build the agent execution infrastructure independently, then support models from xAI, OpenAI, Anthropic, Gemini, OpenRouter, and Ollama. xAI already documents built-in search, X Search, code execution, image generation, collections search, and custom function tools, so these can be integrated through your provider abstraction where appropriate.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://docs.x.ai\&sz=32)

SpaceXSI Docs+1



My suggested MVP order:

| Priority | Component                | Goal                    |
| -------- | ------------------------ | ----------------------- |
| P0       | AI chat + model router   | Working foundation      |
| P0       | Agent/tool execution     | Perform actual tasks    |
| P1       | Browser + computer use   | Operate websites        |
| P1       | Research engine          | Search and verify       |
| P1       | Persistent memory        | Remember useful context |
| P2       | Multi-agent coordination | Delegate work           |
| P2       | Skills + routines        | Automate repeated tasks |
| P3       | Voice + media            | Multimodal experience   |
| P3       | Plugin marketplace       | Open ecosystem          |

Official research references:

- [Grok Bot architecture and overview](https://docs.x.ai/grok-bot/overview?utm_source=chatgpt.com)
- [Grok Bot computer and app functionality](https://docs.x.ai/grok-bot/computer-and-apps?utm_source=chatgpt.com)
- [Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations?utm_source=chatgpt.com)
- [Approvals and security](https://docs.x.ai/grok-bot/approvals-security-and-privacy?utm_source=chatgpt.com)
- [xAI developer tools](https://docs.x.ai/developers/tools/overview?trk=article-ssr-frontend-pulse_little-text-block\&utm_source=chatgpt.com)

## What you should do next

Start by giving the master prompt to Codex or Antigravity with browser access and access to your development workspace. Have it complete the competitor research report and architecture before implementing the first working vertical slice.

One important engineering decision: get the browser agent and persistent task execution working before building multi-agent coordination. Multiple agents without a reliable execution engine just create multiple ways for the same task to fail.