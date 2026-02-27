# 🚀 AI Tools - Quick Start (Admin)

## Run Optimizer as Administrator

### Method 1: Double-click (Easiest)
```
optimize-as-admin.bat
```
Click "Yes" on the UAC prompt

### Method 2: PowerShell (Manual)
```powershell
# Open PowerShell as Administrator
# Then run:
cd C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\ai-tools
.\optimize-admin.ps1
```

### Method 3: With Help
```powershell
.\optimize-admin.ps1 -Help
```

---

## What It Does

| Step | Action | Requires Admin |
|------|--------|----------------|
| 1 | Create Ollama .env | No |
| 2 | Set SYSTEM env vars | **Yes** |
| 3 | Set USER env vars | No |
| 4 | Detect GPU | No |
| 5 | Check processes | No |
| 6 | Create launch scripts | No |

---

## After Running

### 1. Restart (Recommended)
```
Restart your computer for system env vars to apply
```

### 2. Or Restart Ollama
```powershell
# Stop Ollama (task manager or tray icon)
# Then start:
ollama serve
```

### 3. LM Studio (Manual)
```
Open LM Studio → Settings → Model Settings
- GPU Offload: MAX →
- Context: 4096
- Batch: 512
```

---

## Quick Launch

After optimization, start Ollama with optimized settings:

```powershell
cd ai-tools
.\launch-optimized.ps1
```

---

## Verify Settings

```powershell
# Check environment variables
Get-ChildItem Env: | Where-Object { $_.Name -like "OLLAMA*" }

# Should show:
# OLLAMA_MAX_VRAM      = 4294967296
# OLLAMA_NUM_GPU       = 99
# OLLAMA_GPU_LAYERS    = 99
# etc.
```

---

## Troubleshooting

### "Script cannot be loaded"
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### "Access denied"
- Make sure you're running as Administrator
- Right-click → "Run as Administrator"

### Settings not applying
- Restart your computer
- Or restart Ollama service

---

**Files Created:**
- `optimize-admin.ps1` - Main optimizer (Admin)
- `optimize-as-admin.bat` - Easy launcher
- `launch-optimized.ps1` - Quick start Ollama
