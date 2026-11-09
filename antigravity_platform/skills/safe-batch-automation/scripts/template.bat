@echo off
:: ==============================================================================
:: Safe Batch Automation Template
:: Purpose: Template for token-saving, automated, and safe Windows task execution
:: ==============================================================================
setlocal EnableExtensions EnableDelayedExpansion

:: --- Configuration & Defaults ---
set "SCRIPT_NAME=%~nx0"
set "SCRIPT_DIR=%~dp0"
set "LOG_DIR=%SCRIPT_DIR%logs"
set "TIMESTAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "TIMESTAMP=%TIMESTAMP: =0%"
set "LOG_FILE=%LOG_DIR%\task_%TIMESTAMP%.log"

set "DRY_RUN=0"
set "VERBOSE=0"
set "EXIT_CODE=0"
set "TARGET_PARAM="

:: --- Argument Parsing ---
:PARSE_ARGS
if "%~1"=="" goto MAIN
if /i "%~1"=="--dry-run" (
    set "DRY_RUN=1"
    shift
    goto PARSE_ARGS
)
if /i "%~1"=="/dryrun" (
    set "DRY_RUN=1"
    shift
    goto PARSE_ARGS
)
if /i "%~1"=="--verbose" (
    set "VERBOSE=1"
    shift
    goto PARSE_ARGS
)
if /i "%~1"=="-v" (
    set "VERBOSE=1"
    shift
    goto PARSE_ARGS
)
if /i "%~1"=="--help" (
    goto SHOW_HELP
)
if /i "%~1"=="/?" (
    goto SHOW_HELP
)
:: Capture positional target parameter if provided
if not defined TARGET_PARAM (
    set "TARGET_PARAM=%~1"
    shift
    goto PARSE_ARGS
)
shift
goto PARSE_ARGS

:SHOW_HELP
echo Usage: %SCRIPT_NAME% [options] [target]
echo.
echo Options:
echo   --dry-run, /dryrun   Preview actions without making changes (Safe Mode)
echo   --verbose, -v        Display detailed output to console (Default: summary only)
echo   --help, /?           Show this help message
exit /b 0

:: --- Main Routine ---
:MAIN
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%" >nul 2>&1

echo [INFO] Starting %SCRIPT_NAME% at %DATE% %TIME%
if "%DRY_RUN%"=="1" echo [PREVIEW] Running in DRY-RUN mode. No changes will be committed.
echo [LOG] Detailed log: "%LOG_FILE%"

:: Step 1: Pre-execution validation
call :TASK_STEP "Step 1: Validate environment and inputs" :STEP_VALIDATE
if !EXIT_CODE! neq 0 goto FINISH

:: Step 2: Processing action
call :TASK_STEP "Step 2: Execute operations" :STEP_PROCESS
if !EXIT_CODE! neq 0 goto FINISH

:: Step 3: Verification
call :TASK_STEP "Step 3: Verify outputs" :STEP_VERIFY
if !EXIT_CODE! neq 0 goto FINISH

:FINISH
if !EXIT_CODE! equ 0 (
    echo [SUCCESS] %SCRIPT_NAME% completed successfully.
) else (
    echo [ERROR] %SCRIPT_NAME% failed with exit code !EXIT_CODE!. Check log: "%LOG_FILE%"
)
exit /b !EXIT_CODE!

:: --- Helper: Execute and log step ---
:TASK_STEP
set "STEP_TITLE=%~1"
set "STEP_ROUTINE=%~2"
echo [STEP] !STEP_TITLE! ...
if "%VERBOSE%"=="1" (
    call %STEP_ROUTINE%
    set "STEP_ERR=!errorlevel!"
) else (
    call %STEP_ROUTINE% >> "%LOG_FILE%" 2>&1
    set "STEP_ERR=!errorlevel!"
)
if !STEP_ERR! neq 0 (
    echo [FAIL] !STEP_TITLE! failed (Code: !STEP_ERR!)
    set "EXIT_CODE=!STEP_ERR!"
    exit /b !STEP_ERR!
) else (
    echo [DONE] !STEP_TITLE!
)
exit /b 0

:: --- Step Implementations ---
:STEP_VALIDATE
echo Validating environment prerequisites...
:: Safe Guard: Check if target parameter is valid if required
if defined TARGET_PARAM (
    echo Target parameter received: %TARGET_PARAM%
)
if "%DRY_RUN%"=="1" (
    echo [DRY-RUN] Prerequisite checks simulated ok.
    exit /b 0
)
exit /b 0

:STEP_PROCESS
echo Executing core automated logic...
if "%DRY_RUN%"=="1" (
    echo [DRY-RUN] Would process action for target: %TARGET_PARAM%
    exit /b 0
)
:: Place actual commands here (e.g., builds, file transformations, tests)
exit /b 0

:STEP_VERIFY
echo Verifying result artifacts...
if "%DRY_RUN%"=="1" (
    echo [DRY-RUN] Output verification simulated ok.
    exit /b 0
)
exit /b 0

