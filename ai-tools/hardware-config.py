# AI Tools Hardware Optimization
# For: NVIDIA Quadro P1000 (4GB VRAM, Pascal)
# ============================================

HARDWARE_PROFILE = "nvidia_quadro_p1000_4gb"

# LM Studio Settings (manual - apply in GUI)
LM_STUDIO_SETTINGS = {
    "gpu_offload": "MAX",           # Slide to maximum
    "context_length": 4096,         # Don't exceed this
    "batch_size": 512,              # Lower = more stable
    "flash_attention": False,       # Not supported on Pascal
    "mmap": True,                   # Memory mapped files
}

# Ollama Settings
OLLAMA_SETTINGS = {
    "OLLAMA_MAX_VRAM": "4294967296",  # 4GB
    "OLLAMA_NUM_GPU": "99",           # Use all GPU layers
    "OLLAMA_GPU_LAYERS": "99",
    "OLLAMA_CONTEXT_LENGTH": "4096",
    "OLLAMA_BATCH_SIZE": "512",
    "OLLAMA_KEEP_ALIVE": "24h",
}

# Safe Workspace Settings
SAFE_WORKSPACE_SETTINGS = {
    "max_context_tokens": 4096,      # Match VRAM limits
    "model_quantization": "Q4_K_M",  # Best speed/quality balance
    "backup_compression": True,      # Save disk space
}

# Recommended Models for P1000
RECOMMENDED_MODELS = [
    "Qwen2.5-Coder-3B-Instruct-Q4_K_M",  # Fast (~15-20 t/s)
    "Qwen2.5-7B-Instruct-Q4_K_M",        # Balanced (~5-8 t/s)
    "Qwen2.5-7B-Instruct-Q2_K",          # Faster (~10-12 t/s)
    "Qwen3-4B-abliterated-q4_k_m",       # Good middle ground
]

# Models to AVOID (too big for 4GB)
AVOID_MODELS = [
    "*-14B-*",
    "*-32B-*",
    "*-70B-*",
    "*-Q8_*",  # Q8 is too VRAM-heavy
]

# Performance Tips
TIPS = [
    "Close Chrome/Edge before running LLMs (they eat VRAM)",
    "Use Q4_K_M quantization for best balance",
    "Keep context length under 4096",
    "Run only one LLM at a time",
    "Use Studio Driver, not Game Ready Driver",
]
