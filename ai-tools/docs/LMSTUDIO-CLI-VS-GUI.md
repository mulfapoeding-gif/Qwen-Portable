# LM Studio - CLI vs GUI Explained

## ⚠️ Important: `lms` CLI Does NOT Open GUI

The `lms` command-line tool is **terminal-only**. It never opens the LM Studio application window.

---

## 🎯 Two Separate Tools

### 1. LM Studio CLI (`lms` commands)
**Purpose:** Scripting, API access, terminal usage

**Commands:**
```bash
lms chat MODEL          # Terminal chat (text only)
lms server start        # Start API server
lms server stop         # Stop API server
lms load MODEL          # Load model for API
lms unload MODEL        # Unload model
lms ps                  # List loaded models
lms ls                  # List models on disk
lms runtime survey      # Check GPU hardware
```

**Opens GUI:** ❌ **NO** - Terminal only!

---

### 2. LM Studio Application (GUI)
**Purpose:** Visual model management, settings, interactive chat

**How to Open:**
```
Method 1: Start Menu
  1. Press Windows Key
  2. Type "LM Studio"
  3. Press Enter

Method 2: Run command
  Press Win+R
  Type: lmstudio
  Press Enter

Method 3: Batch file
  Run: ai-tools\launch-lmstudio.bat
```

**Opens GUI:** ✅ **YES** - Full application window

---

## ✅ Your Settings ARE Applied

Both CLI and GUI use the **same settings files**:

### Settings Applied:
```
✓ Context Length: 4096 (visible in `lms ps` output)
✓ GPU Config: Created in user-model-configs/
✓ Developer Mode: Enabled
✓ VRAM Guardrail: 4GB
```

### Proof (from `lms ps`):
```
IDENTIFIER                                                        CONTEXT
imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf    4096 ← Your setting!
```

---

## 🔧 How to Verify Settings

### For CLI:
```bash
# Check context length
lms ps

# Check GPU detection
lms runtime survey

# Check server status
lms server status
```

### For GUI:
```
1. Open LM Studio (from Start Menu)
2. Go to Settings → Model Settings
3. You should see:
   - Context Length: 4096
   - GPU Offload: Near MAX
   - Batch Size: 512
```

---

## 🚀 Quick Start Commands

### Terminal Only (No GUI):
```bash
# Chat in terminal
lms chat imported-models/uncategorized/qwen-coder-unlimited.Q4_K_M.gguf

# Start server for API access
lms server start

# Then use curl or Python to access:
curl http://localhost:1234/v1/models
```

### Open GUI:
```bash
# Method 1: Windows Key
Press Windows Key, type "LM Studio", Enter

# Method 2: Batch file
ai-tools\launch-lmstudio.bat
```

### Both Together:
```bash
# 1. Start server (for API)
lms server start

# 2. Open GUI (for visual management)
# Press Windows Key → "LM Studio" → Enter
#
# Both use the same backend!
```

---

## 📊 What's Running

| Component | Status | Purpose |
|-----------|--------|---------|
| **Daemon (llmster)** | PID 5984 | Background service |
| **Server** | Port 1234 | API endpoint |
| **Model** | Loaded | Ready for chat/API |
| **GPU** | Detected | Quadro P1000 (4GB) |
| **Context** | 4096 | Your optimized setting |

---

## 🐛 Common Confusion

### "I run `lms chat` but no window opens!"
**Expected!** `lms chat` is **terminal-only**. The chat happens in your PowerShell window.

### "How do I see the LM Studio interface?"
Open from Start Menu: Windows Key → "LM Studio" → Enter

### "Did my settings apply?"
**YES!** Check with:
```bash
lms ps  # Look at CONTEXT column
```

---

## 🎯 Recommended Workflow

### For Development:
```bash
# 1. Open LM Studio GUI (for settings, model management)
# Windows Key → "LM Studio"

# 2. Use CLI for quick tests
lms chat MODEL -p "Quick question"

# 3. Use GUI for long chats, visual features
```

### For API/Integration:
```bash
# 1. Start server
lms server start

# 2. Use from your code
# Python, Node.js, curl, etc.
# http://localhost:1234/v1/chat/completions
```

### For Quick Terminal Work:
```bash
# Everything in terminal
lms chat MODEL
# Chat interactively right here
```

---

## 📁 Quick Reference

| File | Location | Purpose |
|------|----------|---------|
| **CLI** | `C:\Users\mulfa\.lmstudio\bin\lms.exe` | Command-line tool |
| **Settings** | `C:\Users\mulfa\.lmstudio\settings.json` | Global config |
| **GPU Config** | `C:\Users\mulfa\.lmstudio\user-model-configs\` | Per-model GPU |
| **Ollama** | `C:\Users\mulfa\.ollama\.env` | Ollama config |
| **Launcher** | `ai-tools\launch-lmstudio.bat` | GUI shortcut |

---

## ✅ Summary

**`lms` CLI:**
- ✅ Terminal only
- ✅ No GUI opens
- ✅ Settings ARE applied
- ✅ Use for scripting, API, quick tests

**LM Studio App:**
- ✅ Full GUI
- ✅ Open from Start Menu
- ✅ Settings ARE applied
- ✅ Use for visual management, long chats

**Both use the same backend and settings!**

---

**Quick Test:**
```bash
# Verify settings applied
lms ps

# Should show CONTEXT = 4096
```
