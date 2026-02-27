@echo off
REM LM Studio - Apply Optimized Settings for Quadro P1000
REM Uses lms CLI to configure GPU settings

echo.
echo ========================================
echo   LM Studio - GPU Optimization
echo   For: NVIDIA Quadro P1000 (4GB VRAM)
echo ========================================
echo.

echo [1/3] Checking current model status...
lms ps
echo.

echo [2/3] Unloading current model (if loaded)...
lms unload imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf 2>nul
echo.

echo [3/3] Reloading with optimized settings...
echo.
echo NOTE: LM Studio CLI doesn't expose all GPU settings yet.
echo.
echo Please apply these MANUALLY in LM Studio GUI:
echo.
echo   1. Open LM Studio
echo   2. Go to Settings ^> Model Settings
echo   3. Set GPU Offload to MAX (slide all the way right)
echo   4. Set Context Length to 4096
echo   5. Set Batch Size to 512
echo.
echo Then load your model:
echo   lms load imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf
echo.

echo ========================================
echo   Ollama Settings (Already Applied)
echo ========================================
echo   OLLAMA_MAX_VRAM=4294967296   (4GB)
echo   OLLAMA_NUM_GPU=99            (All layers)
echo   OLLAMA_GPU_LAYERS=99
echo   OLLAMA_CONTEXT_LENGTH=4096
echo   OLLAMA_BATCH_SIZE=512
echo.
echo   File: %USERPROFILE%\.ollama\.env
echo.

echo Done!
echo.
pause
