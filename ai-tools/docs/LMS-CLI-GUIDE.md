# LM Studio CLI (lms) + Settings Files - Complete Configuration

## ✅ What I CAN Configure (Automated)

### 1. LM Studio settings.json (Automated)
**File:** `C:\Users\mulfa\.lmstudio\settings.json`

**Run this to apply:**
```bash
powershell -ExecutionPolicy Bypass -File "ai-tools\configure-lmstudio-settings.ps1"
```

**What it configures:**
- `defaultContextLength: 4096` - Default context for all models
- `developerMode: true` - Enable advanced controls
- `showExperimentalFeatures: true` - Show GPU options
- `modelLoadingGuardrails.customThresholdBytes: 4294967296` - 4GB VRAM limit
- `jitModelTTL.ttlSeconds: 3600` - Keep model loaded 1 hour

### 2. Per-Model GPU Config (Automated)
**File:** `C:\Users\mulfa\.lmstudio\user-model-configs\gpu-config.json`

**Created automatically with:**
```json
{
  "imported-models/uncategorized/qwen-coder-unlimited*": {
    "gpu_layers": 99,
    "context_length": 4096,
    "batch_size": 512,
    "flash_attn": false,
    "n_threads": 4
  }
}
```

### 3. Ollama Environment (Automated)
**File:** `C:\Users\mulfa\.ollama\.env`

```bash
OLLAMA_MAX_VRAM=4294967296
OLLAMA_NUM_GPU=99
OLLAMA_GPU_LAYERS=99
OLLAMA_CONTEXT_LENGTH=4096
OLLAMA_BATCH_SIZE=512
```

---

## 🔧 What `lms` CLI Can Do

### Model Management
```bash
# List models on disk
lms ls

# List loaded models
lms ps

# Load a model (uses settings from config files)
lms load imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf

# Unload a model
lms unload imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf

# Import a new model
lms import path\to\model.gguf
```

### Server Control
```bash
# Start server
lms server start

# Stop server
lms server stop

# Check server status
lms server status
```

### Chat
```bash
# Start interactive chat
lms chat imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf

# One-shot prompt
lms chat imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf -p "Hello!"
```

### Runtime Management
```bash
# List installed engines
lms runtime ls

# Survey hardware
lms runtime survey

# Select engine
lms runtime select
```

---

## 📁 Configuration Files Locations

| File | Purpose | Edit Method |
|------|---------|-------------|
| `~/.lmstudio/settings.json` | Global settings | Script or manual |
| `~/.lmstudio/user-model-configs/` | Per-model GPU settings | Script or JSON |
| `~/.ollama/.env` | Ollama environment | Script or manual |
| `~/.lmstudio/extensions/backends/` | Backend engines | Manual (advanced) |

---

## 🔧 Manual GPU Configuration (Required)

### For Quadro P1000 (4GB VRAM):

1. **Open LM Studio**

2. **Go to Settings → Model Settings**

3. **Apply These Settings:**
   ```
   GPU Offload:      ████████████████████ MAX (slide all the way right)
   Context Length:   4096
   Batch Size:       512
   Flash Attention:  Off (not supported on Pascal)
   ```

4. **Save and Load Model**

---

## 📊 Current Hardware Status

Run this to check:
```bash
lms runtime survey
```

Your output:
```
GPU/ACCELERATORS                VRAM
Quadro P1000 (CUDA, Discrete)   4.00 GiB

CPU: x86_64 (AVX, AVX2)
RAM: 15.94 GiB
```

---

## 🚀 Quick Configuration Script

Run this batch file to see current status:
```bash
ai-tools\lms-configure.bat
```

---

## 📝 Model Loading with Settings

When you load a model via CLI, it uses the **last saved GUI settings**:

```bash
# This uses whatever GPU settings you last set in GUI
lms load imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf
```

**To change GPU settings:**
1. Open LM Studio GUI
2. Adjust settings
3. Load model (GUI or CLI)
4. Settings persist for that model

---

## 🎯 Recommended Workflow

### First Time Setup:
1. **Run optimizer script** (Admin)
   ```bash
   optimize-as-admin.bat
   ```

2. **Open LM Studio GUI**
   - Apply GPU settings manually
   - Load your model once
   - Settings are saved

3. **After that, use CLI:**
   ```bash
   lms load imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf
   lms chat
   ```

### Daily Use:
```bash
# Just load and chat
lms chat imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf
```

---

## 🔍 Checking Model Status

```bash
# See what's loaded
lms ps

# Output example:
# IDENTIFIER                                                        STATUS    CONTEXT    DEVICE
# imported-models/uncategorized/qwen-coder-unlimited.q4_k_m.gguf    IDLE      4096       Local
```

The `CONTEXT` column shows your context length setting.

---

## 📚 Documentation

- Official LM Studio CLI docs: https://lmstudio.ai/docs/developer
- CLI commands: `lms --help`
- Runtime commands: `lms runtime --help`

---

**TL;DR:** Run `lms runtime survey` to check GPU, then manually set GPU Offload to MAX in LM Studio GUI once, and CLI will use those settings forever (per model).
