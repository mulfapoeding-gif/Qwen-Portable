@echo off
REM AI Search - DuckDuckGo Internet Research Tool
REM Usage: ai-search "your search query"

if "%~1"=="" (
    echo.
    echo ========================================
    echo   AI Search - DuckDuckGo Research Tool
    echo ========================================
    echo.
    echo Usage:
    echo   ai-search "your search query"
    echo.
    echo Examples:
    echo   ai-search "python async tutorial"
    echo   ai-search "kotlin coroutines best practices"
    echo   ai-search "android gradle build error fix"
    echo.
    echo Options:
    echo   ai-search-news "topic"  - News search
    echo   ai-search-images "topic" - Image search
    echo   ai-search-help          - Show all options
    echo.
    exit /b 1
)

if "%~1"=="ai-search-help" (
    py -3.12 -m duckduckgo_search text --help
    exit /b 0
)

if "%~1"=="ai-search-news" (
    shift
    py -3.12 -m duckduckgo_search news -k "%*" -m 5
    exit /b 0
)

if "%~1"=="ai-search-images" (
    shift
    py -3.12 -m duckduckgo_search images -k "%*" -m 5
    exit /b 0
)

REM Build the search query from all arguments
setlocal enabledelayedexpansion
set "SEARCH_QUERY="
for %%a in (%*) do (
    if "!SEARCH_QUERY!"=="" (
        set "SEARCH_QUERY=%%a"
    ) else (
        set "SEARCH_QUERY=!SEARCH_QUERY! %%a"
    )
)

REM Run text search with Python 3.12
py -3.12 -m duckduckgo_search text -k "!SEARCH_QUERY!" -m 5
endlocal
