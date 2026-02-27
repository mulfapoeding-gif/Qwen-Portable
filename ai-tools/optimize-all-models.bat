@echo off
REM Auto-Optimize All GGUF Models
REM Creates Q4_K_M and Q2_K quantized versions

echo.
echo ========================================
echo   Auto-Optimize All GGUF Models
echo ========================================
echo.

set MODELS_DIR=C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized
cd /d "%MODELS_DIR%"

echo Scanning for GGUF files...
echo.

for %%f in (*.gguf) do (
    echo ========================================
    echo Processing: %%f
    echo ========================================
    
    REM Skip if already quantized
    echo %%f | findstr /i "_Q4_K_M" >nul
    if not errorlevel 1 (
        echo [SKIP] Already Q4_K_M quantized
        goto :next
    )
    
    echo %%f | findstr /i "_Q2_K" >nul
    if not errorlevel 1 (
        echo [SKIP] Already Q2_K quantized
        goto :next
    )
    
    REM Get base name
    for %%n in ("%%f") do set BASENAME=%%~n
    
    REM Create Q4_K_M version (balanced)
    echo.
    echo [1/2] Creating Q4_K_M version...
    echo.
    llama-quantize "%%f" "!BASENAME!_Q4_K_M.gguf" Q4_K_M
    if errorlevel 1 (
        echo [ERROR] Q4_K_M quantization failed
    ) else (
        echo [OK] Q4_K_M created: !BASENAME!_Q4_K_M.gguf
    )
    
    REM Create Q2_K version (fast)
    echo.
    echo [2/2] Creating Q2_K version...
    echo.
    llama-quantize "%%f" "!BASENAME!_Q2_K.gguf" Q2_K
    if errorlevel 1 (
        echo [ERROR] Q2_K quantization failed
    ) else (
        echo [OK] Q2_K created: !BASENAME!_Q2_K.gguf
    )
    
    :next
    echo.
)

echo ========================================
echo   Optimization Complete!
echo ========================================
echo.
echo Next step: Import to Ollama
echo Run: ollama-import-optimized.bat
echo.
pause
