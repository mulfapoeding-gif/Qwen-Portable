# Qwen Agent PowerShell Function
# Add this to your PowerShell profile

function qwen {
    $scriptPath = "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\examples\qwen_orchestrator.py"
    
    # Check if LM Studio is running
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:1234/v1/models" -TimeoutSec 2 -ErrorAction Stop
        Write-Host "`n[OK] LM Studio server detected`n" -ForegroundColor Green
    } catch {
        Write-Host "`n[WARNING] LM Studio server not detected!" -ForegroundColor Yellow
        Write-Host "Please start LM Studio server:`n"
        Write-Host "  1. Open LM Studio"
        Write-Host "  2. Load a model"
        Write-Host "  3. Start Local Server`n"
        Write-Host "Press any key to continue anyway..."
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    }
    
    # Run the orchestrator
    py -3.12 $scriptPath
}

# Short alias
Set-Alias -Name q -Value qwen -Force

# Export function for future sessions
Export-ModuleMember -Function qwen -Alias q
