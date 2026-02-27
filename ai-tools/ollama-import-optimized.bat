@echo off
REM Import Optimized Models to Ollama
REM Creates Ollama models with optimal parameters

echo.
echo ========================================
echo   Import Optimized Models to Ollama
echo ========================================
echo.

set OLLAMA=C:\Users\mulfa\AppData\Local\Programs\Ollama\ollama.exe
set MODELS_DIR=C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized
cd /d "%MODELS_DIR%"

echo Scanning for optimized GGUF files...
echo.

for %%f in (*_Q4_K_M.gguf) do (
    echo ========================================
    echo Importing: %%f
    echo ========================================
    
    REM Get base name without extension
    for %%n in ("%%f") do set BASENAME=%%~n
    
    REM Create model name (lowercase, no special chars)
    set MODELNAME=!BASENAME:_Q4_K_M=!
    set MODELNAME=!MODELNAME: =!
    set MODELNAME=!MODELNAME:.=!
    
    echo.
    echo Creating Modelfile for !MODELNAME!...
    
    (
        echo FROM %%f
        echo.
        echo # Optimal parameters for speed
        echo PARAMETER num_ctx 4096
        echo PARAMETER num_batch 1024
        echo PARAMETER temperature 0.7
        echo PARAMETER top_p 0.9
        echo.
        echo # System prompt for coding
        echo SYSTEM """You are an expert coding assistant. Write clean, efficient code."""
    ) > "Modelfile-!MODELNAME!.txt"
    
    echo.
    echo Creating Ollama model: !MODELNAME!-q4-optimized
    "%OLLAMA%" create "!MODELNAME!-q4-optimized" -f "Modelfile-!MODELNAME!.txt"
    
    if errorlevel 1 (
        echo [ERROR] Import failed
    ) else (
        echo [OK] Created: !MODELNAME!-q4-optimized
    )
    
    echo.
)

echo ========================================
echo   Import Complete!
echo ========================================
echo.
echo Available models:
"%OLLAMA%" list
echo.
echo To run a model:
echo   ollama run MODELNAME
echo.
pause
