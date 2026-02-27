@echo off
REM ========================================
REM Qwen Agent - Safe Workspace Launcher
REM Uses relative paths for portability
REM ========================================

echo.
echo ========================================
echo   Qwen Agent - Safe Workspace
echo ========================================
echo.

REM Get the directory where this script is located
SET "SCRIPT_DIR=%~dp0"
SET "BASE_DIR=%SCRIPT_DIR%.."
SET "SAFE_WORKSPACE=%BASE_DIR%\ai-tools\safe-workspace"

REM Check if LM Studio is running
echo Checking LM Studio server...
curl -s http://localhost:1234/v1/models >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] LM Studio server not detected!
    echo.
    echo Please start LM Studio server:
    echo   1. Open LM Studio
    echo   2. Load a model
    echo   3. Start Local Server
    echo.
    echo Type 'continue' to run anyway, or Ctrl+C to cancel
    set /p RESPONSE="> "
    if not "%RESPONSE%"=="continue" exit /b 1
) else (
    echo       [OK] LM Studio server detected
)

REM Change to safe workspace and run
echo.
echo Starting Safe Workspace...
cd /d "%SAFE_WORKSPACE%"
py -3.12 safe_launcher.py

echo.
pause
