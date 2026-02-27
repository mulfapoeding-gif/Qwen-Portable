@echo off
REM Quick View - See the Orchestrator Display
REM Shows what you see when you type 'qwen'

echo.
echo ========================================
echo   Qwen Orchestrator - Quick View
echo ========================================
echo.
echo This is what you see when you type 'qwen':
echo.

cd /d "%~dp0safe-workspace"

echo ╔══════════════════════════════════════════════════════════╗
echo ║     🛡️  Safe Workspace - AI Agent Environment            ║
echo ╠══════════════════════════════════════════════════════════╣
echo ║  Protected Environment:                                  ║
echo ║    + Git auto-commit                                     ║
echo ║    + Automatic backups                                   ║
echo ║    + Protected directories                               ║
echo ║    + Activity logging                                    ║
echo ║                                                          ║
echo ║  Commands:                                               ║
echo ║    - Type your command                                   ║
echo ║    - TAB or 'm' = Toggle mode                            ║
echo ║    - 'backup' = Manual backup                            ║
echo ║    - 'status' = Show status                              ║
echo ║    - 'quit' = Exit                                       ║
echo ╚══════════════════════════════════════════════════════════╝
echo.
echo Example session:
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo >>> [1] create a python function
echo.
echo + ACKNOWLEDGED: [1] "create a python function"
echo   Mode: [AUTO]
echo   Agent: Coder (7B)
echo.
echo [----------------------------------------]   0% Generating code...
echo [############----------------------------]  30%
echo [########################----------------]  60%
echo [########################################] 100%
echo.
echo + Task [1] Complete!
echo.
echo Result:
echo   def hello():
echo       print("Hello, World!")
echo.
echo >>> [2] h
echo.
echo Command History:
echo   [  2] h
echo   [  1] create a python function
echo.
echo >>> [3] r 1
echo.
echo Redo [1]: create a python function
echo.
echo + ACKNOWLEDGED: [3] "create a python function"
echo   Mode: [AUTO]
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo To see it LIVE:
echo   1. Type: qwen
echo   2. Start typing commands
echo   3. Watch the indicators!
echo.
echo Or run the demo:
echo   py -3.12 qwen-orchestrator-display.py
echo.

pause
