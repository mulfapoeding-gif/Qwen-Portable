@echo off
REM LM Studio Full Settings Access
REM Opens LM Studio with all settings accessible

echo.
echo ========================================
echo   LM Studio - Full Access
echo ========================================
echo.
echo LM Studio is already installed!
echo.
echo Location: C:\Users\mulfa\.lmstudio\
echo CLI: C:\Users\mulfa\.lmstudio\bin\lms.exe
echo.
echo Opening LM Studio...
echo.

REM Try to launch LM Studio
start "" "lmstudio.exe" 2>nul

if errorlevel 1 (
    echo [INFO] LM Studio GUI not found in PATH.
    echo.
    echo Try these:
    echo 1. Press Windows Key
    echo 2. Type "LM Studio"
    echo 3. Press Enter
    echo.
)

echo.
echo ========================================
echo   LM Studio Settings Access
echo ========================================
echo.
echo In LM Studio:
echo   1. Click gear icon ⚙️ (Settings)
echo   2. Access all settings:
echo      - Model Settings
echo      - Server Settings  
echo      - Advanced Settings
echo      - Developer Options
echo.
echo CLI Commands:
echo   lms ls              - List models
echo   lms load MODEL      - Load model
echo   lms server start    - Start server
echo   lms server status   - Check status
echo   lms chat MODEL      - Interactive chat
echo   lms runtime survey  - GPU info
echo.

pause
