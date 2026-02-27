@echo off
REM Qwen AI Orchestrator Pro
REM Multi-model AI team with tools

echo.
echo ========================================
echo   Qwen AI Orchestrator Pro
echo ========================================
echo.

cd /d "%~dp0"

REM Run the orchestrator
py -3.12 orchestrator.py

pause
