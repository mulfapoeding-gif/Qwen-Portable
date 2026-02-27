@echo off
REM QWEN PRO - Unified Orchestrator with Ollama + llama.cpp
REM ONE WINDOW FOR EVERYTHING!

echo.
echo ========================================
echo   QWEN PRO - Full Unified Orchestrator
echo ========================================
echo.
echo Includes:
echo   - Qwen AI Orchestrator
echo   - Ollama Integration
echo   - llama.cpp Integration
echo   - All models
echo   - All tools
echo.
echo Starting...
echo.

cd /d "%~dp0"
py -3.12 qwen-unified-full.py

pause
