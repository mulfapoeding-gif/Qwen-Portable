@echo off
REM ========================================
REM Sync from USB Backup (Restore)
REM ========================================

echo.
echo ========================================
echo   Restore from USB Backup
echo ========================================
echo.

REM Detect USB drive
for %%d in (D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    if exist "%%d:\Qwen-Portable\README.md" (
        set USB_DRIVE=%%d:
        goto :found
    )
)

echo [ERROR] No USB backup detected!
echo.
pause
exit /b 1

:found
echo USB backup found at: %USB_DRIVE%
echo.
echo WARNING: This will overwrite files in your PC installation!
echo.
set /p CONFIRM="Type YES to continue: "
if not "%CONFIRM%"=="YES" (
    echo Restore cancelled.
    pause
    exit /b 1
)

echo.
echo Restoring files...
echo.

echo [1/4] Restoring bin...
xcopy "%USB_DRIVE%\Qwen-Portable\bin" "%Base%\bin" /E /I /Y >nul

echo [2/4] Restoring ai-tools...
xcopy "%USB_DRIVE%\Qwen-Portable\ai-tools" "%Base%\ai-tools" /E /I /Y >nul

echo [3/4] Restoring projects...
xcopy "%USB_DRIVE%\Qwen-Portable\projects" "%Base%\projects" /E /I /Y >nul

echo [4/4] Restoring config...
xcopy "%USB_DRIVE%\Qwen-Portable\config" "%Base%\config" /E /I /Y >nul

echo.
echo ========================================
echo   Restore Complete!
echo ========================================
echo.
echo Your PC installation has been restored from USB backup.
echo.
pause
