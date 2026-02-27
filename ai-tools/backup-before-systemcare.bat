@echo off
REM Backup AI Tools Configuration
REM Run this BEFORE using Advanced SystemCare

echo.
echo ========================================
echo   AI Tools - Configuration Backup
echo ========================================
echo.
echo Backing up critical files...
echo.

set BACKUP_DIR=%USERPROFILE%\ai-tools-backup-%DATE:~-4%%DATE:~3,2%%DATE:~0,2%
mkdir "%BACKUP_DIR%" 2>nul

REM PowerShell Profile
if exist "%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1" (
    copy "%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1" "%BACKUP_DIR%"
    echo [OK] PowerShell profile backed up
)

REM Ollama config
if exist "%USERPROFILE%\.ollama\.env" (
    copy "%USERPROFILE%\.ollama\.env" "%BACKUP_DIR%"
    echo [OK] Ollama config backed up
)

REM LM Studio settings
if exist "%USERPROFILE%\.lmstudio\settings.json" (
    copy "%USERPROFILE%\.lmstudio\settings.json" "%BACKUP_DIR%"
    echo [OK] LM Studio settings backed up
)

REM User model configs
if exist "%USERPROFILE%\.lmstudio\user-model-configs\" (
    xcopy "%USERPROFILE%\.lmstudio\user-model-configs\" "%BACKUP_DIR%\user-model-configs\" /E /I
    echo [OK] Model configs backed up
)

REM AI tools scripts
if exist "%USERPROFILE%\.lmstudio\models\imported-models\uncategorized\ai-tools\" (
    xcopy "%USERPROFILE%\.lmstudio\models\imported-models\uncategorized\ai-tools\" "%BACKUP_DIR%\ai-tools\" /E /I
    echo [OK] AI tools scripts backed up
)

echo.
echo ========================================
echo   Backup Complete!
echo ========================================
echo.
echo Backup location:
echo %BACKUP_DIR%
echo.
echo You can now safely run Advanced SystemCare.
echo If anything breaks, run: restore-ai-tools.bat
echo.
pause
