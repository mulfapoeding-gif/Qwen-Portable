@echo off
REM Final Qwen Profile - Clean Display, No Blocking
set PROFILE=%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

echo.
echo ========================================
echo   Final Qwen Profile Setup
echo ========================================
echo.
echo Backing up old profile...
copy "%PROFILE%" "%PROFILE%.backup.final" 2>nul

echo.
echo Creating clean profile...

(
echo # Qwen Agent - Clean Profile - No Blocking!
echo.
echo function qwen {
echo     Write-Host ""
echo     Write-Host "╔══════════════════════════════════════════════════════════╗" -ForegroundColor White
echo     Write-Host "║     🛡️  Safe Workspace - AI Agent Environment            ║" -ForegroundColor White
echo     Write-Host "╠══════════════════════════════════════════════════════════╣" -ForegroundColor White
echo     Write-Host "║  🤖 AI Orchestrator Pro:                                 ║" -ForegroundColor White
echo     Write-Host "║    📝 Coder (7B)  📋 Planner (3B)  🔍 Reviewer (4B)     ║" -ForegroundColor White
echo     Write-Host "║    🔍 Search  🌐 Scraper  📋 Planner  🧪 Executor        ║" -ForegroundColor White
echo     Write-Host "║                                                          ║" -ForegroundColor White
echo     Write-Host "║  Commands:                                               ║" -ForegroundColor White
echo     Write-Host "║    [command]   - Execute task                            ║" -ForegroundColor White
echo     Write-Host "║    TAB/m       - Toggle mode (Plan/Auto/Yolo)            ║" -ForegroundColor White
echo     Write-Host "║    plan        - Create plan                             ║" -ForegroundColor White
echo     Write-Host "║    search      - Web search                              ║" -ForegroundColor White
echo     Write-Host "║    scrape      - Web scraping                            ║" -ForegroundColor White
echo     Write-Host "║    status      - Show status                             ║" -ForegroundColor White
echo     Write-Host "║    quit        - Exit                                    ║" -ForegroundColor White
echo     Write-Host "╚══════════════════════════════════════════════════════════╝" -ForegroundColor White
echo     Write-Host ""
echo     cd /d "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\safe-workspace"
echo     py -3.12 safe_launcher.py
echo }
echo.
echo Set-Alias -Name q -Value qwen -Force
echo.
echo function ai-search {
echo     param([string[]]`$Query)
echo     if (-not `$Query) { Write-Host "`nai-search `"query`"`n" -ForegroundColor Yellow; return }
echo     Write-Host "`n🔍 Searching...`n" -ForegroundColor Cyan
echo     py -3.12 -m duckduckgo_search text -k (`$Query -join ' ') -m 5
echo }
echo Set-Alias -Name ais -Value ai-search -Force
echo.
echo function plan-task {
echo     param([string[]]`$Goal)
echo     Write-Host "`n📋 Planning...`n" -ForegroundColor Cyan
echo     py -3.12 "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\task_planner.py" (`$Goal -join ' ')
echo }
echo.
echo Write-Host "`n✅ Qwen loaded! Type 'qwen' to start`n" -ForegroundColor Green
) > "%PROFILE%"

echo.
echo ✅ Profile created!
echo.
echo ========================================
echo   DONE!
echo ========================================
echo.
echo Close ALL PowerShell windows
echo Open NEW PowerShell
echo Type: qwen
echo.
pause
