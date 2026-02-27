@echo off
REM Quick Launch - Bootes Qwen3 Coder with llama.cpp
REM Fast chatting and tasking!

echo.
echo ========================================
echo   Bootes Qwen3 Coder - Fast Chat
echo ========================================
echo.
echo Model: bootes-qwen3_coder-reasoning-q4_k_m.gguf
echo Size: 4B (FAST!)
echo Expected Speed: 20-35 tokens/second
echo.
echo Starting llama.cpp server...
echo.

"C:\Users\mulfa\AppData\Local\Microsoft\WinGet\Packages\ggml.llamacpp_Microsoft.Winget.Source_8wekyb3d8bbwe\llama-server.exe" ^
  -m "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\bootes-qwen3_coder-reasoning-q4_k_m.gguf" ^
  -ngl 99 ^
  -c 4096 ^
  --batch-size 512 ^
  --port 8080

pause
