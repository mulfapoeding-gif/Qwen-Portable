@echo off
REM Qwen Orchestrator - Visual Task Display Demo
REM Shows all task indicators and acknowledgments

echo.
echo ========================================
echo   Qwen Orchestrator - Visual Display
echo ========================================
echo.
echo This shows:
echo   - Task acknowledgments (✅)
echo   - Progress bars [████░░░░]
echo   - Spinners (⠋ ⠙ ⠹...)
echo   - Mode indicators (🟡 🟢 🔵 🔴)
echo   - Command history
echo   - Task completion
echo.
echo Mostly for indication on tasking!
echo.

py -3.12 "%~dp0qwen-orchestrator-display.py"

pause
