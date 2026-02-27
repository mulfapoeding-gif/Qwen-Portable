# ⚡ LFM2-1.2B - Your Quick Small Model

## ✅ Model Status:

| Property | Value |
|----------|-------|
| **File** | LFM2-1.2B-Q8_0.gguf |
| **Size** | 1.2 GB |
| **Quantization** | Q8_0 (Near lossless) |
| **Expected Speed** | 60-100 tokens/s ⚡⚡⚡ |
| **Best For** | Quick tasks, testing, simple Q&A |

---

## 🚀 Quick Launch Commands:

### llama.cpp (Fastest):
```bash
llama-server -m "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\LFM2-1.2B-Q8_0.gguf" -ngl 99 -c 2048 --port 8090
```

### Ollama Import:
```bash
# Create Modelfile
cat > Modelfile-lfm2 << EOF
FROM C:/Users/mulfa/.lmstudio/models/imported-models/uncategorized/LFM2-1.2B-Q8_0.gguf

PARAMETER num_ctx 2048
PARAMETER num_batch 512
PARAMETER temperature 0.7

SYSTEM """You are a fast, helpful assistant."""
EOF

# Import to Ollama
ollama create lfm2-1.2b-fast -f Modelfile-lfm2
```

### LM Studio:
```
1. Open LM Studio
2. Load Model → LFM2-1.2B-Q8_0.gguf
3. Start Server (port 1234)
```

---

## 📊 Performance Expectations:

| Platform | Load Time | Inference Speed |
|----------|-----------|-----------------|
| **llama.cpp** | ~1 second | 60-100 t/s ⚡⚡⚡ |
| **Ollama** | ~1 second | 50-80 t/s ⚡⚡ |
| **LM Studio** | ~3 seconds | 40-60 t/s ⚡ |

---

## 🎯 Best Use Cases:

✅ **Quick questions** - Instant responses  
✅ **Testing prompts** - Fast iteration  
✅ **Simple code** - Basic snippets  
✅ **Grammar/spell check** - Very fast  
✅ **Translation** - Quick translations  

❌ **Complex reasoning** - Too small  
❌ **Large code projects** - Limited knowledge  
❌ **Nuanced tasks** - May miss details  

---

## 🔧 Optimized Settings:

### For llama.cpp:
```bash
llama-server \
  -m "LFM2-1.2B-Q8_0.gguf" \
  -ngl 99 \
  -c 2048 \
  --batch-size 512 \
  -t 4 \
  --port 8090
```

### For Ollama:
```bash
ollama run lfm2-1.2b-fast "hello"
```

### For LM Studio:
```
Settings → Model Settings:
- Context: 2048
- GPU Offload: MAX
- Batch Size: 512
```

---

## 📁 Quick Launch Script:

```bash
@echo off
echo Starting LFM2-1.2B (Fast Model)...
llama-server -m "C:\Users\mulfa\.lmstudio\models\imported-models\uncategorized\LFM2-1.2B-Q8_0.gguf" -ngl 99 -c 2048 --batch-size 512 --port 8090
pause
```

Save as: `ai-tools\launch-lfm2-fast.bat`

---

**This is your FASTEST model - use for quick tasks!** ⚡
