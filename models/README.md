# Models - Categorized AI Model Files

## Organization

Models are organized by family:

- qwen/ - Qwen family models (6 files)
- mistral/ - Mistral family models (1 file)
- wizardlm/ - WizardLM models (1 file)
- other/ - Other models (LFM2, CodeLlama, etc.)

## Your Models

### Qwen Models

| Model | Quantization | Size | Use |
|-------|--------------|------|-----|
| qwen-coder-unlimited | Q4_K_M | ~4GB | General coding |
| Qwen2.5-Coder-3B-Instruct | Q4_K_M | ~2GB | Fast coding (USB) |
| Qwen3-4B-abliterated | Q5_K_M | ~3GB | Complex tasks |
| qwen2.5-7B-instruct | Q2_K | ~4GB | Heavy reasoning |
| bootes-qwen3_coder-reasoning | Q4_K_M | ~4GB | Reasoning |

### Other Models

| Model | Family | Size | Use |
|-------|--------|------|-----|
| mistral-7b-instruct | Mistral | ~3GB | General |
| WizardLM-7B-uncensored | WizardLM | ~3GB | Uncensored |
| LFM2-1.2B | LFM2 | ~1GB | Fast inference |
| mycopilot-codellama | CodeLlama | ~3GB | Code completion |

## USB Backup

Only Qwen2.5-Coder-3B-Instruct-Q4_K_M.gguf is copied to USB for portability.

See ../docs/USB-BACKUP-GUIDE.md for details.
