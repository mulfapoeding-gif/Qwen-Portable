# Multi-Model Setup Guide

## 🎯 Goal: Run 2+ Agents with Different Models

When running multiple AI agents together, using **different models** for each agent creates:
- More diverse perspectives
- Better collaboration (different strengths)
- More realistic multi-agent simulation

---

## ⚠️ LM Studio Limitation

**Free LM Studio:** Only loads **one model at a time** per instance

**Solutions:**

| Option | Complexity | Performance | Notes |
|--------|------------|-------------|-------|
| **A. Two LM Studio Instances** | Medium | Good | Requires 2x RAM |
| **B. LM Studio + Ollama** | Easy | Best | Recommended |
| **C. Single Model** | Easiest | Good | Less diversity |

---

## ✅ Option A: Two LM Studio Instances

### Step 1: Check if Your System Can Handle It

**Requirements:**
- **RAM:** 16GB+ recommended (7B model = ~5GB RAM each)
- **VRAM:** 12GB+ for GPU acceleration on both

### Step 2: Run Two Instances

**Method 1: Multiple Windows (if supported)**
```
1. Open LM Studio → Load Model A → Start Server (Port 1234)
2. Open another LM Studio window → Load Model B → Start Server (Port 1235)
```

**Method 2: LM Studio CLI (if available)**
```bash
# Instance 1
lms-server --port 1234 --model "Qwen-Coder"

# Instance 2
lms-server --port 1235 --model "Qwen-Chat"
```

### Step 3: Configure AutoGen

Edit `autogen_multi_model.py`:
```python
# Agent 1 - Port 1234
CODER_MODEL_CLIENT = OpenAIChatCompletionClient(
    base_url="http://localhost:1234/v1",
    ...
)

# Agent 2 - Port 1235
REVIEWER_MODEL_CLIENT = OpenAIChatCompletionClient(
    base_url="http://localhost:1235/v1",
    ...
)
```

---

## ✅ Option B: LM Studio + Ollama (RECOMMENDED)

### Step 1: Install Ollama

```bash
winget install Ollama.Ollama
```

### Step 2: Download Models

```bash
# Ollama runs on port 11434 by default
# Download a model for Ollama
ollama pull qwen2.5:7b

# LM Studio keeps your GGUF models
# Load a different model in LM Studio (port 1234)
```

### Step 3: Configure Agents

```python
# Coder uses LM Studio (your Qwen Coder GGUF)
CODER_MODEL_CLIENT = OpenAIChatCompletionClient(
    model="local-model",
    base_url="http://localhost:1234/v1",  # LM Studio
    api_key="not-needed",
)

# Reviewer uses Ollama (Qwen 2.5)
REVIEWER_MODEL_CLIENT = OpenAIChatCompletionClient(
    model="qwen2.5:7b",
    base_url="http://localhost:11434/v1",  # Ollama
    api_key="not-needed",
)
```

### Step 4: Run Both Servers

```bash
# Terminal 1: LM Studio
# (Start server from LM Studio UI - port 1234)

# Terminal 2: Ollama (already running as service)
ollama list  # Verify it's running

# Terminal 3: Run your agent
py -3.12 examples/autogen_multi_model.py
```

---

## ✅ Option C: Single Model (Quick Start)

Both agents use the **same LM Studio instance**:

```python
# Both agents use same base_url
CODER_MODEL_CLIENT = OpenAIChatCompletionClient(
    base_url="http://localhost:1234/v1",
    ...
)

REVIEWER_MODEL_CLIENT = OpenAIChatCompletionClient(
    base_url="http://localhost:1234/v1",  # Same!
    ...
)
```

**Pros:**
- Simplest setup
- Less RAM usage

**Cons:**
- Less diverse responses
- Agents may sound similar

---

## 🔧 Recommended Model Combinations

| Agent 1 | Agent 2 | Use Case |
|---------|---------|----------|
| **Qwen Coder** (7B) | **Qwen Chat** (7B) | Code + Planning |
| **Qwen Coder** (7B) | **Mistral** (7B) | Code + Review |
| **Qwen2.5** (7B) | **Qwen2.5** (3B) | Complex + Fast |
| **Llama 3** (8B) | **Qwen Coder** (7B) | General + Code |

---

## 📊 RAM Requirements

| Configuration | RAM Needed | VRAM Needed |
|---------------|------------|-------------|
| Single 7B model (Q4_K_M) | ~5 GB | ~4 GB |
| Two 7B models | ~10 GB | ~8 GB |
| 7B + 3B models | ~7 GB | ~6 GB |

**Tips:**
- Use Q4_K_M quantization for best RAM/performance balance
- Close other applications when running multiple models
- Consider using smaller models (3B) for one agent

---

## 🚀 Quick Test

### Test Both Servers

```bash
# Test LM Studio (port 1234)
curl http://localhost:1234/v1/models

# Test Ollama (port 11434)
curl http://localhost:11434/api/tags

# Test AutoGen script
py -3.12 examples/autogen_multi_model.py
```

### Expected Output

```
============================================================
🤖 AutoGen Multi-Agent System
============================================================

📋 Configuration:
   Coder Model:    http://localhost:1234 (LM Studio)
   Reviewer Model: http://localhost:11434 (Ollama)
   Planner Model:  http://localhost:1234 (LM Studio)

💬 Your task (or 'quit'): Create a Python function to sort a list

🔄 Agents collaborating...
------------------------------------------------------------

👤 Planner:
   I'll break this down into steps:
   1. Define function signature
   2. Choose sorting algorithm
   3. Implement and test

👤 Coder:
   Here's the code:
   ```python
   def sort_list(items):
       return sorted(items)
   ```

👤 Reviewer:
   Good simple solution! Consider:
   - Add type hints
   - Handle edge cases
   - Add docstring

------------------------------------------------------------
✅ Task complete!
```

---

## 🐛 Troubleshooting

### "Connection refused" on port 1235
- Second LM Studio instance not running
- Start another instance or use Ollama

### "Out of memory"
- Close one model
- Use smaller quantization (Q3_K_S)
- Use Option C (single model)

### Agents not responding
- Check both servers are running
- Verify `base_url` in code matches server ports
- Test with curl commands above

### Ollama not working
```bash
# Restart Ollama service
ollama serve

# Pull model again
ollama pull qwen2.5:7b
```

---

## 📝 Summary

**For best multi-agent experience:**

1. **Install Ollama** alongside LM Studio
2. **Load Qwen Coder** in LM Studio (port 1234)
3. **Load Qwen Chat** in Ollama (port 11434)
4. **Configure agents** with different `base_url`
5. **Run multi-agent** script

This gives you:
- ✅ Two different models
- ✅ Diverse agent personalities
- ✅ Better collaboration
- ✅ Reasonable RAM usage

---

**Next:** See `autogen_multi_model.py` for the complete example code!
