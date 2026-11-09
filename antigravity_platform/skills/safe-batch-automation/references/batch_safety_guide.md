# Windows Batch Safety Guide

This guide outlines essential safeguards and best practices when authoring or executing Windows `.bat` and `.cmd` automation scripts in agentic environments.

---

## 1. The Empty Variable Catastrophe

### The Problem
In standard batch scripts, if a variable is unset or empty, `rmdir /s /q "%TARGET_DIR%"` expands to `rmdir /s /q ""` which can cause undefined behavior, or `del /q "%DIR%\*"` expands to `del /q "\*"` which attempts to wipe the root drive directory!

### The Defense
Always validate that critical path variables are non-empty and defined before any destructive action:

```bat
if not defined TARGET_DIR (
    echo [SAFETY ERROR] TARGET_DIR is not defined. Aborting.
    exit /b 1
)
if "%TARGET_DIR%"=="" (
    echo [SAFETY ERROR] TARGET_DIR is empty. Aborting.
    exit /b 1
)
```

---

## 2. Drive Root and System Folder Guard

### The Problem
A script with a bad parameter (e.g. `\` or `C:\`) might attempt to delete or alter system-critical partitions.

### The Defense
Resolve the fully qualified path and check length/path restrictions:

```bat
for %%F in ("%TARGET_DIR%") do set "ABS_TARGET=%%~fF"

:: Check if path is root of drive (e.g., C:\ is 3 characters long)
if "%ABS_TARGET:~3%"=="" (
    echo [SAFETY ERROR] Refusing to operate on root drive: "%ABS_TARGET%"
    exit /b 1
)

:: Check if targeting Windows system directory
if /i "%ABS_TARGET%"=="%SystemRoot%" (
    echo [SAFETY ERROR] Operation forbidden on Windows directory!
    exit /b 1
)
```

---

## 3. Mandatory Environment Isolation (`SETLOCAL`)

Always start every batch automation with:
```bat
setlocal EnableExtensions EnableDelayedExpansion
```

### Why:
1. **Isolation**: Variables set inside the script will not bleed into the user's terminal or subsequent commands.
2. **Delayed Expansion**: Inside loops (`for`) and conditional blocks (`if`), standard `%VAR%` expands only once at parse time. Using `!VAR!` reads the runtime value after preceding commands modify it.
3. **Restoration**: `endlocal` (or script exit) cleanly restores the environment.

---

## 4. Parenthesis Trap in Compound Blocks

### The Problem
In batch files, an unescaped closing parenthesis `)` inside an `if (...)` or `for (...)` block immediately closes the block, causing syntax errors or truncated commands:

```bat
:: BROKEN:
if "%MODE%"=="DRYRUN" (
    echo Previewing (safe mode)
)
:: The ')' in "(safe mode)" closes the 'if' block early!
```

### The Solutions
- **Option A (Recommended)**: Use square brackets `[...]` instead of parentheses:
  ```bat
  echo Previewing [safe mode]
  ```
- **Option B**: Escape the closing parenthesis with a caret `^`:
  ```bat
  echo Previewing (safe mode^)
  ```

---

## 5. Fail-Fast Error Trapping

Never continue executing downstream commands when an earlier critical command fails.

```bat
cmd /c "npm run build"
if errorlevel 1 (
    echo [ERROR] Build failed with exit code %errorlevel%.
    exit /b %errorlevel%
)
```

Inside delayed expansion blocks, check `!ERRORLEVEL!`:
```bat
call :MY_TASK
if !errorlevel! neq 0 (
    echo [ERROR] Step failed with code !errorlevel!
    exit /b !errorlevel!
)
```

---

## 6. Safe Mode / Dry-Run Convention

Any batch script designed to remove, overwrite, terminate, or move resources must:
1. Default to **Dry-Run (Preview)** mode or support `/dryrun` / `--dry-run`.
2. Require an explicit `--confirm`, `--force`, or `/doit` flag to commit destructive operations.
3. List candidate items before taking action.

---

## 7. Cross-Drive Navigation Guard (`cd /d`)

### The Problem
In Windows Command Prompt (`cmd.exe`), typing `cd D:\project` does **not** switch the active drive if the shell is currently on `C:`. It only updates the remembered working directory for drive `D:`, leaving execution on `C:`. Subsequent commands then run in the wrong drive/directory, risking unintended modifications.

### The Defense
Always specify the `/d` switch when changing directories across drives:
```bat
cd /d "D:\rea"
if errorlevel 1 (
    echo [ERROR] Failed to switch drive/directory to D:\rea
    exit /b 1
)
```

---

## 8. Host Architecture Fallback (ARM64 vs. x64)

### The Problem
Native binary extensions (`.node`, `.dll`) compiled for `x64` will fail with errors (such as `requires a Windows x64 host`) when running on Windows ARM64 (e.g. Snapdragon, Surface Pro X) using a native ARM64 Node.js runtime.

### The Defense
Detect the architecture or wrap native calls in fallbacks:
```bat
if /i "%PROCESSOR_ARCHITECTURE%"=="ARM64" (
    echo [INFO] Detected Windows ARM64 host. Applying compatible fallback mode.
)
```
In JavaScript/Node automation scripts, wrap native loader calls in a `try/catch` and gracefully fall back to portable cross-spawn execution.


