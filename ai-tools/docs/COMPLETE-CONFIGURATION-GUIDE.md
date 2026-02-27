# 🛠️ AI Tools - Complete Configuration Guide

## ✅ What's Been Configured (Research + Implementation)

### 1. Ollama - FULLY CONFIGURED ✅

**File:** `C:\Users\mulfa\.ollama\.env`

```bash
OLLAMA_MAX_VRAM=4294967296      # 4GB for P1000
OLLAMA_NUM_GPU=99               # All GPU layers
OLLAMA_GPU_LAYERS=99
OLLAMA_CONTEXT_LENGTH=4096
OLLAMA_BATCH_SIZE=512
OLLAMA_KEEP_ALIVE=24h
```

**Applied via:** `optimize-performance.ps1`

---

### 2. LM Studio - FULLY CONFIGURED ✅

**File:** `C:\Users\mulfa\.lmstudio\settings.json`

**Modified settings:**
```json
{
  "defaultContextLength": {
    "type": "custom",
    "value": 4096
  },
  "developerMode": true,
  "developer": {
    "showExperimentalFeatures": true,
    "jitModelTTL": {
      "enabled": true,
      "ttlSeconds": 3600
    }
  },
  "modelLoadingGuardrails": {
    "mode": "custom",
    "customThresholdBytes": 4294967296
  }
}
```

**Applied via:** `configure-lmstudio-settings.ps1`

---

### 3. Per-Model GPU Config - CREATED ✅

**File:** `C:\Users\mulfa\.lmstudio\user-model-configs\gpu-config.json`

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

---

### 4. System Environment Variables - OPTIONAL

**Applied via:** `optimize-admin.ps1` (requires Admin)

Sets machine-wide environment variables for all applications.

---

## 🚀 How to Apply All Settings

### Quick Method (One Command)
```bash
# Run as admin for full optimization
optimize-as-admin.bat

# Or without admin (most features still work)
ai-tools\optimize-all.bat
```

### Individual Scripts

| Script | Purpose | Requires Admin |
|--------|---------|----------------|
| `optimize-performance.ps1` | Ollama settings | No |
| `configure-lmstudio-settings.ps1` | LM Studio settings | No |
| `optimize-admin.ps1` | System env vars | **Yes** |
| `optimize-all.bat` | All of the above | Optional |

---

## 📊 Configuration Files Summary

| File | Tool | Purpose |
|------|------|---------|
| `~/.ollama/.env` | Ollama | GPU memory, layers, context |
| `~/.lmstudio/settings.json` | LM Studio | Global defaults, developer mode |
| `~/.lmstudio/user-model-configs/gpu-config.json` | LM Studio | Per-model GPU settings |
| `~/.lmstudio/models/` | LM Studio | Model storage |
| `ai-tools/` | All | Scripts and documentation |

---

## 🔍 Verification Commands

### Check Ollama Settings
```bash
# View .env file
type %USERPROFILE%\.ollama\.env

# Check environment variables
Get-ChildItem Env: | Where-Object { $_.Name -like "OLLAMA*" }
```

### Check LM Studio Settings
```bash
# View settings.json
type %USERPROFILE%\.lmstudio\settings.json

# Check GPU detection
lms runtime survey
```

### Check Model Status
```bash
# See loaded models
lms ps

# Load model with new settings
lms load imported-models/uncategorized/qwen-coder-unlimited.Q4_K_M.gguf
```

---

## 🎯 Expected Performance (Quadro P1000)

| Model | Quantization | Context | Speed |
|-------|--------------|---------|-------|
| Qwen2.5-Coder-3B | Q4_K_M | 4096 | ~15-20 t/s |
| Qwen-Coder-Unlimited | Q4_K_M | 4096 | ~8-12 t/s |
| Qwen3-4B | Q5_K_M | 4096 | ~6-10 t/s |
| Qwen2.5-7B | Q2_K | 4096 | ~10-12 t/s |

---

## 🔄 Rollback (If Needed)

### Restore LM Studio Settings
```bash
# Backup was created automatically
copy %USERPROFILE%\.lmstudio\settings.json.backup.* %USERPROFILE%\.lmstudio\settings.json
```

### Restore Ollama Settings
```bash
# Delete .env file
del %USERPROFILE%\.ollama\.env
```

---

## 📚 Research Findings

### What We Discovered

1. **LM Studio stores settings in JSON files** - NOT binary/encrypted
   - `settings.json` for global config
   - `user-model-configs/` for per-model settings

2. **Ollama uses `.env` file** - Simple text file with environment variables

3. **`lms` CLI has limited config options** - But reads from config files automatically

4. **GPU settings are applied when model loads** - Config files control this

5. **Developer mode unlocks advanced options** - Enabled via settings.json

---

## 🎓 Key Learnings

### Before Research:
- ❌ "LM Studio settings are binary/encrypted"
- ❌ "CLI cannot configure GPU settings"
- ❌ "Must use GUI for everything"

### After Research:
- ✅ `settings.json` is plain text - fully editable
- ✅ Per-model configs in `user-model-configs/`
- ✅ Scripts can apply all settings automatically
- ✅ CLI reads from config files automatically

---

## 🔧 Advanced Configuration

### Add More Models to GPU Config

Edit `~/.lmstudio/user-model-configs/gpu-config.json`:

```json
{
  "imported-models/uncategorized/qwen-coder-unlimited*": {
    "gpu_layers": 99,
    "context_length": 4096,
    "batch_size": 512
  },
  "imported-models/uncategorized/Qwen3-4B*": {
    "gpu_layers": 99,
    "context_length": 4096,
    "batch_size": 256
  },
  "imported-models/uncategorized/Qwen2.5-Coder-3B*": {
    "gpu_layers": 99,
    "context_length": 8192,
    "batch_size": 512
  }
}
```

### Adjust for Different VRAM

Edit `~/.ollama/.env`:

```bash
# For 2GB VRAM
OLLAMA_MAX_VRAM=2147483648
OLLAMA_CONTEXT_LENGTH=2048
OLLAMA_BATCH_SIZE=256

# For 6GB VRAM
OLLAMA_MAX_VRAM=6442450944
OLLAMA_CONTEXT_LENGTH=8192
OLLAMA_BATCH_SIZE=1024

# For 8GB+ VRAM
OLLAMA_MAX_VRAM=8589934592
OLLAMA_CONTEXT_LENGTH=16384
OLLAMA_BATCH_SIZE=2048
```

---

## 📖 Additional Resources

- **LM Studio Docs:** https://lmstudio.ai/docs/developer
- **Ollama Docs:** https://ollama.ai/docs
- **Your Configs:** `ai-tools/docs/` folder
- **Hardware Survey:** Run `lms runtime survey`

---

## ✅ Summary

**You now have:**
- ✅ Ollama fully configured for P1000
- ✅ LM Studio settings optimized
- ✅ Per-model GPU configs created
- ✅ Scripts to re-apply anytime
- ✅ Full documentation of what was done
- ✅ Rollback capability

**Run this to apply everything:**
```bash
optimize-as-admin.bat
```

**Then restart and test:**
```bash
lms runtime survey
lms chat imported-models/uncategorized/qwen-coder-unlimited.Q4_K_M.gguf
```

---

**Your Quadro P1000 is now fully optimized for AI workloads!** 🚀
