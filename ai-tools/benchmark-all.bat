@echo off
REM Benchmark All Models - Before/After Optimization
REM Tests speed of original vs quantized models

echo.
echo ========================================
echo   Benchmark All Models
echo ========================================
echo.

set MODELS_DIR=C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized
cd /d "%MODELS_DIR%"

echo This will benchmark all GGUF models.
echo Each test takes ~30 seconds.
echo.
pause

for %%f in (*.gguf) do (
    echo.
    echo ========================================
    echo Benchmarking: %%f
    echo ========================================
    echo.
    
    REM Run benchmark (30 tokens for speed)
    llama-bench -m "%%f" -ngl 99 -t 8 -b 512 --tensor-split 1 -n 30 2>&1 | findstr /C:"tokens/s"
    
    echo.
)

echo ========================================
echo   Benchmark Complete!
echo ========================================
echo.
echo Compare tokens/s values:
echo - Higher = Faster
echo - Q4_K_M should be 2x faster than original
echo - Q2_K should be 3-4x faster than original
echo.
pause
