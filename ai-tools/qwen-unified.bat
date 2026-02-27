@echo off
REM QWEN PRO - Unified AI Orchestrator
REM One window for everything!

echo.
echo ========================================
echo   QWEN PRO - Unified Orchestrator
echo ========================================
echo.
echo One window for everything:
echo   - Task execution
echo   - Progress indicators
echo   - Command history
echo   - Mode switching
echo   - Status monitoring
echo.
echo Starting...
echo.

cd /d "%~dp0"
py -3.12 qwen-unified.py

pause
