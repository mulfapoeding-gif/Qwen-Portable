@echo off
REM Bodaay's HuggingFace Model Downloader
REM Enhanced version with progress bars
REM Based on: https://github.com/bodaay/HuggingFaceModelDownloader

echo.
echo ========================================
echo   Bodaay's HuggingFace Model Downloader
echo ========================================
echo.
echo Usage:
echo   hf-download-bodaay MODEL_ID [options]
echo.
echo Examples:
echo   hf-download-bodaay Nerdsking/Nerdsking-python-coder-7B-i
echo   hf-download-bodaay microsoft/phi-2 -f gguf
echo   hf-download-bodaay --login
echo.
echo Options:
echo   -o OUTPUT   Output directory
echo   -f FILTER   File filter (default: gguf)
echo   -l          Login to HuggingFace
echo.

if "%~1"=="" (
    py -3.12 "%~dp0hf-downloader-bodaay.py"
    pause
    exit /b 1
)

py -3.12 "%~dp0hf-downloader-bodaay.py" %*

pause
