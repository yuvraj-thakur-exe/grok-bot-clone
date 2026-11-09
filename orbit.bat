@echo off
setlocal
set "ORBIT_ROOT=%~dp0"
set "PYTHONPATH=%ORBIT_ROOT%src;%PYTHONPATH%"
where py >nul 2>nul
if not errorlevel 1 goto use_py
where python >nul 2>nul
if not errorlevel 1 goto use_python
echo ORBIT requires Python 3.11 or newer. Install Python or uv, then rerun.
exit /b 9009

:use_py
py -3 -m orbit_cli %*
exit /b %errorlevel%

:use_python
python -m orbit_cli %*
exit /b %errorlevel%
