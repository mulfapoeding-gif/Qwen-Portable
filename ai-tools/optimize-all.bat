@echo off
REM ========================================
REM   AI Tools - Complete Optimization
REM   For: NVIDIA Quadro P1000 (4GB VRAM)
REM ========================================

echo.
echo ========================================
echo   AI Tools - Complete Optimization
echo   Quadro P1000 Edition
echo ========================================
echo.

REM Check if running as admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [WARNING] Not running as Administrator!
    echo.
    echo Some optimizations require admin rights.
    echo.
    choice /C YN /M "Continue without admin features"
    if errorlevel 2 goto :EOF
)

REM 1. Ollama Settings
echo [1/3] Configuring Ollama...
powershell -ExecutionPolicy Bypass -File "%~dp0ai-tools\optimize-performance.ps1"
echo.

REM 2. LM Studio Settings
echo [2/3] Configuring LM Studio...
powershell -ExecutionPolicy Bypass -File "%~dp0ai-tools\configure-lmstudio-settings.ps1"
echo.

REM 3. System Environment (Admin only)
if %1==/admin (
    echo [3/3] Setting system environment variables...
    powershell -ExecutionPolicy Bypass -File "%~dp0ai-tools\optimize-admin.ps1"
) else (
    echo [SKIP] System environment variables (run with /admin for this)
)

echo.
echo ========================================
echo   All Optimizations Complete!
echo ========================================
echo.
echo IMPORTANT: Restart all applications:
echo   1. Close and reopen LM Studio
echo   2. Restart Ollama: ollama serve
echo   3. Restart your terminal
echo.
echo Then test with:
echo   lms runtime survey
echo   lms chat imported-models/uncategorized/qwen-coder-unlimited.Q4_K_M.gguf
echo.
pause
