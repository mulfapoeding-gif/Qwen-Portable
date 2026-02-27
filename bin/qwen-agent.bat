@echo off
REM Qwen Agent Launcher
REM Quick launcher for the orchestrator

echo.
echo ========================================
echo   Qwen Agent System
echo ========================================
echo.

REM Check if LM Studio is running
curl -s http://localhost:1234/v1/models >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] LM Studio server not detected!
    echo.
    echo Please start LM Studio server:
    echo   1. Open LM Studio
    echo   2. Load a model
    echo   3. Start Local Server
    echo.
    echo Press any key to continue anyway...
    pause >nul
)

REM Run the orchestrator
py -3.12 examples\qwen_orchestrator.py

pause
