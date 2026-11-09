# Token Optimization Patterns for Batch Automation

This guide explains how automating workflows through Windows `.bat` scripts dramatically reduces LLM token consumption and prevents context window bloat.

---

## The Context Token Problem

In AI-assisted pair programming, each terminal tool call (`run_command`) consumes tokens in multiple ways:
1. **Prompt Re-transmission**: Every tool call sends the conversation history again. Running 6 sequential commands consumes 6 roundtrips of full context re-reads.
2. **Output Flooding**: Compilers, linters, package managers (`npm`, `pip`, `cargo`, `mvn`), and test suites often emit hundreds to thousands of lines. A 1,000-line build log consumes ~4,000 - 8,000 context tokens.
3. **Context Degradation**: Flooding the context window with raw stdout pushes important code definitions, user constraints, and instructions out of immediate attention.

---

## Optimization Patterns

### Pattern 1: Silent Log Redirection
Instead of letting noisy tools dump directly to stdout, redirect all output to a temporary log file and print a single concise summary line.

```bat
:: Standard (Token-heavy): Emits 800 lines of output (~3,000 tokens)
npm run build

:: Optimized (Token-saving): Emits 1 line (~15 tokens)
call npm run build > "%LOG_FILE%" 2>&1
if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Build completed.
) else (
    echo [ERROR] Build failed. See %LOG_FILE%
)
```

**Token Savings**: **~98% reduction** on successful operations.

---

### Pattern 2: Targeted Failure Tail
When a failure occurs, agents only need the error stack trace, not the 500 lines of setup logs. Output only the last 10–15 lines:

```bat
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Task failed with code %ERRORLEVEL%. Last lines of log:
    powershell -NoProfile -Command "Get-Content -Path '%LOG_FILE%' -Tail 12"
    exit /b %ERRORLEVEL%
)
```

**Token Savings**: Keeps error diagnosis within ~100 tokens instead of several thousand.

---

### Pattern 3: Single-Shot Batch Aggregation
When performing a multi-step routine (e.g., Clean -> Build -> Test -> Package):

**Anti-Pattern (5 agent turns):**
- Turn 1: `npm run clean`
- Turn 2: `npm install`
- Turn 3: `npm run build`
- Turn 4: `npm test`
- Turn 5: `npm run package`
*(Total: 5 roundtrips, ~50,000 cumulative tokens processed across turns)*

**Optimized Pattern (1 agent turn):**
- Agent generates or invokes `run_pipeline.bat`
- Batch file executes all 5 steps sequentially, fails fast if any step breaks, and outputs a 5-line summary table:
  ```text
  [STEP 1/5] Clean: [DONE]
  [STEP 2/5] Install: [DONE]
  [STEP 3/5] Build: [DONE]
  [STEP 4/5] Test: [DONE]
  [STEP 5/5] Package: [DONE]
  [RESULT] All steps succeeded in 12s.
  ```
*(Total: 1 roundtrip, ~500 tokens)*

---

### Pattern 4: Filtered Stream Pipes
If an agent needs specific metrics (e.g. test counts or warnings) without saving a full log:

```bat
:: Filter with findstr
npm test 2>&1 | findstr /i /c:"pass" /c:"fail" /c:"error" /c:"warning"
```

Only matching status lines reach the agent's context.

