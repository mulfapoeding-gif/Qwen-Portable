# Qwen-Portable - PowerShell Profile Fix Script
# This script cleans and reconfigures PowerShell profile for Qwen (fresh start)
# Run this if qwen command is broken or not working

$Base = "C:\Users\mulfa\Qwen-Portable"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  PowerShell Profile Fix & Reconfig" -ForegroundColor Cyan
Write-Host "========================================"
Write-Host ""

Write-Host "This script will:" -ForegroundColor Yellow
Write-Host "  1. Backup your current PowerShell profile" -ForegroundColor White
Write-Host "  2. Remove ALL old Qwen functions" -ForegroundColor White
Write-Host "  3. Install fresh Qwen configuration" -ForegroundColor White
Write-Host "  4. Test the new configuration" -ForegroundColor White
Write-Host ""

$continue = Read-Host "Continue? (y/n)"
if ($continue -ne "y" -and $continue -ne "Y") {
    Write-Host "Cancelled." -ForegroundColor Red
    exit
}

Write-Host ""

# Get PowerShell profile path
$profilePath = $PROFILE.CurrentUserCurrentHost

Write-Host "Profile path: $profilePath" -ForegroundColor Gray
Write-Host ""

# Step 1: Backup current profile
Write-Host "[Step 1/4] Backing up current profile..." -ForegroundColor Cyan

if (Test-Path $profilePath) {
    $backupName = "Microsoft.PowerShell_profile.backup." + (Get-Date -Format "yyyyMMdd-HHmmss") + ".ps1"
    $backupPath = Join-Path (Split-Path $profilePath) $backupName
    Copy-Item -Path $profilePath -Destination $backupPath -Force
    Write-Host "  [OK] Backup created: $backupName" -ForegroundColor Green
} else {
    Write-Host "  [INFO] No existing profile found, will create new one" -ForegroundColor Gray
}

Write-Host ""

# Step 2: Remove old Qwen functions
Write-Host "[Step 2/4] Removing old Qwen functions..." -ForegroundColor Cyan

if (Test-Path $profilePath) {
    $content = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
    
    if ($content -like "*function qwen*" -or $content -like "*function qwen-backup*" -or $content -like "*function qwen-undo*" -or $content -like "*function qwen-help*") {
        $lines = Get-Content $profilePath
        $newLines = @()
        $skip = $false
        $removedCount = 0
        
        foreach ($line in $lines) {
            if ($line -like "*function qwen*" -or $line -like "*function qwen-backup*" -or $line -like "*function qwen-undo*" -or $line -like "*function qwen-help*") {
                $skip = $true
                $removedCount++
            }
            if ($skip -and $line -like "*Set-Alias -Name q*") {
                $skip = $false
                $removedCount++
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
        
        $newLines | Set-Content $profilePath -Force
        Write-Host "  [OK] Removed $removedCount old Qwen function(s)" -ForegroundColor Green
    } else {
        Write-Host "  [INFO] No old Qwen functions found" -ForegroundColor Gray
    }
} else {
    Write-Host "  [INFO] Profile does not exist, will create new one" -ForegroundColor Gray
    $profileDir = Split-Path -Path $profilePath -Parent
    if (-not (Test-Path $profileDir)) {
        New-Item -Path $profileDir -ItemType Directory -Force | Out-Null
    }
    New-Item -Path $profilePath -ItemType File -Force | Out-Null
    Write-Host "  [OK] New profile created" -ForegroundColor Green
}

Write-Host ""

# Step 3: Install fresh Qwen configuration
Write-Host "[Step 3/4] Installing fresh Qwen configuration..." -ForegroundColor Cyan

$qwenFunction = @"

# ============================================
# Qwen Agent - Portable Installation
# Installed: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
# ============================================
function qwen {
    `$env:QWEN_BASE = "$Base"
    `$env:SAFE_WORKSPACE = "$Base\ai-tools\safe-workspace"

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
    Set-Location "$Base\ai-tools\safe-workspace"
    py -3.12 backup_restore.py
}

# Git undo function
function qwen-undo {
    Set-Location "$Base\ai-tools\safe-workspace"
    Write-Host "`n[Git] Undoing last change..." -ForegroundColor Cyan
    git reset --soft HEAD~1
    Write-Host "[Git] Done! Changes preserved but unstaged.`n" -ForegroundColor Green
}

# Quick help
function qwen-help {
    Write-Host "`n========================================" -ForegroundColor Cyan
    Write-Host "  Qwen Agent Commands" -ForegroundColor Cyan
    Write-Host "========================================`n" -ForegroundColor Cyan
    Write-Host "  qwen         - Start safe workspace" -ForegroundColor White
    Write-Host "  q            - Short alias" -ForegroundColor White
    Write-Host "  qwen-backup  - Backup/restore utilities" -ForegroundColor White
    Write-Host "  qwen-undo    - Undo last AI change" -ForegroundColor White
    Write-Host "  qwen-help    - Show this help`n" -ForegroundColor White
    Write-Host "Documentation: $Base\docs`n" -ForegroundColor Gray
}
"@

Add-Content -Path $profilePath -Value $qwenFunction
Write-Host "  [OK] Fresh Qwen configuration installed" -ForegroundColor Green

Write-Host ""

# Step 4: Test the configuration
Write-Host "[Step 4/4] Testing configuration..." -ForegroundColor Cyan

Write-Host "  Reloading profile..." -ForegroundColor Gray
. $profilePath

Write-Host ""
Write-Host "  Testing commands..." -ForegroundColor Gray

if (Get-Command qwen -ErrorAction SilentlyContinue) {
    Write-Host "  [OK] 'qwen' command is available" -ForegroundColor Green
} else {
    Write-Host "  [WARN] 'qwen' command not loaded (restart PowerShell to use)" -ForegroundColor Yellow
}

if (Get-Command q -ErrorAction SilentlyContinue) {
    Write-Host "  [OK] 'q' alias is available" -ForegroundColor Green
} else {
    Write-Host "  [WARN] 'q' alias not loaded (restart PowerShell to use)" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  PowerShell Profile Fix Complete!" -ForegroundColor Green
Write-Host "========================================"
Write-Host ""
Write-Host "What was done:" -ForegroundColor White
Write-Host "  1. Backed up your old profile" -ForegroundColor Gray
Write-Host "  2. Removed all old Qwen functions" -ForegroundColor Gray
Write-Host "  3. Installed fresh Qwen configuration" -ForegroundColor Gray
Write-Host "  4. Tested the new configuration" -ForegroundColor Gray
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Close ALL PowerShell windows" -ForegroundColor White
Write-Host "  2. Open a NEW PowerShell window" -ForegroundColor White
Write-Host "  3. Type: qwen" -ForegroundColor White
Write-Host ""
if (Test-Path $backupPath) {
    Write-Host "Backup location:" -ForegroundColor Gray
    Write-Host "  $backupPath" -ForegroundColor Gray
    Write-Host ""
}
