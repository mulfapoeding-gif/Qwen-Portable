@echo off
REM ========================================
REM System Check and Repair
REM ========================================

echo.
echo ========================================
echo   Qwen - System Check and Repair
echo ========================================
echo.

SET "BASE=C:\Users\mulfa\Qwen-Portable"
SET "ISSUES=0"

echo Scanning for issues...
echo.

REM Check directory structure
echo [1/6] Checking directory structure...
if not exist "%BASE%\bin" (
    echo     [MISSING] bin/ directory
    SET /A ISSUES+=1
) else (
    echo     [OK] bin/ directory
)
if not exist "%BASE%\models" (
    echo     [MISSING] models/ directory
    SET /A ISSUES+=1
) else (
    echo     [OK] models/ directory
)
if not exist "%BASE%\ai-tools" (
    echo     [MISSING] ai-tools/ directory
    SET /A ISSUES+=1
) else (
    echo     [OK] ai-tools/ directory
)
if not exist "%BASE%\projects" (
    echo     [MISSING] projects/ directory
    SET /A ISSUES+=1
) else (
    echo     [OK] projects/ directory
)

REM Check README files
echo.
echo [2/6] Checking README files...
if not exist "%BASE%\README.md" (
    echo     [MISSING] Main README.md
    SET /A ISSUES+=1
) else (
    echo     [OK] README.md
)
if not exist "%BASE%\docs\INSTALL-GUIDE.md" (
    echo     [MISSING] INSTALL-GUIDE.md
    SET /A ISSUES+=1
) else (
    echo     [OK] INSTALL-GUIDE.md
)

REM Check scripts
echo.
echo [3/6] Checking scripts...
if not exist "%BASE%\bin\qwen.bat" (
    echo     [MISSING] qwen.bat
    SET /A ISSUES+=1
) else (
    echo     [OK] qwen.bat
)
if not exist "%BASE%\recovery\install-qwen.bat" (
    echo     [MISSING] install-qwen.bat
    SET /A ISSUES+=1
) else (
    echo     [OK] install-qwen.bat
)

REM Check Python
echo.
echo [4/6] Checking Python...
py -3.12 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo     [ERROR] Python 3.12 not found
    SET /A ISSUES+=1
) else (
    echo     [OK] Python 3.12 installed
    py -3.12 --version
)

REM Check Git
echo.
echo [5/6] Checking Git...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo     [ERROR] Git not found
    SET /A ISSUES+=1
) else (
    echo     [OK] Git installed
    git --version
)

REM Check LM Studio
echo.
echo [6/6] Checking LM Studio...
curl -s http://localhost:1234/v1/models >nul 2>&1
if %errorlevel% neq 0 (
    echo     [INFO] LM Studio server not running
) else (
    echo     [OK] LM Studio server detected
)

echo.
echo ========================================
echo   Scan Results
echo ========================================
echo.
echo Issues found: %ISSUES%
echo.
if %ISSUES% GTR 0 (
    echo Recommendations:
    echo   1. Run recovery\install-qwen.bat for fresh install
    echo   2. Run recovery\restore-readmes.bat for missing docs
    echo   3. Check Python/Git installation
) else (
    echo All checks passed! System is healthy.
)

echo.
pause
