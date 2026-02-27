@echo off
REM Task Planner - Break down complex tasks
REM Usage: plan-task "your project goal"

if "%~1"=="" (
    echo.
    echo ========================================
    echo   Task Planner - Project Decomposition
    echo ========================================
    echo.
    echo Usage:
    echo   plan-task "your project goal"
    echo.
    echo Examples:
    echo   plan-task "Build a web scraper for news sites"
    echo   plan-task "Create a Python API client"
    echo   plan-task "Make a Gradio dashboard"
    echo.
    exit /b 1
)

py -3.12 "%~dp0task_planner.py" %*
