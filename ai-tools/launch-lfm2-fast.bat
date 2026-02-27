@echo off
REM LFM2-1.2B Quick Launch
REM Your fastest small model for quick tasks

echo.
echo ========================================
echo   LFM2-1.2B - Quick Small Model
echo ========================================
echo.
echo Size: 1.2 GB
echo Expected Speed: 60-100 tokens/second
echo Best for: Quick questions, testing, simple tasks
echo.
echo Starting server on port 8090...
echo.

llama-server -m "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\LFM2-1.2B-Q8_0.gguf" -ngl 99 -c 2048 --batch-size 512 -t 4 --port 8090

pause
