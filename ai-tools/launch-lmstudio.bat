@echo off
REM Launch LM Studio GUI

echo Starting LM Studio...

REM Try to launch from common locations
if exist "C:\Program Files\LM Studio\LM Studio.exe" (
    start "" "C:\Program Files\LM Studio\LM Studio.exe"
) else if exist "%LOCALAPPDATA%\Programs\lmstudio\LM Studio.exe" (
    start "" "%LOCALAPPDATA%\Programs\lmstudio\LM Studio.exe"
) else (
    echo LM Studio not found in standard locations.
    echo.
    echo Please launch manually:
    echo 1. Press Windows Key
    echo 2. Type "LM Studio"
    echo 3. Press Enter
    echo.
    pause
)
