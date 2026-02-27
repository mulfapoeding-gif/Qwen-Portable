# LM Studio Settings Optimizer for Quadro P1000
# This script modifies LM Studio settings.json for optimal GPU usage

$settingsPath = "$env:USERPROFILE\.lmstudio\settings.json"

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  LM Studio Settings Optimizer" -ForegroundColor Cyan
Write-Host "  For: NVIDIA Quadro P1000 (4GB VRAM)" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Check if settings file exists
if (-not (Test-Path $settingsPath)) {
    Write-Host "[ERROR] Settings file not found at: $settingsPath" -ForegroundColor Red
    Write-Host "Please open LM Studio at least once to create the settings file.`n" -ForegroundColor Yellow
    exit 1
}

# Load current settings
Write-Host "[1/4] Loading current settings..." -ForegroundColor Yellow
$settings = Get-Content $settingsPath -Raw | ConvertFrom-Json

# Backup current settings
$backupPath = "$settingsPath.backup.$(Get-Date -Format 'yyyyMMdd-HHmmss')"
Copy-Item $settingsPath $backupPath
Write-Host "  [OK] Backup created: $backupPath" -ForegroundColor Green

# Modify settings for Quadro P1000
Write-Host "`n[2/4] Applying optimized settings..." -ForegroundColor Yellow

# Set default context length to 4096 (optimal for 4GB VRAM)
$settings.defaultContextLength = @{
    type = "custom"
    value = 4096
}
Write-Host "  [OK] Context length: 4096" -ForegroundColor Green

# Enable developer mode for more control
$settings.developerMode = $true
Write-Host "  [OK] Developer mode: Enabled" -ForegroundColor Green

# Show experimental features (for advanced GPU controls)
$settings.developer.showExperimentalFeatures = $true
Write-Host "  [OK] Experimental features: Enabled" -ForegroundColor Green

# Configure JIT model settings
$settings.developer.jitModelTTL = @{
    enabled = $true
    ttlSeconds = 3600  # Keep model loaded for 1 hour
}
Write-Host "  [OK] Model TTL: 1 hour" -ForegroundColor Green

# Unload previous model when loading new one (save VRAM)
$settings.chat.unloadPreviousModelOnSelect = $true
Write-Host "  [OK] Auto-unload previous model: Enabled" -ForegroundColor Green

# Configure model loading guardrails for 4GB VRAM
$settings.modelLoadingGuardrails = @{
    mode = "custom"
    customThresholdBytes = 4294967296  # 4GB
    alwaysAllowLoadAnyway = $false
}
Write-Host "  [OK] VRAM guardrail: 4GB" -ForegroundColor Green

# Save updated settings
Write-Host "`n[3/4] Saving settings..." -ForegroundColor Yellow
$settings | ConvertTo-Json -Depth 100 | Set-Content $settingsPath -Encoding UTF8
Write-Host "  [OK] Settings saved to: $settingsPath" -ForegroundColor Green

# Create per-model configuration file
Write-Host "`n[4/4] Creating per-model GPU config..." -ForegroundColor Yellow

$modelConfigDir = "$env:USERPROFILE\.lmstudio\user-model-configs"
if (-not (Test-Path $modelConfigDir)) {
    New-Item -ItemType Directory -Path $modelConfigDir -Force | Out-Null
}

# Create config for Qwen Coder Unlimited
$modelConfig = @{
    "imported-models/uncategorized/qwen-coder-unlimited*" = @{
        "gpu_layers" = 99  # Max GPU layers for P1000
        "context_length" = 4096
        "batch_size" = 512
        "flash_attn" = $false  # Not supported on Pascal
        "n_threads" = 4  # Use 4 CPU threads
    }
}

$modelConfigPath = "$modelConfigDir\gpu-config.json"
$modelConfig | ConvertTo-Json -Depth 10 | Set-Content $modelConfigPath -Encoding UTF8
Write-Host "  [OK] Model config created: $modelConfigPath" -ForegroundColor Green

# Summary
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Optimization Complete!" -ForegroundColor Green
Write-Host "========================================`n"

Write-Host "Settings Applied:" -ForegroundColor White
Write-Host "  [OK] Context Length: 4096" -ForegroundColor Green
Write-Host "  [OK] Developer Mode: Enabled" -ForegroundColor Green
Write-Host "  [OK] Experimental Features: Enabled" -ForegroundColor Green
Write-Host "  [OK] Model TTL: 1 hour" -ForegroundColor Green
Write-Host "  [OK] VRAM Guardrail: 4GB" -ForegroundColor Green
Write-Host "  [OK] Per-model GPU config: Created" -ForegroundColor Green

Write-Host "`nNext Steps:" -ForegroundColor White
Write-Host "  1. RESTART LM Studio (close completely and reopen)" -ForegroundColor Yellow
Write-Host "  2. Load your model: imported-models/uncategorized/qwen-coder-unlimited.Q4_K_M.gguf" -ForegroundColor Gray
Write-Host "  3. In Model Settings, verify:" -ForegroundColor Gray
Write-Host "     - GPU Offload: Should be near MAX" -ForegroundColor Gray
Write-Host "     - Context: 4096" -ForegroundColor Gray
Write-Host "     - Batch Size: 512" -ForegroundColor Gray

Write-Host "`nBackup Location:" -ForegroundColor White
Write-Host "  $backupPath" -ForegroundColor Gray
Write-Host "  (Restore by copying back to settings.json)`n" -ForegroundColor Gray
