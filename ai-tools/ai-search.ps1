# AI Search - Internet Research Function for PowerShell
# Add this to your PowerShell profile for quick access

function ai-search {
    param(
        [Parameter(Position=0, ValueFromRemainingArguments=$true)]
        [string[]]$Query
    )
    
    if (-not $Query) {
        Write-Host "`n========================================" -ForegroundColor Cyan
        Write-Host "  AI Search - DuckDuckGo Research Tool" -ForegroundColor Cyan
        Write-Host "========================================`n" -ForegroundColor Cyan
        Write-Host "Usage:" -ForegroundColor White
        Write-Host "  ai-search `"your search query`"`n" -ForegroundColor Gray
        Write-Host "Examples:" -ForegroundColor White
        Write-Host "  ai-search python async tutorial" -ForegroundColor Gray
        Write-Host "  ai-search kotlin coroutines best practices" -ForegroundColor Gray
        Write-Host "  ai-search android gradle build error fix`n" -ForegroundColor Gray
        return
    }
    
    $searchQuery = $Query -join " "
    Write-Host "`n[Searching DuckDuckGo for: $searchQuery]`n" -ForegroundColor Cyan
    
    & py -3.12 -m duckduckgo_search text -k $searchQuery -m 5
}

# News search
function ai-search-news {
    param(
        [Parameter(Position=0, ValueFromRemainingArguments=$true)]
        [string[]]$Query
    )
    
    $searchQuery = $Query -join " "
    Write-Host "`n[Searching News for: $searchQuery]`n" -ForegroundColor Cyan
    
    & py -3.12 -m duckduckgo_search news -k $searchQuery -m 5
}

# Alias
Set-Alias -Name ais -Value ai-search -Force
