# 🚨 Emergency Commands - If Qwen Doesn't Work

## ✅ Primary Command (Should Work):

```powershell
qwen
```

---

## 🚨 If `qwen` Doesn't Work:

### Option 1: Emergency Launcher (Easiest)
```bash
C:\Users\mulfa\emergency-qwen.bat
```

Or double-click: `C:\Users\mulfa\emergency-qwen.bat`

---

### Option 2: Direct Launch
```bash
cd C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\safe-workspace
py -3.12 safe_launcher.py
```

---

### Option 3: Fix PowerShell Profile
```powershell
# Run this in PowerShell:
cd C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools
.\overwrite-profile.bat

# Then close ALL PowerShell and open new one
```

---

### Option 4: Reload Profile
```powershell
# In PowerShell, type:
. $PROFILE

# Then try:
qwen
```

---

## 🐛 Troubleshooting:

### "qwen is not recognized"
```powershell
# Try emergency launcher:
C:\Users\mulfa\emergency-qwen.bat

# Or reload profile:
. $PROFILE
```

### "Still shows LM Studio check"
```powershell
# Profile wasn't updated. Run:
cd C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools
.\overwrite-profile.bat

# Close ALL PowerShell windows
# Open NEW one
```

### "Python not found"
```bash
# Python 3.12 should be installed
# Try:
py -3.12 --version
```

### "Safe launcher not found"
```bash
# Navigate directly:
cd C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools\safe-workspace
dir safe_launcher.py
```

---

## 📋 Quick Reference:

| Command | Location | Use |
|---------|----------|-----|
| `qwen` | Any PowerShell | Primary command |
| `emergency-qwen.bat` | `C:\Users\mulfa\` | Backup launcher |
| `py -3.12 safe_launcher.py` | safe-workspace folder | Direct launch |
| `. $PROFILE` | PowerShell | Reload profile |
| `overwrite-profile.bat` | ai-tools folder | Fix profile |

---

## ✅ Emergency Files Created:

| File | Location |
|------|----------|
| `emergency-qwen.bat` | `C:\Users\mulfa\emergency-qwen.bat` |
| `emergency-qwen.bat` | `ai-tools\emergency-qwen.bat` |
| `overwrite-profile.bat` | `ai-tools\overwrite-profile.bat` |

---

## 🎯 Quick Test:

```powershell
# Test if qwen works:
qwen

# If not, use emergency:
C:\Users\mulfa\emergency-qwen.bat
```

---

**Save this file for reference!** 🚨
