# Aider + LM Studio Setup Guide

## ✅ Installation Complete!

### Quick Start

1. **Start LM Studio Server:**
   - Open LM Studio
   - Load a model (e.g., Qwen Coder from your imported models)
   - Go to "Local Server" tab
   - Click "Start Server" (default: http://localhost:1234)

2. **Run Aider:**
   ```bash
   py -3.12 -m aider --openai-api-base http://localhost:1234/v1 --openai-api-key not-needed
   ```

3. **Or use the batch file:**
   - Copy `aider-lmstudio.bat` to `C:\Users\mulfa\bin\`
   - Add to PATH or run from there
   - Run: `aider-lmstudio`

### Add to PATH (Optional)

To run `aider-lmstudio` from anywhere:

**Option A: Add Python Scripts to PATH**
```bash
# Add this to your system PATH:
C:\Users\mulfa\AppData\Local\Programs\Python\Python312\Scripts
```

**Option B: Create a shortcut**
1. Copy `aider-lmstudio.bat` to `C:\Users\mulfa\bin\`
2. Add `C:\Users\mulfa\bin\` to PATH

### Basic Aider Commands

```bash
# Start interactive session
aider

# One-shot message
aider --message "fix the bug in this function"

# Add specific files to context
aider myfile.py

# See all options
aider --help
```

### Aider Modes

- **Interactive mode** (default): Chat and edit files together
- **Message mode**: Single command with `--message`
- **Auto-commit**: Aider automatically commits changes with Git

### Tips for Android/Kotlin Dev

```bash
# Work on Android project
aider app/src/main/java/com/example/myapp/MainActivity.kt

# Fix Gradle build errors
aider build.gradle.kts --message "Fix this dependency error: <paste error>"

# Debug with ADB logs
adb logcat | Select-String "MyApp"
aider --message "Explain this crash log: <paste log>"
```

### Research with DuckDuckGo

DuckDuckGo search is installed for troubleshooting:

```bash
# Search from command line
ddgs "kotlin gradle build error missing dependency"

# Use in Aider - ask it to search for solutions
# Aider can help you research and apply fixes
```

### Complete AI Development Stack

| Tool | Purpose |
|------|---------|
| **Aider** | AI pair programming in terminal |
| **LM Studio** | Run local models (Qwen, etc.) |
| **DuckDuckGo CLI** | Privacy-focused research |
| **Git** | Version control (Aider auto-commits) |
| **Python 3.12** | Runtime for AI tools |

### Troubleshooting

**"Connection refused" error:**
- Make sure LM Studio server is running
- Check the port (default 1234)

**Model not responding:**
- Try a larger model (7B+)
- Increase context window in LM Studio settings

**Git errors:**
- Aider requires a Git repository
- Run `git init` in your project folder first
