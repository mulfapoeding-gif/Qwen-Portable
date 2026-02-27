@echo off
REM llama.cpp Server Launcher for Your Models
REM Fast GGUF inference with Vulkan GPU acceleration

echo.
echo ========================================
echo   llama.cpp Server - Fast Inference
echo ========================================
echo.

REM Set model path
set MODEL_PATH=C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\mycopilot-codellama.gguf

echo Starting llama.cpp server...
echo Model: mycopilot-codellama.gguf (8B)
echo GPU: Quadro P1000 (Vulkan)
echo.

REM Start server with GPU acceleration
llama-server -m "%MODEL_PATH%" -ngl 99 -c 4096 --host 0.0.0.0 --port 8080

pause
