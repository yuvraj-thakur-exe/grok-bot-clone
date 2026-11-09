@echo off
:: ==============================================================================
:: REA Safe Runner Utility
:: Purpose: Runs REA commands and build tasks safely in D:\rea with token saving
:: Usage:
::   rea_runner.bat [build | check | doctor | start | run <args...>]
:: ==============================================================================
setlocal EnableExtensions EnableDelayedExpansion

set "REA_DIR=D:\rea"
set "LOG_DIR=%~dp0logs"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%" >nul 2>&1

set "T_STAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%"
set "T_STAMP=%T_STAMP: =0%"
set "LOG_FILE=%LOG_DIR%\rea_%T_STAMP%.log"

if not exist "%REA_DIR%" (
    echo [ERROR] REA directory not found at "%REA_DIR%".
    exit /b 1
)

:: Ensure cross-drive switch
cd /d "%REA_DIR%" || (
    echo [ERROR] Failed to switch to %REA_DIR%
    exit /b 1
)

set "ACTION=%~1"
if "%ACTION%"=="" set "ACTION=check"

if /i "%ACTION%"=="build" (
    echo [START] Building REA in %REA_DIR%...
    call npm run build > "%LOG_FILE%" 2>&1
    set "ERR=!errorlevel!"
    goto REPORT
)

if /i "%ACTION%"=="check" (
    echo [START] Running REA fast check in %REA_DIR%...
    call npm run check:fast > "%LOG_FILE%" 2>&1
    set "ERR=!errorlevel!"
    goto REPORT
)

if /i "%ACTION%"=="deps" (
    echo [START] Checking dependencies in %REA_DIR%...
    call npm run deps:check > "%LOG_FILE%" 2>&1
    set "ERR=!errorlevel!"
    goto REPORT
)

if /i "%ACTION%"=="doctor" (
    echo [START] Running REA doctor diagnostics...
    node scripts\rea.mjs doctor > "%LOG_FILE%" 2>&1
    set "ERR=!errorlevel!"
    goto REPORT
)

if /i "%ACTION%"=="run" (
    shift
    echo [START] Running custom REA command: %*
    node scripts\rea.mjs %* > "%LOG_FILE%" 2>&1
    set "ERR=!errorlevel!"
    goto REPORT
)

echo Usage: rea_runner.bat [build ^| check ^| deps ^| doctor ^| run ^<args...^>]
exit /b 1

:REPORT
if !ERR! equ 0 (
    echo [SUCCESS] Action '%ACTION%' succeeded [Code: 0]
    echo [LOG] Log saved to: %LOG_FILE%
    exit /b 0
) else (
    echo [ERROR] Action '%ACTION%' failed [Code: !ERR!]
    echo [LOG] Full log saved to: %LOG_FILE%
    echo [TAIL] Last 10 lines of output:
    echo ------------------------------------------------------------
    powershell -NoProfile -Command "Get-Content -Path '%LOG_FILE%' -Tail 10 -ErrorAction SilentlyContinue"
    echo ------------------------------------------------------------
    exit /b !ERR!
)

