# Qwen Agent - PowerShell Profile Installer
# Run this script once to add 'qwen' command to PowerShell

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Qwen Agent - PowerShell Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$profilePath = $PROFILE.CurrentUserCurrentHost
$scriptPath = "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\safe-workspace\safe_launcher.py"

Write-Host "Profile path: $profilePath`n"

# Check if profile exists
if (-not (Test-Path $profilePath)) {
    Write-Host "Creating PowerShell profile..." -ForegroundColor Yellow
    New-Item -Path $profilePath -ItemType File -Force | Out-Null
    Write-Host "Profile created`n" -ForegroundColor Green
}

# Add the SAFE workspace function to profile
Write-Host "Adding SAFE 'qwen' function to profile..." -ForegroundColor Yellow

$qwenFunction = @"

# ============================================
# Qwen Agent - SAFE WORKSPACE (Auto-added)
# ============================================
function qwen {
    `$env:SAFE_WORKSPACE = "C:`Users`mulfa`.lmstudio`models`imported-models`uncategorized`safe-workspace"
    
    # Check if LM Studio is running
    try {
        `$response = Invoke-WebRequest -Uri "http://localhost:1234/v1/models" -TimeoutSec 2 -ErrorAction Stop
        Write-Host "`n[OK] LM Studio server detected`n" -ForegroundColor Green
    } catch {
        Write-Host "`n[WARNING] LM Studio server not detected!" -ForegroundColor Yellow
        Write-Host "Please start LM Studio server:`n"
        Write-Host "  1. Open LM Studio"
        Write-Host "  2. Load a model"
        Write-Host "  3. Start Local Server`n"
        Write-Host "  Type 'continue' to run anyway, or Ctrl+C to cancel"
        `$response = Read-Host
        if (`$response -ne 'continue') { return }
    }
    
    # Change to safe workspace and run
    Set-Location `$env:SAFE_WORKSPACE
    Write-Host "`n[SAFE WORKSPACE] Protected environment active`n" -ForegroundColor Green
    py -3.12 safe_launcher.py
}

# Short alias
Set-Alias -Name q -Value qwen -Force

# Backup utilities function
function qwen-backup {
    Set-Location "C:`Users`mulfa`.lmstudio`models`imported-models`uncategorized`safe-workspace"
    py -3.12 backup_restore.py
}

# Git undo function
function qwen-undo {
    Set-Location "C:`Users`mulfa`.lmstudio`models`imported-models`uncategorized`safe-workspace"
    Write-Host "`n[Git] Undoing last change..." -ForegroundColor Cyan
    git reset --soft HEAD~1
    Write-Host "[Git] Done! Changes preserved but unstaged.`n" -ForegroundColor Green
}
"@

# Remove old qwen function if exists
$content = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
if ($content -like "*function qwen*") {
    Write-Host "Removing old 'qwen' function..." -ForegroundColor Yellow
    # Remove the old function
    $lines = Get-Content $profilePath
    $newLines = @()
    $skip = $false
    foreach ($line in $lines) {
        if ($line -like "*function qwen*") { $skip = $true }
        if ($skip -and $line -like "*Set-Alias -Name q*") { $skip = $false; continue }
        if (-not $skip) { $newLines += $line }
    }
    $newLines | Set-Content $profilePath
    Write-Host "Old function removed`n" -ForegroundColor Green
}

# Append new function
Add-Content -Path $profilePath -Value $qwenFunction
Write-Host "'qwen' function added to profile`n" -ForegroundColor Green

# Reload profile
Write-Host "Reloading profile..." -ForegroundColor Yellow
. $profilePath
Write-Host "Profile reloaded`n" -ForegroundColor Green

# Test
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================`n"

Write-Host "You can now use:" -ForegroundColor White
Write-Host "  qwen         - Safe workspace (recommended)" -ForegroundColor Cyan
Write-Host "  q            - Short alias" -ForegroundColor Cyan
Write-Host "  qwen-backup  - Backup utilities" -ForegroundColor Cyan
Write-Host "  qwen-undo    - Undo last change`n" -ForegroundColor Cyan

Write-Host "NEW PowerShell windows will have these commands automatically."
Write-Host "Open a new window and type 'qwen' to start!`n"
