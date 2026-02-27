@echo off
REM Hugging Face Model Downloader
REM Download any model from Hugging Face Hub

echo.
echo ========================================
echo   Hugging Face Model Downloader
echo ========================================
echo.
echo Usage:
echo   hf-download MODEL_ID [OUTPUT_DIR]
echo.
echo Examples:
echo   hf-download Nerdsking/Nerdsking-python-coder-7B-i
echo   hf-download microsoft/phi-2 models/phi-2
echo.
echo This tool:
echo   - Downloads GGUF files from Hugging Face
echo   - Saves to your models folder
echo   - Shows download progress
echo.

if "%~1"=="" (
    echo [ERROR] Please provide a model ID
    echo Example: hf-download Nerdsking/Nerdsking-python-coder-7B-i
    pause
    exit /b 1
)

set MODEL_ID=%1
set OUTPUT_DIR=%~2
if "%OUTPUT_DIR%"=="" set OUTPUT_DIR=C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized

echo.
echo Downloading: %MODEL_ID%
echo To: %OUTPUT_DIR%
echo.

py -3.12 "%~dp0hf-downloader.py" %MODEL_ID% "%OUTPUT_DIR%"

pause
