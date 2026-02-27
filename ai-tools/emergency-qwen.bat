@echo off
REM Emergency Qwen Launcher - Bypasses PowerShell profile!
REM Use this if 'qwen' command doesn't work

echo.
echo ========================================
echo   Emergency Qwen Launcher
echo ========================================
echo.

cd /d "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\safe-workspace"

echo Starting Safe Workspace...
echo.

py -3.12 safe_launcher.py

pause
