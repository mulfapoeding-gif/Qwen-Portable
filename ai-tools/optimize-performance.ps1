# AI Tools Performance Optimizer
# For NVIDIA Quadro P1000 on Windows 11
# ============================================

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  AI Tools - Performance Optimizer" -ForegroundColor Cyan
Write-Host "  For: NVIDIA Quadro P1000 (4GB VRAM)" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# 1. Set Ollama Environment Variables
Write-Host "[1/4] Configuring Ollama..." -ForegroundColor Yellow

$ollamaEnvPath = "$env:USERPROFILE\.ollama\.env"
$ollamaEnvContent = @"
# Ollama Environment for Quadro P1000
OLLAMA_MAX_VRAM=4294967296
OLLAMA_NUM_GPU=99
OLLAMA_GPU_LAYERS=99
OLLAMA_CONTEXT_LENGTH=4096
OLLAMA_BATCH_SIZE=512
OLLAMA_KEEP_ALIVE=24h
"@

if (Test-Path $ollamaEnvPath) {
    Write-Host "  [OK] Ollama .env exists" -ForegroundColor Green
} else {
    Set-Content -Path $ollamaEnvPath -Value $ollamaEnvContent
    Write-Host "  [OK] Created Ollama .env file" -ForegroundColor Green
}

# 2. Set System Environment Variables (User level)
Write-Host "`n[2/4] Setting system environment variables..." -ForegroundColor Yellow

[Environment]::SetEnvironmentVariable("OLLAMA_MAX_VRAM", "4294967296", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_GPU", "99", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_GPU_LAYERS", "99", "User")
Write-Host "  [OK] Environment variables set" -ForegroundColor Green

# 3. LM Studio Reminder
Write-Host "`n[3/4] LM Studio Settings (manual):" -ForegroundColor Yellow
Write-Host "  Open LM Studio - Settings - Model Settings" -ForegroundColor White
Write-Host "  - GPU Offload: MAX (slide all the way right)" -ForegroundColor Gray
Write-Host "  - Context Length: 4096" -ForegroundColor Gray
Write-Host "  - Batch Size: 512" -ForegroundColor Gray
Write-Host "  - Model: Use Q4_K_M quantization" -ForegroundColor Gray

# 4. Driver Check
Write-Host "`n[4/4] Checking NVIDIA Driver..." -ForegroundColor Yellow

$gpu = Get-WmiObject Win32_VideoController | Where-Object { $_.Name -like "*NVIDIA*" }
if ($gpu) {
    Write-Host "  [OK] GPU Detected: $($gpu.Name)" -ForegroundColor Green
    Write-Host "      Driver Version: $($gpu.DriverVersion)" -ForegroundColor Gray
    Write-Host "`n  Driver Type Check:" -ForegroundColor Cyan
    Write-Host "      Open NVIDIA Control Panel - Help - Check for Updates" -ForegroundColor Gray
    Write-Host "      If offered Studio Driver, install it (more stable than Game Ready)" -ForegroundColor Gray
} else {
    Write-Host "  [!] No NVIDIA GPU detected" -ForegroundColor Yellow
}

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Optimization Complete!" -ForegroundColor Green
Write-Host "========================================`n"

Write-Host "Next Steps:" -ForegroundColor White
Write-Host "  1. Restart Ollama: ollama serve (in new terminal)" -ForegroundColor Gray
Write-Host "  2. Apply LM Studio settings manually (see above)" -ForegroundColor Gray
Write-Host "  3. Test speed: Type /count in LM Studio chat" -ForegroundColor Gray
Write-Host "  4. Download recommended models:" -ForegroundColor Gray
Write-Host "     - Qwen2.5-Coder-3B-Instruct-Q4_K_M (fast)" -ForegroundColor Gray
Write-Host "     - Qwen2.5-7B-Instruct-Q4_K_M (balanced)" -ForegroundColor Gray

Write-Host "`nExpected Performance:" -ForegroundColor White
Write-Host "  3B model: ~15-20 tokens/second" -ForegroundColor Gray
Write-Host "  7B model: ~5-8 tokens/second" -ForegroundColor Gray
Write-Host "  7B Q2_K:  ~10-12 tokens/second" -ForegroundColor Gray

Write-Host "`nDone!`n" -ForegroundColor Green
