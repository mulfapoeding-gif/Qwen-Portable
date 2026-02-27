@echo off
REM Aider launcher for LM Studio
REM Usage: aider-lmstudio [model-name] [additional args]

set LMSTUDIO_API_BASE=http://localhost:1234/v1
set LMSTUDIO_API_KEY=not-needed

if "%~1"=="" (
    echo Starting Aider with LM Studio...
    echo.
    echo Make sure LM Studio server is running on http://localhost:1234
    echo.
    py -3.12 -m aider --openai-api-base %LMSTUDIO_API_BASE% --openai-api-key %LMSTUDIO_API_KEY% %*
) else (
    py -3.12 -m aider --openai-api-base %LMSTUDIO_API_BASE% --openai-api-key %LMSTUDIO_API_KEY% %*
)
