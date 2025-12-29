# Doublespeak-Hermes: Local Ollama Integration

This is a fork of [1tux/doublespeak](https://github.com/1tux/doublespeak) with added support for running attacks using **Ollama's local hermes3:8b** model instead of downloading large HuggingFace models.

## Why This Fork?

The original Doublespeak requires downloading multi-gigabyte HuggingFace models. This fork enables:
- ✅ Fast local inference with Ollama
- ✅ No model downloads during testing
- ✅ Works offline (after initial setup)
- ✅ Lower VRAM requirements
- ✅ Perfect for development and debugging

## Quick Start

### 1. Prerequisites

```bash
# Install Ollama
# Download from https://ollama.ai

# Verify Ollama is running
ollama serve  # In one terminal

# Pull the model (one-time)
ollama pull hermes3:8b
```

### 2. Clone and Setup

```bash
# Clone this fork
git clone <your-github-fork-url> doublespeak-hermes
cd doublespeak-hermes

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run an Attack

```bash
# Using the convenience script
./RUN_ME.sh --harmful-keyword "explosives" --benign-substitute "apples"

# Or directly
python example_usage_ollama_direct.py --harmful-keyword "bomb" --benign-substitute "carrot"
```

## Files

### Core Implementation
- **example_usage_ollama_direct.py** - Main script (USE THIS!)
  - Direct Ollama API integration
  - No wrapper abstraction
  - Fully tested and working

### Utilities  
- **RUN_ME.sh** - Convenience script
- **ollama_wrapper.py** - Transformer-compatible wrapper (reference)
- **example_usage_ollama.py** - Alternative wrapper-based approach

### Documentation
- **OLLAMA_SETUP.md** - Complete setup guide
- **QUICK_START.md** - 3-step quick start
- **DEBUG_SUMMARY.txt** - Technical implementation details
- **OLLAMA_DEBUG_FIXED.md** - Debugging notes

## Usage Examples

### Basic Attack
```bash
python example_usage_ollama_direct.py
```

### Custom Keywords
```bash
python example_usage_ollama_direct.py \
  --harmful-keyword "explosives" \
  --benign-substitute "apples" \
  --num-examples 20
```

### Different Model
```bash
python example_usage_ollama_direct.py --model-name llama2
```

### Custom Output Directory
```bash
python example_usage_ollama_direct.py --output-dir my_results
```

## Features

- ✅ Local inference with hermes3:8b
- ✅ Works with any Ollama model
- ✅ Customizable keywords and substitutes
- ✅ Configurable output directories
- ✅ Connection verification
- ✅ Model availability checking

## Technical Details

### Why "Hermes"?

Hermes (Nous Research) is a capable 8B model well-suited for:
- Instruction following
- Fast inference
- Reasonable output quality
- Lower resource requirements

### Key Implementation

The solution directly uses the Ollama API:
```python
import ollama

client = ollama.Client(host="http://localhost:11434")
response = client.generate(
    model="hermes3:8b",
    prompt=prompt,
    stream=False
)
```

No wrapper complications - just direct API usage.

## Original Project

Based on: [1tux/doublespeak](https://github.com/1tux/doublespeak)

Original research on prompt injection and jailbreaking attacks.

## Changes from Original

1. Added Ollama integration for local inference
2. Added convenience scripts and documentation
3. Optimized for testing/debugging workflow
4. Added requirements.txt with ollama package

All original functionality remains available with HuggingFace models.

## Troubleshooting

### "Could not connect to Ollama"
- Make sure `ollama serve` is running in another terminal
- Check http://localhost:11434 is accessible

### "Model hermes3:8b not found"
- Pull the model: `ollama pull hermes3:8b`
- Or use a different model: `--model-name llama2`

### Out of Memory
- Use a smaller model: `ollama pull mistral`
- Or increase system RAM/VRAM

## Contributing

This is a fork for local development. To contribute improvements:

1. Test thoroughly with Ollama
2. Keep backwards compatibility with HuggingFace mode
3. Update documentation
4. Submit pull requests

## License

Same as original Doublespeak project.

---

**Status**: ✅ Fully tested and working with hermes3:8b

**Last Updated**: December 28, 2025
