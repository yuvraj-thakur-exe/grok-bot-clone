@echo off
setlocal enabledelayedexpansion

:: ============================================================================
:: ORBIT / GROK BOT CLONE (GBC) - New Machine Setup & Auto-Installer
:: ============================================================================
:: This script initializes a fresh clone of ORBIT on any Windows machine:
:: 1. Verifies prerequisites (Python 3.11+, Git, Node.js, pnpm/npm).
:: 2. Creates the unified directory layout.
:: 3. Clones and verifies required upstream repositories (OpenGrokBot, OmniVoice).
:: 4. Configures Python virtual environment and installs dependencies.
:: 5. Runs the diagnostic health check and full test suite.
:: ============================================================================

set "SCRIPT_DIR=%~dp0"
if "%SCRIPT_DIR:~-1%"=="\" set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
cd /d "%SCRIPT_DIR%"

set "LOG_DIR=%SCRIPT_DIR%\logs"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
set "LOG_FILE=%LOG_DIR%\setup_%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%_%TIME:~0,2%%TIME:~3,2%%TIME:~6,2%.log"
set "LOG_FILE=%LOG_FILE: =0%"

echo ============================================================================
echo   ORBIT / GROK BOT CLONE - Machine Setup ^& Dependency Installer
echo ============================================================================
echo Root directory: %SCRIPT_DIR%
echo Setup log file: %LOG_FILE%
echo.

:: ----------------------------------------------------------------------------
:: STEP 1: Verify Prerequisites
:: ----------------------------------------------------------------------------
echo [1/6] Checking system prerequisites...

where git >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git is not installed or not in PATH.
    echo Please install Git from https://git-scm.com/ and re-run this script.
    exit /b 1
)
for /f "tokens=*" %%v in ('git --version 2^>nul') do set "GIT_VER=%%v"
echo   [OK] Git detected: %GIT_VER%

where python >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python 3.11 or newer from https://www.python.org/
    exit /b 1
)
for /f "tokens=*" %%v in ('python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')" 2^>nul') do set "PY_VER=%%v"
echo   [OK] Python detected: %PY_VER%

python -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python version %PY_VER% is below required minimum 3.11.
    exit /b 1
)

where node >nul 2>&1
if errorlevel 1 (
    echo   [WARNING] Node.js not detected. Node.js 18+ is recommended for the web/desktop UI.
) else (
    for /f "tokens=*" %%v in ('node -v 2^>nul') do set "NODE_VER=%%v"
    echo   [OK] Node.js detected: !NODE_VER!
)

where pnpm >nul 2>&1
if errorlevel 1 (
    echo   [NOTE] pnpm not detected in PATH. npm will be used as fallback.
) else (
    for /f "tokens=*" %%v in ('pnpm -v 2^>nul') do set "PNPM_VER=%%v"
    echo   [OK] pnpm detected: !PNPM_VER!
)
echo.

:: ----------------------------------------------------------------------------
:: STEP 2: Initialize Core Directories
:: ----------------------------------------------------------------------------
echo [2/6] Ensuring directory structure exists...
for %%d in (
    "upstream"
    "configs"
    "logs"
    "reports"
    "reports\repo-audits"
    ".orbit"
    ".orbit\runs"
    ".antigravity"
    "antigravity_platform\config"
    "docs\02-research\grokbot-rea-reports"
) do (
    if not exist "%SCRIPT_DIR%\%%~d" (
        mkdir "%SCRIPT_DIR%\%%~d" >nul 2>&1
        echo   Created: %%~d
    )
)
echo   [OK] Directory layout initialized.
echo.

:: ----------------------------------------------------------------------------
:: STEP 3: Setup Python Environment & Dependencies
:: ----------------------------------------------------------------------------
echo [3/6] Setting up Python environment...
if not exist "%SCRIPT_DIR%\.venv" (
    echo   Creating local virtual environment at .venv...
    python -m venv "%SCRIPT_DIR%\.venv" >> "%LOG_FILE%" 2>&1
    if errorlevel 1 (
        echo   [WARNING] Could not create .venv. Continuing with host Python...
        set "PY_CMD=python"
    ) else (
        set "PY_CMD=%SCRIPT_DIR%\.venv\Scripts\python.exe"
        echo   [OK] Virtual environment created.
    )
) else (
    set "PY_CMD=%SCRIPT_DIR%\.venv\Scripts\python.exe"
    echo   [OK] Existing .venv detected.
)

echo   Installing/verifying required Python packages [pyyaml, pytest]...
"%PY_CMD%" -m pip install --upgrade pip >nul 2>&1
"%PY_CMD%" -m pip install pyyaml pytest >> "%LOG_FILE%" 2>&1
if errorlevel 1 (
    echo   [WARNING] Pip install had warnings. Inspect %LOG_FILE% for details.
) else (
    echo   [OK] Python packages verified.
)
echo.

:: ----------------------------------------------------------------------------
:: STEP 4: Clone & Verify Upstream Repositories
:: ----------------------------------------------------------------------------
echo [4/6] Setting up upstream repositories...

:: 4a. OpenGrokBot
set "OPENGROKBOT_DIR=%SCRIPT_DIR%\upstream\opengrokbot"
if not exist "%OPENGROKBOT_DIR%\.git" (
    echo   Cloning OpenGrokBot [Z4YT0N/OpenGrokBot]...
    git clone https://github.com/Z4YT0N/OpenGrokBot.git "%OPENGROKBOT_DIR%" >> "%LOG_FILE%" 2>&1
    if errorlevel 1 (
        echo   [ERROR] Failed to clone OpenGrokBot. Check network connection.
    ) else (
        git -C "%OPENGROKBOT_DIR%" checkout 86e45d2023e6921a79ad9bfcdc5d25ac0a593bdc >> "%LOG_FILE%" 2>&1
        echo   [OK] OpenGrokBot cloned and pinned to commit 86e45d2.
    )
) else (
    echo   [OK] OpenGrokBot already present at upstream\opengrokbot.
)

:: 4b. OmniVoice
set "OMNIVOICE_DIR=%SCRIPT_DIR%\upstream\omnivoice"
if not exist "%OMNIVOICE_DIR%\.git" (
    echo   Cloning OmniVoice [k2-fsa/OmniVoice]...
    git clone --depth 1 https://github.com/k2-fsa/OmniVoice.git "%OMNIVOICE_DIR%" >> "%LOG_FILE%" 2>&1
    if errorlevel 1 (
        echo   [WARNING] Failed to clone OmniVoice. Can be cloned later via scripts\clone_upstreams.
    ) else (
        echo   [OK] OmniVoice cloned into upstream\omnivoice.
    )
) else (
    echo   [OK] OmniVoice already present at upstream\omnivoice.
)
echo.

:: ----------------------------------------------------------------------------
:: STEP 5: Run Verification & Health Checks
:: ----------------------------------------------------------------------------
echo [5/6] Running system diagnostics and health checks...

set "PYTHONPATH=%SCRIPT_DIR%\src"
"%PY_CMD%" -m orbit_cli doctor
if errorlevel 1 (
    echo [WARNING] orbit_cli doctor reported warnings.
)

echo.
echo Running unit test suite (17 tests)...
"%PY_CMD%" -m unittest discover -s "%SCRIPT_DIR%\tests" -v
if errorlevel 1 (
    echo [ERROR] Some unit tests failed. Inspect the output above.
) else (
    echo [OK] All tests passed cleanly.
)
echo.

:: ----------------------------------------------------------------------------
:: STEP 6: Summary & Ready to Work
:: ----------------------------------------------------------------------------
echo ============================================================================
echo   SETUP COMPLETE - ORBIT / GBC IS READY!
echo ============================================================================
echo.
echo You can now use the following commands from this folder:
echo.
echo   .\orbit.ps1 doctor                 - Run system diagnostic check
echo   .\orbit.ps1 run --validate-only    - Validate task DAG manifests
echo   .\orbit.ps1 storage status         - Check storage budget and reserve
echo.
echo For detailed instructions and architecture specs, see:
echo   - SETUP_ON_NEW_MACHINE.md
echo   - README.md
echo   - docs\02-research\grokbot-rea-reports\architecture_report.md
echo.
exit /b 0

