# Doublespeak with Ollama (hermes3:8b)

This guide explains how to run the Doublespeak attack pipeline using Ollama's local `hermes3:8b` model instead of downloading large HuggingFace models.

## Setup

### 1. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 2. Install Ollama (if not already installed)

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**macOS:**
```bash
brew install ollama
```

**Windows:**
Download from https://ollama.ai/download

### 3. Pull the Model
```bash
ollama pull hermes3:8b
```

You can also use other models like:
- `ollama pull llama2`
- `ollama pull mistral`
- `ollama pull neural-chat`

### 4. Start Ollama Server
```bash
ollama serve
```

This starts Ollama on `http://localhost:11434` (default)

## Usage

### Using the Ollama Example Script

Run the attack with the local Ollama model:

```bash
python example_usage_ollama.py --model-name hermes3:8b
```

**Options:**
- `--model-name`: Ollama model name (default: `hermes3:8b`)
- `--harmful-keyword`: Harmful keyword to replace (default: `bomb`)
- `--benign-substitute`: Benign substitute word (default: `carrot`)
- `--num-examples`: Number of in-context examples (default: `10`)
- `--output-dir`: Directory to save outputs (default: `outputs`)
- `--device`: Device to use (default: `cuda` if available, else `cpu`)

**Examples:**

```bash
# Basic attack
python example_usage_ollama.py

# Custom keywords
python example_usage_ollama.py --harmful-keyword "explosives" --benign-substitute "apples"

# Use different model
python example_usage_ollama.py --model-name llama2

# Use HuggingFace model as fallback
python example_usage_ollama.py --use-huggingface --hf-model meta-llama/Llama-3.1-8B-Instruct
```

## How It Works

The project uses two model backends:

### Ollama Backend (Default)
- **Location:** `ollama_wrapper.py`
- **Advantages:**
  - Fast (model runs locally)
  - No downloads during test (if model already pulled)
  - Lower VRAM requirements
  - Good for testing/debugging
  - Works offline (after initial setup)

### HuggingFace Backend (Fallback)
- **Location:** `example_usage.py`
- **Advantages:**
  - Uses original implementation
  - Access to latest HuggingFace models
  - Better compatibility with analysis tools

## Troubleshooting

### Ollama Connection Error
```
✗ Could not connect to Ollama: ...
```

**Solution:** Make sure Ollama is running:
```bash
ollama serve
```

### Model Not Found
```
⚠ Model hermes3:8b not found locally. Pulling...
```

**Solution:** This will auto-pull the model, but you can also manually pull:
```bash
ollama pull hermes3:8b
```

### Out of Memory
If you get VRAM errors:
1. Stop other GPU processes
2. Use a smaller model: `ollama pull mistral` (7B instead of 8B)
3. Check GPU memory: `nvidia-smi`

### No GPU Available
The wrapper falls back to CPU, but it will be slower. Ensure CUDA is properly installed for GPU support.

## Requirements

See `requirements.txt` for all dependencies. Key additions for Ollama:
- `ollama>=0.1.0` - Python client for Ollama

## Files

- `ollama_wrapper.py` - Wrapper providing transformers-compatible interface to Ollama
- `example_usage_ollama.py` - Main script for running attacks with Ollama
- `OLLAMA_SETUP.md` - This file

## Original Files (Still Available)

The original doublespeak files remain unchanged:
- `doublespeak_attack.py` - Core attack implementation
- `mech_interp.py` - Mechanistic interpretability analysis
- `example_usage.py` - Original HuggingFace-based example

## References

- Doublespeak Attack: [Paper/Documentation]
- Ollama: https://ollama.ai
- Hermes3: https://huggingface.co/NousResearch/Hermes-3-Llama-3.1-8B
