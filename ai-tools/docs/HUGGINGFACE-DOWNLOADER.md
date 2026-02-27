# 🤗 Hugging Face Model Downloader

## ✅ Installed!

**Tool:** `huggingface_hub`  
**Purpose:** Download any model from Hugging Face  
**Saves to:** Your models folder automatically

---

## 🚀 Quick Start:

### Option 1: Batch Script (Easiest)
```bash
# Download Nerdsking Python Coder 7B
ai-tools\hf-download.bat Nerdsking/Nerdsking-python-coder-7B-i

# Download any model
ai-tools\hf-download.bat microsoft/phi-2
```

### Option 2: Python Script
```bash
py -3.12 ai-tools\hf-downloader.py Nerdsking/Nerdsking-python-coder-7B-i
```

### Option 3: In Python Code
```python
from huggingface_hub import hf_hub_download

# Download specific file
file_path = hf_hub_download(
    repo_id="Nerdsking/Nerdsking-python-coder-7B-i",
    filename="model.gguf"
)
```

---

## 📥 Download Nerdsking Python Coder 7B:

**This model is PERFECT for Python coding!**

```bash
# Run this command:
ai-tools\hf-download.bat Nerdsking/Nerdsking-python-coder-7B-i
```

**Expected:**
- Size: ~4-7 GB (depending on quantization)
- Download time: 5-20 minutes (based on internet)
- Best for: Python code generation, debugging

---

## 🎯 Popular Python Coding Models:

| Model | Size | Quality | Download Command |
|-------|------|---------|------------------|
| **Nerdsking-python-coder-7B** | ~4 GB | ⭐⭐⭐⭐⭐ | `hf-download Nerdsking/Nerdsking-python-coder-7B-i` |
| **DeepSeek Coder 6.7B** | ~4 GB | ⭐⭐⭐⭐⭐ | `hf-download deepseek-ai/deepseek-coder-6.7b-instruct` |
| **StarCoder2 7B** | ~4 GB | ⭐⭐⭐⭐ | `hf-download bigcode/starcoder2-7b` |
| **CodeLlama 7B** | ~4 GB | ⭐⭐⭐⭐ | `hf-download codellama/CodeLlama-7B-Instruct-hf` |
| **Phi-2 (2.7B)** | ~2 GB | ⭐⭐⭐ | `hf-download microsoft/phi-2` |

---

## 📁 Downloaded Models Location:

```
C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\

└── Nerdsking-python-coder-7B_i/
    ├── model.gguf          ← Use this!
    ├── config.json
    ├── tokenizer.json
    └── ...
```

---

## 🔧 After Download:

### 1. Import to Ollama:
```bash
# Create Modelfile
cat > Modelfile-nerdsking << EOF
FROM C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/Nerdsking-python-coder-7B_i/model.gguf

PARAMETER num_ctx 4096
PARAMETER num_batch 1024
PARAMETER temperature 0.7

SYSTEM """You are an expert Python programmer. Write clean, efficient code."""
EOF

# Import
ollama create nerdsking-python-coder -f Modelfile-nerdsking
```

### 2. Use in LM Studio:
```
1. Open LM Studio
2. Load Model → Browse to downloaded folder
3. Select model.gguf
4. Start chatting!
```

### 3. Use with llama.cpp:
```bash
llama-server -m "Nerdsking-python-coder-7B_i/model.gguf" -ngl 99 -c 4096 --port 8095
```

---

## 🐛 Troubleshooting:

### "Model requires login"
```bash
# Login to Hugging Face
huggingface-cli login

# Or use Python:
py -3.12 -c "from huggingface_hub import login; login()"
```

### "Download failed"
```
Check:
1. Model ID is correct (case-sensitive!)
2. Internet connection
3. Enough disk space
4. Model exists on Hugging Face
```

### "Slow download"
```
- Large models take time (4GB = 10-30 min)
- Pause/resume is automatic
- Downloaded files are cached
```

---

## 📊 Your Downloaded Models:

| Model | Status | Location |
|-------|--------|----------|
| **Nerdsking-python-coder-7B** | ⏳ Ready to download | Use `hf-download` |
| LFM2-1.2B | ✅ Downloaded | Local |
| Qwen Coder | ✅ Downloaded | Local |
| CodeLlama | ✅ Downloaded | Local |

---

## 🎯 Quick Commands:

### Download Model:
```bash
ai-tools\hf-download.bat MODEL_ID
```

### List Available Models:
```bash
# Visit: https://huggingface.co/models
# Search for: "python coder", "code generation", etc.
```

### Login (for private models):
```bash
huggingface-cli login
```

---

## ✅ Files Created:

| File | Purpose |
|------|---------|
| `hf-downloader.py` | Python downloader script |
| `hf-download.bat` | Quick launcher |
| `docs/HUGGINGFACE-DOWNLOADER.md` | This guide |

---

## 🚀 Next Steps:

### 1. Download Nerdsking Python Coder:
```bash
ai-tools\hf-download.bat Nerdsking/Nerdsking-python-coder-7B-i
```

### 2. Import to Ollama:
```bash
ai-tools\ollama-import-optimized.bat
```

### 3. Use in Your Workflow:
```bash
ollama run nerdsking-python-coder "Write a Python function to scrape a website"
```

---

**Your Hugging Face downloader is ready!** 🤗

**Download Nerdsking Python Coder:** `ai-tools\hf-download.bat Nerdsking/Nerdsking-python-coder-7B-i`
