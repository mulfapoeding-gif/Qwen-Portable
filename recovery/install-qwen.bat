@echo off
REM ========================================
REM Qwen - Fresh Installation Script
REM ========================================

echo.
echo ========================================
echo   Qwen - Fresh Installation
echo ========================================
echo.

SETLOCAL EnableDelayedExpansion

SET "SCRIPT_DIR=%~dp0"
SET "BASE_DIR=%SCRIPT_DIR%.."

echo Installation directory: %BASE_DIR%
echo.

REM Check Python
echo [Step 1/4] Checking prerequisites...
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Python 3.12 not found!
    echo Please install Python 3.12 from:
    echo   https://www.python.org/downloads/
    pause
    exit /b 1
)
echo       [OK] Python found
py -3.12 --version

REM Check Git
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Git not found!
    echo Please install Git from:
    echo   https://git-scm.com/download/win
    pause
    exit /b 1
)
echo       [OK] Git found
git --version

REM Install PowerShell Profile
echo.
echo [Step 2/4] Installing PowerShell profile...
SET "INSTALL_SCRIPT=%BASE_DIR%\bin\install-profile.ps1"
if exist "%INSTALL_SCRIPT%" (
    powershell -ExecutionPolicy Bypass -File "%INSTALL_SCRIPT%"
    echo       [OK] PowerShell profile installed
) else (
    echo [WARNING] install-profile.ps1 not found
)

REM Initialize Git in Projects
echo.
echo [Step 3/4] Setting up Git in projects...
if not exist "%BASE_DIR%\projects\.git" (
    cd "%BASE_DIR%\projects"
    git init
    echo # Qwen Projects > README.md
    git add README.md
    git commit -m "Initial commit"
    cd "%SCRIPT_DIR%"
    echo       [OK] Git initialized
) else (
    echo       [INFO] Git already initialized
)

REM Create Desktop Shortcut
echo.
echo [Step 4/4] Creating desktop shortcut...
powershell -Command " = New-Object -ComObject WScript.Shell;  = .CreateShortcut('%USERPROFILE%\Desktop\Qwen.lnk'); .TargetPath = '%BASE_DIR%\bin\qwen.bat'; .WorkingDirectory = '%BASE_DIR%\bin'; .Description = 'Qwen AI Workspace'; .Save()"
echo       [OK] Desktop shortcut created

echo.
echo ========================================
echo   Installation Complete!
echo ========================================
echo.
echo Next steps:
echo   1. Close ALL PowerShell windows
echo   2. Open NEW PowerShell window
echo   3. Type: qwen
echo.
echo For USB backup, run:
echo   recovery\install-usb-backup.bat
echo.
pause
