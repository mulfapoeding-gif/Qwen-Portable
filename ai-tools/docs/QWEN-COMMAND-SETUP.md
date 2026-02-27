# ✅ Qwen Command - PowerShell Setup Complete!

## 🎯 What's Installed

The **`qwen`** command is now available in PowerShell!

---

## 🚀 How to Use

### 1. Open a NEW PowerShell Window
(Close any existing ones and open a fresh window)

### 2. Type:
```powershell
qwen
```

Or the short alias:
```powershell
q
```

---

## 📊 What Happens

When you type `qwen`:

```
1. Checks if LM Studio server is running
   ├─ ✓ Running → Continues
   └─ ✗ Not running → Shows warning, asks to continue

2. Launches the Qwen Agent Orchestrator
   ├─ Shows agent status
   ├─ Displays mode (Plan/Auto/Yolo)
   └─ Ready for your commands

3. You can now:
   ├─ Type commands → Agents execute with indicators
   ├─ Press TAB → Toggle modes
   ├─ Type 'status' → Check agents
   └─ Type 'quit' → Exit
```

---

## 💬 Example Session

```powershell
PS C:\Users\mulfa> qwen

[OK] LM Studio server detected

╔══════════════════════════════════════════════════════════╗
║     🤖 Qwen Agent Orchestrator                        ║
╠══════════════════════════════════════════════════════════╣
║  Commands:                                               ║
║    - Type your command                                   ║
║    - TAB or 'm' = Toggle mode (Plan/Auto/Yolo)           ║
║    - 'status' = Show agent status                        ║
║    - 'quit' = Exit                                       ║
╚══════════════════════════════════════════════════════════╝

=== Agent Status ===
  ✓ Aider
  ✓ Langchain
  ✓ Autogen
  ✓ Search

>>> Create a python hello world

📍 Mode: AUTO

Step 1/1: Activating aider agent...
[████████████████████] Running aider...
✓ aider completed

══════════════════════════════════════════════════════════
Results:

[1] def hello():
    print("Hello, World!")

══════════════════════════════════════════════════════════

>>> quit

👋 Goodbye!
```

---

## 🎛️ Commands Inside Orchestrator

| Command | Action |
|---------|--------|
| **Any text** | Processed as command |
| `tab` or `m` | Toggle mode (Plan/Auto/Yolo) |
| `status` | Show available agents |
| `quit` or `exit` or `q` | Exit orchestrator |

---

## 🔧 Troubleshooting

### "qwen is not recognized"
```powershell
# Reload profile
. $PROFILE

# Or restart PowerShell
```

### "LM Studio server not detected"
```
1. Open LM Studio
2. Load a model
3. Click "Start Server"
4. Try again
```

### Want to reinstall?
```powershell
# Run the installer again
py -3.12 "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\install-powershell.ps1"
```

---

## 📁 Files

| File | Purpose |
|------|---------|
| `qwen` (PowerShell command) | Main launcher |
| `q` (alias) | Short launcher |
| `qwen-agent.bat` | Alternative batch launcher |
| `examples/qwen_orchestrator.py` | Main orchestrator |
| `ORCHESTRATOR-GUIDE.md` | Full documentation |

---

## ⚡ Quick Start

1. **Open NEW PowerShell**
2. **Type:** `qwen`
3. **Give command:** `Create a fibonacci function`
4. **Watch agents work!**

---

**That's it! You're ready to command your AI agents!** 🎉
