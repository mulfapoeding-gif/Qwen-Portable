@echo off
REM ========================================
REM Sync to USB Backup
REM ========================================

echo.
echo ========================================
echo   Sync to USB Backup
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
echo Please create USB backup first:
echo   recovery\install-usb-backup.bat
echo.
pause
exit /b 1

:found
echo USB backup found at: %USB_DRIVE%
echo.
echo Syncing changes...
echo.

REM Sync files
echo [1/4] Syncing bin...
xcopy "%Base%\bin" "%USB_DRIVE%\Qwen-Portable\bin" /E /I /Y >nul

echo [2/4] Syncing ai-tools...
xcopy "%Base%\ai-tools" "%USB_DRIVE%\Qwen-Portable\ai-tools" /E /I /Y >nul

echo [3/4] Syncing projects...
xcopy "%Base%\projects" "%USB_DRIVE%\Qwen-Portable\projects" /E /I /Y >nul

echo [4/4] Syncing config...
xcopy "%Base%\config" "%USB_DRIVE%\Qwen-Portable\config" /E /I /Y >nul

echo.
echo ========================================
echo   Sync Complete!
echo ========================================
echo.
echo Your USB backup is now up to date.
echo.
pause
