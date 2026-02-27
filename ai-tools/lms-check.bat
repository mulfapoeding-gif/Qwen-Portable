@echo off
REM LM Studio - Check and Fix Issues

echo.
echo ========================================
echo   LM Studio - Diagnostic Tool
echo ========================================
echo.

echo [1/5] Checking LM Studio daemon...
lms daemon status
if %errorlevel% neq 0 (
    echo Starting daemon...
    lms daemon up
)
echo.

echo [2/5] Checking server status...
lms server status
if %errorlevel% neq 0 (
    echo Starting server...
    lms server start
)
echo.

echo [3/5] Checking loaded models...
lms ps
echo.

echo [4/5] Checking GPU detection...
lms runtime survey
echo.

echo [5/5] Checking CLI installation...
where lms
echo.

echo ========================================
echo   Diagnostic Complete
echo ========================================
echo.
echo If LM Studio GUI is not opening:
echo.
echo   1. LM Studio CLI works in TERMINAL only
echo      - It does NOT open the GUI
echo      - Use 'lms chat' for terminal chat
echo.
echo   2. To open LM Studio GUI:
echo      - Press Windows key
echo      - Type "LM Studio"
echo      - Press Enter
echo.
echo   3. After GUI opens, your settings are applied:
echo      - Context: 4096
echo      - GPU Offload: Check in Model Settings
echo      - Batch Size: 512
echo.
echo Commands:
echo   lms chat MODEL      - Terminal chat (no GUI)
echo   lms server start    - Start API server
echo   lms load MODEL      - Load model (for server)
echo.

pause
