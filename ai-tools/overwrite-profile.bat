@echo off
REM OVERWRITE PowerShell Profile - No LM Studio Check!
set PROFILE=%USERPROFILE%\OneDrive\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1

echo.
echo ========================================
echo   OVERWRITE Profile - NO LM Studio Check
echo ========================================
echo.

echo Deleting old profile...
del /F /Q "%PROFILE%" 2>nul

echo.
echo Creating clean profile...

(
echo # Qwen Agent - CLEAN PROFILE - NO LM Studio Check!
echo.
echo function qwen {
echo     Write-Host ""
echo     Write-Host "╔══════════════════════════════════════════════════════════╗" -ForegroundColor White
echo     Write-Host "║     🛡️  Safe Workspace - AI Agent Environment            ║" -ForegroundColor White
echo     Write-Host "╠══════════════════════════════════════════════════════════╣" -ForegroundColor White
echo     Write-Host "║  Modes: 🟡 PLAN  🟢 PLAN-WEB  🔵 AUTO  🔴 YOLO          ║" -ForegroundColor White
echo     Write-Host "║  Commands: [command], TAB, plan-web, search, quit       ║" -ForegroundColor White
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
echo     Write-Host "`n🌐 Researching...`n" -ForegroundColor Green
echo     py -3.12 "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\web_research.py" (`$Goal -join ' ')
echo }
echo.
echo Write-Host "`n✅ Qwen loaded! Type 'qwen' to start`n" -ForegroundColor Green
) > "%PROFILE%"

echo.
echo ✅ Profile OVERWRITTEN!
echo.
echo ========================================
echo   DONE!
echo ========================================
echo.
echo NO LM Studio check - launches immediately!
echo.
echo Close ALL PowerShell windows
echo Open NEW PowerShell
echo Type: qwen
echo.
pause
