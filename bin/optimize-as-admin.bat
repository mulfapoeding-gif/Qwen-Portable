@echo off
REM AI Tools - Optimize as Admin
REM Runs the optimizer with Administrator privileges

echo.
echo ========================================
echo   AI Tools - Performance Optimizer
echo   Running as Administrator
echo ========================================
echo.

powershell -Command "Start-Process PowerShell -ArgumentList '-ExecutionPolicy Bypass -File \"%~dp0ai-tools\optimize-admin.ps1\"' -Verb RunAs"

echo.
echo Launched optimizer as Administrator!
echo.
pause
