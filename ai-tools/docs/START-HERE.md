# 📁 AI Tools - Organized Structure

## New Folder Layout

```
uncategorized/
│
├── ai-tools/                      # ⭐ All AI tools organized here
│   │
│   ├── safe-workspace/            # Protected sandbox environment
│   │   ├── safe_launcher.py       # Main launcher
│   │   ├── backup_restore.py      # Backup utilities
│   │   ├── .safety-config.yml     # Safety settings
│   │   ├── projects/              # Your safe projects
│   │   ├── temp/                  # Temporary files
│   │   ├── .backups/              # Auto backups
│   │   └── logs/                  # Activity logs
│   │
│   ├── examples/                  # Example scripts
│   │   ├── qwen_orchestrator.py   # Main orchestrator
│   │   ├── langchain_agent.py     # LangChain example
│   │   ├── autogen_agents.py      # AutoGen example
│   │   ├── autogen_multi_model.py # Multi-model setup
│   │   └── gradio_dashboard.py    # Web dashboard
│   │
│   └── docs/                      # All documentation
│       ├── START-HERE.md          # Quick start (this file)
│       ├── SAFE-WORKSPACE-GUIDE.md
│       ├── ORCHESTRATOR-GUIDE.md
│       ├── AGENT-FRAMEWORKS.md
│       ├── MULTI-MODEL-SETUP.md
│       └── ...
│
├── qwen-agent.bat                 # Quick launcher
├── safe-workspace.bat             # Safe workspace launcher
└── install-powershell-fixed.ps1   # PowerShell installer
```

---

## 🚀 Quick Start

### From ANY PowerShell:
```powershell
qwen
```

### Or use batch files:
```bash
qwen-agent.bat           # Quick launch
safe-workspace.bat       # Safe workspace
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| **START-HERE.md** | This file - overview |
| **SAFE-WORKSPACE-GUIDE.md** | Safety features & usage |
| **ORCHESTRATOR-GUIDE.md** | Agent orchestrator docs |
| **AGENT-FRAMEWORKS.md** | LangChain + AutoGen |
| **MULTI-MODEL-SETUP.md** | Multiple models setup |

---

## 🛡️ Safe Workspace

Your AI agents work in a **protected sandbox**:

- ✅ Git auto-commit (undo anything)
- ✅ Automatic backups
- ✅ Protected directories
- ✅ Activity logging
- ✅ Confirmation prompts

---

## 🎯 Commands

| Command | Action |
|---------|--------|
| `qwen` | Start safe workspace |
| `q` | Short alias |
| `qwen-backup` | Backup/restore |
| `qwen-undo` | Undo last change |
| `qwen-help` | Show help |

---

**Start with:** Open PowerShell and type `qwen`
