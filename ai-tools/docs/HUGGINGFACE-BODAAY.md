# 🤗 Bodaay's HuggingFace Model Downloader

## ✅ Installed!

**Based on:** https://github.com/bodaay/HuggingFaceModelDownloader  
**Enhanced with:** Progress bars, better error handling, GGUF filtering

---

## 🚀 Quick Start:

### Download Nerdsking Python Coder 7B:
```bash
ai-tools\hf-download-bodaay.bat Nerdsking/Nerdsking-python-coder-7B-i
```

### Download Any Model:
```bash
# Basic
ai-tools\hf-download-bodaay.bat MODEL_ID

# With options
ai-tools\hf-download-bodaay.bat MODEL_ID -o models/ -f gguf

# Login for private models
ai-tools\hf-download-bodaay.bat --login
```

---

## 📥 Download Commands:

### Popular Python Coding Models:

```bash
# Nerdsking Python Coder 7B (BEST for Python)
hf-download-bodaay.bat Nerdsking/Nerdsking-python-coder-7B-i

# DeepSeek Coder 6.7B
hf-download-bodaay.bat deepseek-ai/deepseek-coder-6.7b-instruct

# StarCoder2 7B
hf-download-bodaay.bat bigcode/starcoder2-7b

# CodeLlama 7B Instruct
hf-download-bodaay.bat codellama/CodeLlama-7B-Instruct-hf

# Phi-2 (Small & Fast)
hf-download-bodaay.bat microsoft/phi-2
```

---

## ⚡ Features:

### 1. **Progress Bars**
```
  [########################################] 100% - 4.23 GB/4.23 GB - model.gguf
```

### 2. **GGUF Filtering**
- Only downloads `.gguf` files by default
- Skip unnecessary files (config, tokenizer, etc.)
- Faster downloads, less disk space

### 3. **Error Handling**
- Shows available files if no GGUF found
- Retry failed downloads
- Clear error messages

### 4. **Human-Readable Sizes**
```
  [########--------------------------------]  20% - 846.50 MB/4.23 GB
```

---

## 🎯 Usage Examples:

### Basic Download:
```bash
hf-download-bodaay.bat Nerdsking/Nerdsking-python-coder-7B-i
```

### Custom Output Directory:
```bash
hf-download-bodaay.bat MODEL_ID -o C:\Models\
```

### Different File Type:
```bash
# Download Safetensors instead
hf-download-bodaay.bat MODEL_ID -f safetensors
```

### Login for Private Models:
```bash
# First time login
hf-download-bodaay.bat --login

# Then download
hf-download-bodaay.bat private/model-id
```

---

## 📁 Download Location:

Models save to:
```
C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\MODEL_NAME\

Example:
C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\Nerdsking-python-coder-7B_i\
├── model.gguf          ← Use this!
├── config.json
└── tokenizer.json
```

---

## 🔧 After Download:

### 1. Use in LM Studio:
```
1. Open LM Studio
2. Load Model → Browse to folder
3. Select model.gguf
```

### 2. Import to Ollama:
```bash
# Create Modelfile
cat > Modelfile << EOF
FROM C:/Users/mulfa/.lmstudio/models/.../model.gguf
PARAMETER num_ctx 4096
PARAMETER temperature 0.7
SYSTEM """You are an expert Python programmer."""
EOF

# Import
ollama create nerdsking-coder -f Modelfile
```

### 3. Use with llama.cpp:
```bash
llama-server -m "model.gguf" -ngl 99 -c 4096 --port 8080
```

---

## 🆚 Comparison:

| Tool | Features | Best For |
|------|----------|----------|
| **hf-download-bodaay** | Progress bars, GGUF filter | GGUF models |
| **hf-download** (original) | Basic download | Any files |
| **huggingface-cli** | Official CLI | All HF operations |

---

## 🐛 Troubleshooting:

### "No GGUF files found"
```
The model might not have GGUF files.
Options:
1. Download safetensors: -f safetensors
2. Convert to GGUF using llama.cpp
3. Find GGUF version on HuggingFace
```

### "Download failed"
```
Check:
1. Model ID is correct (case-sensitive!)
2. Internet connection
3. Disk space
4. Model requires login: --login
```

### "Slow download"
```
- Large models take time
- Pause/resume is automatic
- Files are cached locally
```

---

## 📊 Your Downloaders:

| Tool | Command | Best For |
|------|---------|----------|
| **Bodaay's** | `hf-download-bodaay.bat` | GGUF models with progress |
| **Original** | `hf-download.bat` | General downloads |
| **Python** | `hf-downloader.py` | Scripting |

---

## ✅ Files Created:

| File | Purpose |
|------|---------|
| `hf-downloader-bodaay.py` | Enhanced downloader |
| `hf-download-bodaay.bat` | Quick launcher |
| `docs/HUGGINGFACE-BODAAY.md` | This guide |

---

## 🚀 Next Steps:

### 1. Download Nerdsking Python Coder:
```bash
ai-tools\hf-download-bodaay.bat Nerdsking/Nerdsking-python-coder-7B-i
```

### 2. Optimize After Download:
```bash
ai-tools\optimize-all-models.bat
```

### 3. Use in Your Workflow:
```bash
ollama run nerdsking-coder "Write a Python web scraper"
```

---

**Bodaay's HuggingFace Downloader is ready!** 🤗

**Download Nerdsking Python Coder:**
```bash
ai-tools\hf-download-bodaay.bat Nerdsking/Nerdsking-python-coder-7B-i
```
