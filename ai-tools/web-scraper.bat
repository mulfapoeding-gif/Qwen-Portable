@echo off
REM Web Scraper Tool
REM Usage: web-scraper "url" [search_pattern]

if "%~1"=="" (
    echo.
    echo ========================================
    echo   Web Scraper - Information Gathering
    echo ========================================
    echo.
    echo Usage:
    echo   web-scraper "url"
    echo   web-scraper "url" "pattern"
    echo.
    echo Examples:
    echo   web-scraper "https://docs.python.org/3/tutorial"
    echo   web-scraper "https://github.com/example/repo" "python"
    echo.
    exit /b 1
)

py -3.12 "%~dp0web_scraper.py" %*
