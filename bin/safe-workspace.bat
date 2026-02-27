@echo off
REM ========================================
REM Safe Workspace - Direct Launcher
REM Uses relative paths for portability
REM ========================================

echo.
echo ========================================
echo   Safe Workspace - AI Agent Environment
echo ========================================
echo.

REM Get the directory where this script is located
SET "SCRIPT_DIR=%~dp0"
SET "BASE_DIR=%SCRIPT_DIR%.."
SET "SAFE_WORKSPACE=%BASE_DIR%\ai-tools\safe-workspace"

REM Change to safe workspace and run
cd /d "%SAFE_WORKSPACE%"
py -3.12 safe_launcher.py

echo.
pause
