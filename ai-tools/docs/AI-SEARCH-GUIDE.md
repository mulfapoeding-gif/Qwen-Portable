# 🌐 AI Search - Internet Research Tool

## ✅ Internet Boost Installed!

**DuckDuckGo Search** is now integrated into your AI tools!

---

## 🚀 Quick Start

### In PowerShell (NEW window):
```powershell
# Text search
ai-search "python async tutorial"

# Short alias
ais "kotlin coroutines"

# News search
ai-search-news "AI developments"

# Help
ai-search
```

### From Batch File:
```bash
ai-tools\ai-search.bat "android gradle error"
```

---

## 📚 Commands

| Command | Purpose | Example |
|---------|---------|---------|
| `ai-search "query"` | Web search | `ai-search "python tutorial"` |
| `ais "query"` | Short alias | `ais "kotlin best practices"` |
| `ai-search-news "topic"` | News search | `ai-search-news "AI news"` |
| `ai-search-images "topic"` | Image search | `ai-search-images "architecture"` |
| `ai-search-help` | Show options | `ai-search-help` |

---

## 🔍 Search Options

### Text Search (Default)
```powershell
ai-search "python async await tutorial"
```

### News Search
```powershell
ai-search-news "machine learning breakthrough"
```

### Image Search
```powershell
ai-search-images "neural network diagram"
```

### Advanced Options (via CLI)
```bash
# Region-specific
py -3.12 -m duckduckgo_search text -k "python" -r us-en

# Time limit (day/week/month/year)
py -3.12 -m duckduckgo_search text -k "python" -t w

# Safe search
py -3.12 -m duckduckgo_search text -k "python" -s moderate

# Max results
py -3.12 -m duckduckgo_search text -k "python" -m 10
```

---

## 🎯 Integration with AI Agents

### Use in Your Workflow:

1. **Research First**
   ```powershell
   # Search for solution
   ais "android gradle build error fix"
   
   # Then use Aider to implement
   aider -m "Fix this gradle error based on search results"
   ```

2. **Debug with Research**
   ```powershell
   # Search error message
   ais "TypeError: 'NoneType' object python fix"
   
   # Apply fix with AI
   aider myfile.py -m "Fix this based on search results"
   ```

3. **Learn New Technology**
   ```powershell
   # Find tutorials
   ais "rust ownership tutorial beginners"
   
   # Generate examples
   aider -m "Create rust ownership examples based on tutorial"
   ```

---

## 📊 Search Result Format

```
1.    Title - Source
title       Result Title
href        https://example.com/page
body        Result description and snippet...

2.    Next Result - Source
...
```

---

## 🔧 Troubleshooting

### "ai-search not recognized"
```powershell
# Reload profile
. $PROFILE

# Or restart PowerShell
```

### "No results found"
- Try different keywords
- Check spelling
- Try broader search terms

### "Request timeout"
- Check internet connection
- DuckDuckGo may be temporarily unavailable
- Try again in a few seconds

---

## 🛡️ Privacy Features

**DuckDuckGo Search:**
- ✅ No tracking
- ✅ No personalization
- ✅ No filter bubbles
- ✅ Same results for everyone
- ✅ No search history stored

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `ai-tools/ai-search.bat` | Batch launcher |
| `ai-tools/ai-search.ps1` | PowerShell function |
| `ai-tools/install-ai-search.ps1` | Installer |

---

## 🎓 Examples

### Development Research
```powershell
# Find documentation
ais "rust lifetime annotations explained"

# Search for errors
ais "borrowed value does not live long enough rust"

# Find best practices
ais "rust error handling best practices 2025"
```

### Android/Kotlin
```powershell
# Debug build errors
ais "gradle build failed java home"

# Learn features
ais "kotlin flow vs livedata"

# Find libraries
ais "best kotlin json parser 2025"
```

### General Programming
```powershell
# Tutorials
ais "docker compose tutorial beginners"

# Compare technologies
ais "postgresql vs mysql 2025"

# Performance tips
ais "python performance optimization tips"
```

---

## 🔄 Reload Profile

If commands don't work:
```powershell
# Reload PowerShell profile
. $PROFILE

# Verify functions exist
Get-Command ai-search
Get-Command ais
```

---

## ✅ Summary

**You now have:**
- ✅ DuckDuckGo search integrated
- ✅ PowerShell functions (`ai-search`, `ais`)
- ✅ Batch file launcher
- ✅ News and image search
- ✅ Privacy-focused research
- ✅ Works with AI agents

**Quick test:**
```powershell
ai-search "python machine learning tutorial"
```

---

**Happy researching!** 🔍
