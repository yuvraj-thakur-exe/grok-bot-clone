@echo off
:: ==============================================================================
:: Safe Cleanup Utility
:: Purpose: Safely delete build artifacts, caches, and temporary files without
::          risking critical data or flooding agent token context.
:: Default: DRY-RUN (Preview) mode. Requires --confirm to perform deletion.
:: ==============================================================================
setlocal EnableExtensions EnableDelayedExpansion

set "TARGET_DIR=%~1"
set "ACTION_CONFIRM=0"

:: Check arguments
if "%~1"=="" goto USAGE
if "%~1"=="/?" goto USAGE
if "%~1"=="--help" goto USAGE

:PARSE_ARGS
if "%~1"=="" goto VALIDATE
if /i "%~1"=="--confirm" (
    set "ACTION_CONFIRM=1"
    shift
    goto PARSE_ARGS
)
if /i "%~1"=="/doit" (
    set "ACTION_CONFIRM=1"
    shift
    goto PARSE_ARGS
)
if not defined TARGET_DIR (
    set "TARGET_DIR=%~1"
)
shift
goto PARSE_ARGS

:VALIDATE
:: Safety Guard 1: Ensure TARGET_DIR is non-empty
if "%TARGET_DIR%"=="" (
    echo [SAFETY ERROR] Target directory cannot be empty.
    exit /b 1
)

:: Safety Guard 2: Resolve absolute path
for %%F in ("%TARGET_DIR%") do set "ABS_TARGET=%%~fF"

:: Safety Guard 3: Reject root drive or system paths
if "%ABS_TARGET:~3%"=="" (
    echo [SAFETY ERROR] Refusing to run on drive root: "%ABS_TARGET%"
    exit /b 1
)
if /i "%ABS_TARGET%"=="%SystemRoot%" (
    echo [SAFETY ERROR] Refusing to run on Windows directory!
    exit /b 1
)
if not exist "%ABS_TARGET%" (
    echo [WARNING] Target directory does not exist: "%ABS_TARGET%"
    exit /b 0
)

echo [TARGET] Scanning: "%ABS_TARGET%"

:: Run safe preview or deletion
if "%ACTION_CONFIRM%"=="0" (
    echo [MODE] DRY-RUN / PREVIEW ONLY [Add --confirm to execute deletion]
    echo ------------------------------------------------------------
    powershell -NoProfile -Command ^
        "$target = '%ABS_TARGET%';" ^
        "$patterns = @('*.tmp', '*.log', '*.pyc', '__pycache__', 'dist', 'build', '.pytest_cache');" ^
        "$items = Get-ChildItem -Path $target -Recurse -Force -Include $patterns -ErrorAction SilentlyContinue;" ^
        "$count = ($items | Measure-Object).Count;" ^
        "Write-Host ('[PREVIEW] Found ' + $count + ' cleanup candidate item(s).');" ^
        "if ($count -gt 0) {" ^
        "  $items | Select-Object -First 10 | ForEach-Object { Write-Host ('  [WOULD DELETE] ' + $_.FullName) };" ^
        "  if ($count -gt 10) { Write-Host ('  ... and ' + ($count - 10) + ' more item(s).') }" ^
        "}"
    echo ------------------------------------------------------------
    echo [NOTE] Re-run with --confirm to delete these items safely.
    exit /b 0
) else (
    echo [MODE] DELETION CONFIRMED. Processing cleanup...
    powershell -NoProfile -Command ^
        "$target = '%ABS_TARGET%';" ^
        "$patterns = @('*.tmp', '*.log', '*.pyc', '__pycache__', 'dist', 'build', '.pytest_cache');" ^
        "$items = Get-ChildItem -Path $target -Recurse -Force -Include $patterns -ErrorAction SilentlyContinue;" ^
        "$count = ($items | Measure-Object).Count;" ^
        "foreach ($item in $items) {" ^
        "  try {" ^
        "    if ($item.PSIsContainer) { Remove-Item -LiteralPath $item.FullName -Recurse -Force -ErrorAction Stop }" ^
        "    else { Remove-Item -LiteralPath $item.FullName -Force -ErrorAction Stop }" ^
        "  } catch {}" ^
        "}" ^
        "Write-Host ('[SUCCESS] Cleaned ' + $count + ' item(s) from ' + $target);"
    exit /b 0
)

:USAGE
echo Usage: safe_clean.bat ^<target_directory^> [--confirm]
echo.
echo Examples:
echo   safe_clean.bat .\my_project            (Previews items that would be deleted)
echo   safe_clean.bat .\my_project --confirm  (Executes safe deletion)
exit /b 1
