@echo off
REM GLM Model - Fast Inference Launcher
REM Optimized for your Quadro P1000 GPU

echo.
echo ========================================
echo   GLM Model - Fast Inference
echo ========================================
echo.
echo Model: zai-org/GLM-5
echo Optimizations:
echo   - GPU acceleration (CUDA)
echo   - FP16 precision (2x faster)
echo   - Low CPU memory usage
echo   - Optimized pipeline
echo.
echo Starting...
echo.

py -3.12 "%~dp0glm-fast-inference.py"

pause
