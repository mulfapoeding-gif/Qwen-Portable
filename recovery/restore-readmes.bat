@echo off
REM ========================================
REM README Files Restore
REM ========================================

echo.
echo ========================================
echo   README Files Restore
echo ========================================
echo.
echo This will restore all missing README files.
echo.
pause

SET "BASE=C:\Users\mulfa\Qwen-Portable"

echo Restoring README files...
echo.

REM Run the documentation creator
if exist "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\CREATE-READMEs-FINAL.ps1" (
    powershell -ExecutionPolicy Bypass -File "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\CREATE-READMEs-FINAL.ps1"
) else if exist "%BASE%\docs\README.md" (
    echo README files already present
) else (
    echo [ERROR] Cannot find README creator script
    echo Please run from original location
)

echo.
pause
