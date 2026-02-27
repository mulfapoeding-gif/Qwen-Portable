# 🛡️ Safe Workspace - Complete Guide

## 🎯 What It Is

A **protected sandbox environment** where AI agents can work safely without risking damage to your system or files.

---

## 🏗️ Directory Structure

```
uncategorized/
├── safe-workspace.bat          # ⭐ LAUNCHER - Start safe workspace
├── safe-workspace/
│   ├── README.md               # Safety documentation
│   ├── safe_launcher.py        # Main safe launcher
│   ├── backup_restore.py       # Backup utilities
│   ├── .safety-config.yml      # Safety settings
│   ├── projects/               # Your safe projects
│   │   └── sandbox/           # Test area
│   ├── temp/                   # Temporary files
│   ├── .backups/               # Automatic backups
│   └── logs/                   # Activity logs
```

---

## 🛡️ Safety Features

### 1. **Git Auto-Commit** (Time Machine)
```
Every change is automatically committed to Git
→ Can undo any agent action
→ Full history of what AI did
→ Command: git log
```

### 2. **Automatic Backups** (Insurance)
```
Before major changes:
→ Timestamped backup created
→ Stored in .backups/
→ Can restore anytime
```

### 3. **Protected Directories** (Walls)
```
Agents CAN modify:
  ✓ safe-workspace/projects/
  ✓ safe-workspace/temp/
  ✓ safe-workspace/sandbox/

Agents CANNOT touch:
  ✗ C:/Windows/
  ✗ C:/Program Files/
  ✗ Your Documents
  ✗ System files
```

### 4. **Confirmation Prompts** (Double-Check)
```
Dangerous operations ask first:
  → Delete files: "Type YES to confirm"
  → Install packages: "Proceed? (y/n)"
  → Network access: "Allow connection? (y/n)"
```

### 5. **Activity Logging** (Audit Trail)
```
Every action logged:
  [10:30:45] COMMAND: Create python function
  [10:30:46] AIDER: Generated code
  [10:30:47] GIT: Committed changes
  [10:30:48] BACKUP: Created backup_20250101_103048
```

---

## 🚀 How to Use

### Start Safe Workspace

**Method 1: Batch File**
```bash
safe-workspace.bat
```

**Method 2: PowerShell** (add this function)
```powershell
function safe-qwen {
    cd "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized"
    py -3.12 safe-workspace/safe_launcher.py
}
```

### Inside Safe Workspace

```
╔══════════════════════════════════════════════════════════╗
║     🛡️  Safe Workspace - AI Agent Environment            ║
╠══════════════════════════════════════════════════════════╣
║  Protected Environment:                                  ║
║    ✓ Git auto-commit                                     ║
║    ✓ Automatic backups                                   ║
║    ✓ Activity logging                                    ║
║    ✓ Protected directories                               ║
╚══════════════════════════════════════════════════════════╝

>>> Create a test python script

📦 Creating backup...
✓ Backup: backup_20250126_103045
✓ Git commit: Create a test python script
[████████████████████] Running aider...
✓ aider completed

Result: Your code is created safely!
```

---

## 🔄 Backup & Restore

### Manual Backup
```bash
# Open backup utilities
py -3.12 safe-workspace/backup_restore.py

# Select: 1. Create Backup
```

### Restore from Backup
```bash
# Open backup utilities
py -3.12 safe-workspace/backup_restore.py

# Select: 3. Restore from Backup
# Choose backup from list
# Type YES to confirm
```

### Git Undo
```bash
# See what changed
cd safe-workspace
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard changes completely
git restore .
```

---

## 🛡️ Safety Levels

Edit `.safety-config.yml` to adjust:

### Strict (Default)
```yaml
safety_level: strict
# - All protections active
# - Confirmations required
# - Protected directories enforced
```

### Moderate
```yaml
safety_level: moderate
# - Backups enabled
# - Git enabled
# - Fewer confirmations
```

### Permissive (NOT RECOMMENDED)
```yaml
safety_level: permissive
# - Minimal protections
# - Use only when trusted
```

---

## 📊 Activity Logs

View logs:
```bash
# Today's log
type safe-workspace/logs/agent_log_20250226.txt

# All logs
dir safe-workspace/logs/
```

Log format:
```
[10:30:45] COMMAND: Create python function
[10:30:46] BACKUP: Created backup_20250126_103046
[10:30:47] GIT: Committed changes
[10:30:48] AIDER: Generated code
[10:30:49] STATUS: Complete
```

---

## ⚠️ Protected Operations

These require **YES confirmation**:

| Operation | Confirmation |
|-----------|--------------|
| Delete file | Type "YES" |
| Delete directory | Type "YES" |
| Execute shell command | Type "YES" |
| Install package | Type "YES" |
| Network access | Type "YES" |
| Modify protected path | BLOCKED |

---

## 🎯 Example Workflow

### 1. Start Safe Workspace
```bash
safe-workspace.bat
```

### 2. Create Code
```
>>> Create a Python web scraper

📦 Backup created
✓ Git committed
[████████████████████] Running...
✓ Complete!
```

### 3. Review What Was Done
```bash
cd safe-workspace
git diff HEAD~1
```

### 4. Test the Code
```
>>> Run the scraper

[Executing in temp/]
✓ Output: [results]
```

### 5. Keep or Revert
```bash
# If good - keep it
# If bad - undo!
git restore .
```

---

## 🔧 Backup Utilities Menu

```
╔════════════════════════════════════════╗
║  🛡️  Backup & Restore Utilities          ║
╠════════════════════════════════════════╣
║  1. Create Backup                      ║
║  2. List Backups                       ║
║  3. Restore from Backup                ║
║  4. Show Git History                   ║
║  5. Undo Last Change                   ║
║  0. Exit                               ║
╚════════════════════════════════════════╝
```

---

## 🚨 Emergency Procedures

### "Agent is going crazy!"
```
1. Press Ctrl+C to interrupt
2. Type 'quit' to exit
3. Run: git restore .
```

### "I deleted something important!"
```
1. Open backup utilities
2. Select "Restore from Backup"
3. Choose recent backup
4. Type YES to confirm
```

### "System is messed up!"
```
1. cd safe-workspace
2. git log --oneline
3. git reset --hard <good-commit>
4. Everything restored to that point
```

---

## 📋 Safety Checklist

Before running agents:

- [ ] LM Studio server ready
- [ ] Safe workspace initialized
- [ ] Git working (`git status`)
- [ ] Backup directory exists
- [ ] Protected paths configured

After running agents:

- [ ] Check git log
- [ ] Review changes
- [ ] Test generated code
- [ ] Create manual backup if needed

---

## 🎓 Best Practices

### ✅ DO
- Always use safe workspace for experiments
- Review git diffs before keeping changes
- Create manual backups before big changes
- Check activity logs regularly
- Test in `sandbox/` first

### ❌ DON'T
- Disable safety features
- Skip backup creation
- Give agents system paths
- Ignore confirmation prompts
- Delete backup files

---

## 🔐 Advanced Configuration

### Add More Protected Paths

Edit `.safety-config.yml`:
```yaml
protected_directories:
  - C:/My/Important/Folder
  - D:/Critical/Data
```

### Custom Backup Schedule

Add to your tasks:
```bash
# Daily backup at 9 AM
0 9 * * * py -3.12 backup_restore.py --auto
```

### Integration with Regular Qwen

Modify PowerShell profile:
```powershell
function qwen {
    # Always use safe workspace
    cd "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized"
    py -3.12 safe-workspace/safe_launcher.py
}
```

---

## 📊 Comparison

| Feature | Regular Qwen | Safe Workspace |
|---------|-------------|----------------|
| Git auto-commit | ✗ | ✓ |
| Automatic backups | ✗ | ✓ |
| Protected directories | ✗ | ✓ |
| Activity logging | Partial | ✓ Full |
| One-click restore | ✗ | ✓ |
| Confirmation prompts | Some | ✓ All dangerous |
| Audit trail | ✗ | ✓ |

---

## 🎯 Summary

**Safe Workspace gives you:**

✅ **Sandbox** - Protected area for AI experiments  
✅ **Time Machine** - Git undo for any change  
✅ **Insurance** - Automatic backups  
✅ **Walls** - Protected system directories  
✅ **Audit** - Complete activity logs  
✅ **Control** - Confirmation prompts  

**Start with:** `safe-workspace.bat`

**Remember:** When in doubt, restore from backup!

---

**Your AI playground is now SAFE!** 🛡️
