@echo off
REM Restore AI Tools Configuration
REM Run this AFTER Advanced SystemCare if something breaks

echo.
echo ========================================
echo   AI Tools - Configuration Restore
echo ========================================
echo.

REM Find latest backup
set BACKUP_DIR=%USERPROFILE%\ai-tools-backup-*

if not exist "%BACKUP_DIR%" (
    echo [ERROR] No backup found!
    echo Please run backup-before-systemcare.bat FIRST
    pause
    exit /b 1
)

echo Restoring from: %BACKUP_DIR%
echo.

REM PowerShell Profile
if exist "%BACKUP_DIR%\Microsoft.PowerShell_profile.ps1" (
    copy "%BACKUP_DIR%\Microsoft.PowerShell_profile.ps1" "%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\" /Y
    echo [OK] PowerShell profile restored
)

REM Ollama config
if exist "%BACKUP_DIR%\.ollama\.env" (
    copy "%BACKUP_DIR%\.ollama\.env" "%USERPROFILE%\.ollama\" /Y
    echo [OK] Ollama config restored
)

REM LM Studio settings
if exist "%BACKUP_DIR%\settings.json" (
    copy "%BACKUP_DIR%\settings.json" "%USERPROFILE%\.lmstudio\" /Y
    echo [OK] LM Studio settings restored
)

REM User model configs
if exist "%BACKUP_DIR%\user-model-configs\" (
    xcopy "%BACKUP_DIR%\user-model-configs\" "%USERPROFILE%\.lmstudio\user-model-configs\" /E /I /Y
    echo [OK] Model configs restored
)

REM AI tools scripts
if exist "%BACKUP_DIR%\ai-tools\" (
    xcopy "%BACKUP_DIR%\ai-tools\" "%USERPROFILE%\.lmstudio\models\imported-models\uncategorized\ai-tools\" /E /I /Y
    echo [OK] AI tools scripts restored
)

echo.
echo ========================================
echo   Restore Complete!
echo ========================================
echo.
echo IMPORTANT: Restart PowerShell for changes to apply.
echo.
pause
