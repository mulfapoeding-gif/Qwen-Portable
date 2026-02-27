@echo off
REM Quick Launch Optimized Models
REM One-click launch for each optimized model

:menu
cls
echo.
echo ========================================
echo   Launch Optimized Models
echo ========================================
echo.
echo Select model to launch:
echo.
echo [1] CodeLlama 8B - Q4_K_M (Balanced)
echo [2] CodeLlama 8B - Q2_K (Fastest)
echo [3] Qwen3 4B - Q4_K_M (Balanced)
echo [4] Qwen3 4B - Q2_K (Fastest)
echo [5] Qwen 1.5B - Q4_K_M (Super Fast)
echo [6] Qwen 1.5B - Q2_K (Fastest)
echo [0] Exit
echo.
set /p choice="Enter choice: "

if "%choice%"=="1" goto codellama_q4
if "%choice%"=="2" goto codellama_q2
if "%choice%"=="3" goto qwen3_q4
if "%choice%"=="4" goto qwen3_q2
if "%choice%"=="5" goto qwen_q4
if "%choice%"=="6" goto qwen_q2
if "%choice%"=="0" goto end

goto menu

:codellama_q4
echo.
echo Starting CodeLlama 8B Q4_K_M...
llama-server -m "mycopilot-codellama.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8080
goto menu

:codellama_q2
echo.
echo Starting CodeLlama 8B Q2_K...
llama-server -m "mycopilot-codellama_Q2_K.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8081
goto menu

:qwen3_q4
echo.
echo Starting Qwen3 4B Q4_K_M...
llama-server -m "bootes-qwen3_coder-reasoning-q4_k_m.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8082
goto menu

:qwen3_q2
echo.
echo Starting Qwen3 4B Q2_K...
llama-server -m "bootes-qwen3_coder-reasoning-q4_k_m_Q2_K.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8083
goto menu

:qwen_q4
echo.
echo Starting Qwen 1.5B Q4_K_M...
llama-server -m "qwen-coder-unlimited.q4_k_m.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8084
goto menu

:qwen_q2
echo.
echo Starting Qwen 1.5B Q2_K...
llama-server -m "qwen-coder-unlimited.q4_k_m_Q2_K.gguf" -ngl 99 -c 4096 --batch-size 1024 --port 8085
goto menu

:end
echo.
echo Goodbye!
echo.
