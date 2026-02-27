# AI Search - PowerShell Profile Installer
# Adds ai-search function to your PowerShell profile

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  AI Search - PowerShell Integration" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$profilePath = $PROFILE.CurrentUserCurrentHost
$scriptPath = "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\ai-search.ps1"

Write-Host "Profile path: $profilePath`n"

# Check if profile exists
if (-not (Test-Path $profilePath)) {
    Write-Host "Creating PowerShell profile..." -ForegroundColor Yellow
    New-Item -Path $profilePath -ItemType File -Force | Out-Null
    Write-Host "Profile created`n" -ForegroundColor Green
}

# Check if already added
$content = Get-Content $profilePath -Raw -ErrorAction SilentlyContinue
if ($content -like "*ai-search.ps1*") {
    Write-Host "AI Search already in profile`n" -ForegroundColor Green
} else {
    # Append to profile
    Add-Content -Path $profilePath -Value "`n# AI Search Function`n. '$scriptPath'"
    Write-Host "AI Search added to profile`n" -ForegroundColor Green
}

# Reload profile
Write-Host "Reloading profile..." -ForegroundColor Yellow
. $profilePath
Write-Host "Profile reloaded`n" -ForegroundColor Green

# Test
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Setup Complete!" -ForegroundColor Green
Write-Host "========================================`n"

Write-Host "Commands available:" -ForegroundColor White
Write-Host "  ai-search "query"  - Search the internet" -ForegroundColor Cyan
Write-Host "  ais "query"       - Short alias`n" -ForegroundColor Cyan

Write-Host "Examples:" -ForegroundColor White
Write-Host "  ai-search python async tutorial" -ForegroundColor Gray
Write-Host "  ai-search kotlin coroutines best practices" -ForegroundColor Gray
Write-Host "  ais android gradle error fix`n" -ForegroundColor Gray

Write-Host "Open a NEW PowerShell window and try:" -ForegroundColor Yellow
Write-Host "  ai-search "python machine learning tutorial"`n" -ForegroundColor Cyan
