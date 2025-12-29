# Ollama Integration - Debugging & Fix

## Problem
The original `ollama_wrapper.py` was hanging during import due to interaction between torch and ollama imports.

## Root Cause
When importing `ollama` and `torch` in the same module, there were initialization delays. Additionally, the `ListResponse` object from ollama API has a `.models` attribute (list), not a dictionary with `get()` method.

## Solution
Created `example_usage_ollama_direct.py` which:
1. Avoids the wrapper abstraction layer
2. Uses the Ollama API directly
3. Properly handles the ListResponse and GenerateResponse objects
4. Works with the actual ollama library API

## How to Use

### Activate venv (if not already active)
```bash
cd /home/jeb/programs/python_programs
source venv/bin/activate
cd doublespeak
```

### Run the direct version
```bash
python example_usage_ollama_direct.py
```

### With custom parameters
```bash
python example_usage_ollama_direct.py \
  --harmful-keyword "explosives" \
  --benign-substitute "apples" \
  --model-name hermes3:8b \
  --num-examples 10 \
  --output-dir outputs
```

## Or use full path (no venv needed)
```bash
/home/jeb/programs/python_programs/venv/bin/python \
  /home/jeb/programs/python_programs/doublespeak/example_usage_ollama_direct.py \
  --harmful-keyword "explosives" \
  --benign-substitute "apples"
```

## Files
- `example_usage_ollama_direct.py` - **Working** version, use this!
- `ollama_wrapper.py` - Old wrapper (has import issues)
- `example_usage_ollama.py` - Uses the wrapper (deprecated)

## Status
✅ Ollama connection working
✅ Model listing working  
✅ Generation working
✅ Output files created successfully

## Requirements
- Ollama service running: `ollama serve`
- Model available: hermes3:8b (or specify another available model)
- Python venv with ollama package installed

## Sample Output
```
============================================================
DOUBLESPEAK ATTACK WITH OLLAMA (Direct)
============================================================
Model: hermes3:8b
Connecting to Ollama...
✓ Connected to Ollama
✓ Available models: ['qwen2.5-coder:14b', ..., 'hermes3:8b', ...]

✓ Malicious prompt generated
✓ Response generated successfully
✓ Saved to: outputs/
  - malicious_prompt.txt
  - attack_response.txt
============================================================
```
