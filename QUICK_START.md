# Quick Start - Doublespeak with Ollama

## Prerequisites
- ✓ Virtual environment activated: `/home/jeb/programs/python_programs/venv`
- ✓ Requirements installed: torch, transformers, ollama, etc.
- ✓ Ollama installed on your system

## 1. Start Ollama Server (Terminal 1)
```bash
ollama serve
```

## 2. Pull the hermes3:8b Model (Terminal 2)
```bash
ollama pull hermes3:8b
```

## 3. Run Doublespeak Attack (Terminal 2, after model pulls)
```bash
cd /home/jeb/programs/python_programs/doublespeak
source venv/bin/activate
python example_usage_ollama.py
```

## What Gets Generated
- `outputs/malicious_prompt.txt` - The jailbreak prompt
- `outputs/attack_response.txt` - Model's response to the attack

## Available Options

```bash
# Use different harmful keyword
python example_usage_ollama.py --harmful-keyword "explosives" --benign-substitute "apples"

# Use a different Ollama model
python example_usage_ollama.py --model-name llama2

# Run with more examples
python example_usage_ollama.py --num-examples 20

# Save outputs to custom directory
python example_usage_ollama.py --output-dir my_outputs
```

## Status
- ✓ venv activated
- ✓ Packages installed (ollama 0.6.1, torch 2.7.1, transformers 4.57.1)
- ✓ ollama_wrapper.py created
- ✓ example_usage_ollama.py created
- ✓ requirements.txt updated with ollama>=0.1.0

## Next Steps
1. Make sure Ollama is running (`ollama serve`)
2. Run: `python example_usage_ollama.py`
3. Check `outputs/` directory for results

For more details, see `OLLAMA_SETUP.md`
