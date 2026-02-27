@echo off
REM ========================================
REM Configuration Validation
REM ========================================

echo.
echo ========================================
echo   Configuration Validator
echo ========================================
echo.

SET "BASE=C:\Users\mulfa\Qwen-Portable"
SET "ERRORS=0"

echo Validating configurations...
echo.

REM Check Python
echo [1/5] Python Installation...
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo     [FAIL] Python 3.12 not installed
    SET /A ERRORS+=1
) else (
    echo     [PASS] Python 3.12 installed
    py -3.12 --version
)

REM Check Git
echo.
echo [2/5] Git Installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo     [FAIL] Git not installed
    SET /A ERRORS+=1
) else (
    echo     [PASS] Git installed
    git --version
)

REM Check LM Studio
echo.
echo [3/5] LM Studio Server...
curl -s http://localhost:1234/v1/models >nul 2>&1
if %errorlevel% neq 0 (
    echo     [INFO] LM Studio not running (will work in plan mode)
) else (
    echo     [PASS] LM Studio server running
)

REM Check safety config
echo.
echo [4/5] Safety Configuration...
if exist "%BASE%\ai-tools\safe-workspace\.safety-config.yml" (
    echo     [PASS] Safety config found
) else (
    echo     [WARN] Safety config missing
    SET /A ERRORS+=1
)

REM Check PowerShell profile
echo.
echo [5/5] PowerShell Profile...
if exist "%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1" (
    echo     [PASS] PowerShell profile exists
) else (
    echo     [INFO] PowerShell profile not found (run install-qwen.bat)
)

echo.
echo ========================================
echo   Validation Results
echo ========================================
echo.
echo Errors: %ERRORS%
echo.
if %ERRORS% GTR 0 (
    echo Action required:
    echo   Run: recovery\install-qwen.bat
) else (
    echo All validations passed!
)

echo.
pause
