@echo off
REM Qwen Profile with PLAN-WEB Mode
set PROFILE=%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

echo.
echo ========================================
echo   Qwen Profile - Plan-Web Mode Added
echo ========================================
echo.
echo Backing up old profile...
copy "%PROFILE%" "%PROFILE%.backup.planweb" 2>nul

echo.
echo Creating profile with Plan-Web mode...

(
echo # Qwen Agent - Plan-Web Mode Enabled
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
echo     Write-Host "║  Modes:                                                  ║" -ForegroundColor White
echo     Write-Host "║    🟡 PLAN       - Show what would be done               ║" -ForegroundColor Yellow
echo     Write-Host "║    🟢 PLAN-WEB   - Research internet + plan              ║" -ForegroundColor Green
echo     Write-Host "║    🔵 AUTO       - Execute with confirmation             ║" -ForegroundColor Cyan
echo     Write-Host "║    🔴 YOLO       - Execute immediately                   ║" -ForegroundColor Red
echo     Write-Host "║                                                          ║" -ForegroundColor White
echo     Write-Host "║  Commands:                                               ║" -ForegroundColor White
echo     Write-Host "║    [command]   - Execute task                            ║" -ForegroundColor White
echo     Write-Host "║    TAB/m       - Toggle mode                             ║" -ForegroundColor White
echo     Write-Host "║    plan        - Create plan                             ║" -ForegroundColor White
echo     Write-Host "║    plan-web    - Research + plan from web                ║" -ForegroundColor White
echo     Write-Host "║    search      - Web search                              ║" -ForegroundColor White
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
echo function plan-web {
echo     param([string[]]`$Goal)
echo     if (-not `$Goal) { Write-Host "`nplan-web `"your goal`"`n" -ForegroundColor Yellow; return }
echo     Write-Host "`n🌐 Researching from Web...`n" -ForegroundColor Green
echo     py -3.12 "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\web_research.py" (`$Goal -join ' ')
echo }
echo.
echo Write-Host "`n✅ Qwen loaded with Plan-Web mode! Type 'qwen' to start`n" -ForegroundColor Green
) > "%PROFILE%"

echo.
echo ✅ Profile updated with Plan-Web mode!
echo.
echo ========================================
echo   DONE!
echo ========================================
echo.
echo NEW FEATURES:
echo   🟢 PLAN-WEB mode added
echo   - Researches internet before planning
echo   - Finds best practices
echo   - Shows sources
echo.
echo Close ALL PowerShell windows
echo Open NEW PowerShell
echo Type: qwen
echo.
pause
