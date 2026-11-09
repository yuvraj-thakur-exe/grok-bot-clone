@echo off
:: ==============================================================================
:: Safe Runner Utility
:: Purpose: Runs arbitrary commands or batch jobs silently to save tokens,
::          capturing output to a log file and outputting only a concise summary.
:: Usage:
::   safe_runner.bat "Task Name" "command line to execute" [--show-output-on-fail]
:: ==============================================================================
setlocal EnableExtensions EnableDelayedExpansion

if "%~1"=="" goto USAGE
if "%~1"=="/?" goto USAGE
if "%~1"=="--help" goto USAGE

set "TASK_NAME=%~1"
set "CMD_TO_RUN=%~2"
set "SHOW_TAIL_ON_FAIL=1"

if "%~2"=="" (
    echo [ERROR] No command specified.
    goto USAGE
)

:: Create log folder
set "LOG_DIR=%~dp0logs"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%" >nul 2>&1

:: Timestamp for log file
set "T_STAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "T_STAMP=%T_STAMP: =0%"
set "LOG_PATH=%LOG_DIR%\run_%T_STAMP%.log"

echo [START] %TASK_NAME%...
echo [%DATE% %TIME%] Command: %CMD_TO_RUN% > "%LOG_PATH%"

:: Record start time in seconds (PowerShell quick timestamp for precision)
for /f "usebackq tokens=*" %%T in (`powershell -NoProfile -Command "[DateTimeOffset]::UtcNow.ToUnixTimeSeconds()"`) do set "START_SEC=%%T"

:: Execute command and redirect both stdout and stderr
cmd /c "%CMD_TO_RUN%" >> "%LOG_PATH%" 2>&1
set "CMD_EXIT_CODE=%errorlevel%"

:: Record end time
for /f "usebackq tokens=*" %%T in (`powershell -NoProfile -Command "[DateTimeOffset]::UtcNow.ToUnixTimeSeconds()"`) do set "END_SEC=%%T"
set /a DURATION=!END_SEC!-!START_SEC! 2>nul
if not defined DURATION set "DURATION=0"

if %CMD_EXIT_CODE% equ 0 (
    echo [SUCCESS] %TASK_NAME% finished in !DURATION!s [Code: 0]
    echo [LOG] Log saved: %LOG_PATH%
    exit /b 0
) else (
    echo [ERROR] %TASK_NAME% failed in !DURATION!s [Code: %CMD_EXIT_CODE%]
    echo [LOG] Full log saved: %LOG_PATH%
    if "%SHOW_TAIL_ON_FAIL%"=="1" (
        echo [TAIL] Last 10 lines of output:
        echo ------------------------------------------------------------
        powershell -NoProfile -Command "Get-Content -Path '%LOG_PATH%' -Tail 10 -ErrorAction SilentlyContinue"
        echo ------------------------------------------------------------
    )
    exit /b %CMD_EXIT_CODE%
)

:USAGE
echo Usage: safe_runner.bat "Task Label" "command to run"
echo.
echo Example:
echo   safe_runner.bat "Build Project" "npm run build"
echo   safe_runner.bat "Run Tests" "pytest tests/"
exit /b 1
