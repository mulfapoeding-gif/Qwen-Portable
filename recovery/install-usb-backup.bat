@echo off
REM ========================================
REM USB Backup Creator
REM ========================================

echo.
echo ========================================
echo   USB Backup Creator
echo ========================================
echo.
echo This will create a bootable USB backup of your Qwen installation.
echo.
echo Requirements:
echo   - 32GB USB 3.0 drive recommended
echo   - All files will be copied to USB
echo.
pause

echo Available drives:
wmic logicaldisk where "drivetype=2" get deviceid,description,volumename
echo.
set /p USB_LETTER="Enter USB drive letter (e.g., E): "
echo.

SET "USB=%USB_LETTER%:\Qwen-Portable"
SET "BASE=C:\Users\mulfa\Qwen-Portable"

echo Creating USB backup at: %USB%
echo.

echo [1/3] Copying core files...
xcopy "%BASE%\bin" "%USB%\bin" /E /I /Y
xcopy "%BASE%\ai-tools" "%USB%\ai-tools" /E /I /Y
xcopy "%BASE%\config" "%USB%\config" /E /I /Y
xcopy "%BASE%\docs" "%USB%\docs" /E /I /Y
xcopy "%BASE%\recovery" "%USB%\recovery" /E /I /Y
xcopy "%BASE%\sync" "%USB%\sync" /E /I /Y
echo       [OK] Core files copied

echo.
echo [2/3] Copying projects...
xcopy "%BASE%\projects" "%USB%\projects" /E /I /Y
echo       [OK] Projects copied

echo.
echo [3/3] Copying core model...
if exist "%BASE%\models\qwen\Qwen2.5-Coder-3B-Instruct-Q4_K_M.gguf" (
    mkdir "%USB%\models\qwen"
    copy "%BASE%\models\qwen\Qwen2.5-Coder-3B-Instruct-Q4_K_M.gguf" "%USB%\models\qwen\"
    echo       [OK] Core model copied
) else (
    echo       [INFO] Core model not found, skipping
)

echo.
echo Copying README files...
copy "%BASE%\README.md" "%USB%\"

echo.
echo ========================================
echo   USB Backup Complete!
echo ========================================
echo.
echo USB contents:
echo   - All code and tools
echo   - Configuration files
echo   - Active projects
echo   - 1 core model: Qwen2.5-Coder-3B
echo.
echo Total size: ~8-10 GB
echo.
echo To use:
echo   1. Safely eject USB
echo   2. Plug into any PC with Python + LM Studio
echo   3. Run: bin\qwen.bat
echo.
pause
