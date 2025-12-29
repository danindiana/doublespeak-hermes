#!/bin/bash
# Quick run script for Doublespeak with Ollama

VENV="/home/jeb/programs/python_programs/venv"
SCRIPT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/example_usage_ollama_direct.py"

# Check if Ollama is running
echo "Checking Ollama connection..."
if ! curl -s http://localhost:11434 > /dev/null 2>&1; then
    echo "✗ Ollama is not running!"
    echo "  Start it with: ollama serve"
    exit 1
fi

echo "✓ Ollama is running"

# Check if venv exists
if [ ! -d "$VENV" ]; then
    echo "✗ Virtual environment not found at $VENV"
    exit 1
fi

echo "✓ Virtual environment found"

# Run the script
echo ""
echo "Running Doublespeak with Ollama..."
"$VENV/bin/python" "$SCRIPT" "$@"
