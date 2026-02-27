# Qwen Agent - PowerShell Profile Installer
# Run this script once to add 'qwen' command to PowerShell

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Qwen Agent - PowerShell Setup" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$profilePath = $PROFILE.CurrentUserCurrentHost
$toolsPath = "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools"
$workspacePath = "$toolsPath\safe-workspace"
$examplesPath = "$toolsPath\examples"
$docsPath = "$toolsPath\docs"

Write-Host "Profile path: $profilePath`n"
Write-Host "Tools path: $toolsPath`n"

# Check if profile exists
if (-not (Test-Path $profilePath)) {
    Write-Host "Creating PowerShell profile..." -ForegroundColor Yellow
    New-Item -Path $profilePath -ItemType File -Force | Out-Null
    Write-Host "Profile created`n" -ForegroundColor Green
}

# Remove old qwen functions
Write-Host "Removing old qwen functions..." -ForegroundColor Yellow
$lines = Get-Content $profilePath
$newLines = @()
$skip = $false
foreach ($line in $lines) {
    if ($line -like "*function qwen*" -or $line -like "*function qwen-backup*" -or $line -like "*function qwen-undo*") { 
        $skip = $true 
    }
    if ($skip -and $line -like "*Set-Alias -Name q*") { 
        $skip = $false
        continue 
    }
    if ($skip -and $line -like "*# ============================================*") { 
        $skip = $false
        continue 
    }
    if (-not $skip) { 
        $newLines += $line 
    }
}
$newLines | Set-Content $profilePath
Write-Host "Old functions removed`n" -ForegroundColor Green

# Add the NEW fixed functions to profile
Write-Host "Adding fixed 'qwen' function to profile..." -ForegroundColor Yellow

$qwenFunction = @"

# ============================================
# Qwen Agent - SAFE WORKSPACE (Fixed paths)
# ============================================
function qwen {
    # Use forward slashes for PowerShell paths (no escaping needed!)
    `$env:SAFE_WORKSPACE = "C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/ai-tools/safe-workspace"
    
    # Check if LM Studio is running
    Write-Host "`nChecking LM Studio server..." -ForegroundColor Cyan
    try {
        `$response = Invoke-WebRequest -Uri "http://localhost:1234/v1/models" -TimeoutSec 2 -ErrorAction Stop
        Write-Host "[OK] LM Studio server detected`n" -ForegroundColor Green
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
    Write-Host "Starting Safe Workspace..." -ForegroundColor Cyan
    Set-Location `$env:SAFE_WORKSPACE
    Write-Host "[SAFE WORKSPACE] Protected environment active`n" -ForegroundColor Green
    py -3.12 safe_launcher.py
}

# Short alias
Set-Alias -Name q -Value qwen -Force

# Backup utilities function
function qwen-backup {
    Set-Location "C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/ai-tools/safe-workspace"
    py -3.12 backup_restore.py
}

# Git undo function
function qwen-undo {
    Set-Location "C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/ai-tools/safe-workspace"
    Write-Host "`n[Git] Undoing last change..." -ForegroundColor Cyan
    git reset --soft HEAD~1
    Write-Host "[Git] Done! Changes preserved but unstaged.`n" -ForegroundColor Green
}

# Quick help
function qwen-help {
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "  Qwen Agent Commands" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
    Write-Host "  qwen         - Start safe workspace (main command)" -ForegroundColor White
    Write-Host "  q            - Short alias for qwen" -ForegroundColor White
    Write-Host "  qwen-backup  - Backup/restore utilities" -ForegroundColor White
    Write-Host "  qwen-undo    - Undo last AI change (git)" -ForegroundColor White
    Write-Host "  qwen-help    - Show this help`n" -ForegroundColor White
    Write-Host "Documentation: C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/ai-tools/docs`n" -ForegroundColor Gray
}
"@

# Append new function
Add-Content -Path $profilePath -Value $qwenFunction
Write-Host "'qwen' function added to profile`n" -ForegroundColor Green

# Reload profile
Write-Host "Reloading profile..." -ForegroundColor Yellow
. $profilePath
Write-Host "Profile reloaded`n" -ForegroundColor Green

# Summary
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================`n"

Write-Host "Files organized:" -ForegroundColor White
Write-Host "  ai-tools/           - All AI tools" -ForegroundColor Gray
Write-Host "  ai-tools/safe-workspace/ - Protected sandbox" -ForegroundColor Gray
Write-Host "  ai-tools/examples/  - Example scripts" -ForegroundColor Gray
Write-Host "  ai-tools/docs/      - Documentation`n" -ForegroundColor Gray

Write-Host "Commands available:" -ForegroundColor White
Write-Host "  qwen         - Main command (from ANY directory)" -ForegroundColor Cyan
Write-Host "  q            - Short alias" -ForegroundColor Cyan
Write-Host "  qwen-backup  - Backup utilities" -ForegroundColor Cyan
Write-Host "  qwen-undo    - Undo changes" -ForegroundColor Cyan
Write-Host "  qwen-help    - Show help`n" -ForegroundColor Cyan

Write-Host "Open a NEW PowerShell window and type 'qwen' to start!"
