"""
Ollama Wrapper for Doublespeak Attack
Provides a compatible interface to use Ollama models (like hermes3:8b)
instead of Hugging Face models
"""

import torch
import ollama
from typing import Optional, Dict, Any
import json

class OllamaModelWrapper:
    """Wraps ollama models to provide a transformers-like interface"""
    
    def __init__(self, model_name: str = "hermes3:8b", device: str = "cuda"):
        """
        Initialize the Ollama model wrapper
        
        Args:
            model_name: Ollama model name (e.g., "hermes3:8b")
            device: Device to use (for compatibility, ollama handles this)
        """
        self.model_name = model_name
        self.device = device
        self.client = ollama.Client()  # Uses default localhost:11434
        
        # Test connection
        try:
            response = self.client.list()
            print(f"✓ Connected to Ollama")
            models = response.get('models', [])
            model_names = [m['name'] for m in models]
            print(f"✓ Available models: {model_names}")
            
            if model_name not in model_names:
                print(f"⚠ Model {model_name} not found locally. Pulling...")
                self.client.pull(model_name)
        except Exception as e:
            print(f"✗ Could not connect to Ollama: {e}")
            print(f"  Make sure Ollama is running: ollama serve")
            raise
    
    def generate(self, 
                prompt: str,
                max_new_tokens: int = 100,
                temperature: float = 0.7,
                **kwargs) -> str:
        """
        Generate text using Ollama model
        
        Args:
            prompt: Input prompt
            max_new_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional arguments (for compatibility)
        
        Returns:
            Generated text
        """
        try:
            response = self.client.generate(
                model=self.model_name,
                prompt=prompt,
                stream=False,
                options={
                    'temperature': temperature,
                    'num_predict': max_new_tokens,
                }
            )
            return response['response']
        except Exception as e:
            print(f"✗ Generation error: {e}")
            raise
    
    def forward(self, input_ids: torch.Tensor, **kwargs) -> Dict[str, Any]:
        """
        Forward pass compatibility method
        Note: This is a simplified version for testing
        """
        # Decode input tokens
        input_text = "placeholder"  # Would need tokenizer
        
        # Generate output
        output_text = self.generate(input_text, max_new_tokens=50)
        
        # Return dict with logits (simplified)
        return {
            'logits': torch.zeros(1, 1, 128000),  # Placeholder
            'generated_text': output_text
        }
    
    def to(self, device: str) -> 'OllamaModelWrapper':
        """Compatibility method for device placement"""
        self.device = device
        return self
    
    @property
    def config(self):
        """Return a config object for compatibility"""
        class Config:
            hidden_size = 4096
            num_hidden_layers = 32
            vocab_size = 128000
        return Config()


class OllamaTokenizer:
    """Simple tokenizer wrapper for Ollama models"""
    
    def __init__(self, model_name: str = "hermes3:8b"):
        self.model_name = model_name
        self.pad_token_id = 0
        self.eos_token_id = 2
        self.pad_token = "[PAD]"
        self.eos_token = "[EOS]"
    
    def encode(self, text: str, return_tensors: Optional[str] = None) -> Any:
        """Encode text to token IDs (simplified)"""
        # This is a placeholder - real tokenization would use the model
        tokens = text.split()[:100]  # Simple word-based tokenization
        token_ids = [hash(t) % 128000 for t in tokens]
        
        if return_tensors == "pt":
            return torch.tensor([token_ids])
        return token_ids
    
    def decode(self, token_ids: torch.Tensor, skip_special_tokens: bool = False) -> str:
        """Decode token IDs back to text (simplified)"""
        # This is a placeholder
        if isinstance(token_ids, torch.Tensor):
            token_ids = token_ids.tolist()
        return " ".join([f"token_{i}" for i in token_ids[0] if isinstance(token_ids[0], list)])
    
    def __call__(self, text: str, return_tensors: Optional[str] = None, **kwargs) -> Dict:
        """Tokenizer call method"""
        input_ids = self.encode(text, return_tensors=return_tensors)
        
        if return_tensors == "pt":
            return {
                'input_ids': input_ids,
                'attention_mask': torch.ones_like(input_ids)
            }
        
        return {
            'input_ids': input_ids,
            'attention_mask': [1] * len(input_ids)
        }


def load_ollama_model(model_name: str = "hermes3:8b", device: str = "cuda"):
    """
    Load an Ollama model with a compatible tokenizer
    
    Args:
        model_name: Ollama model name
        device: Device to use
    
    Returns:
        Tuple of (model, tokenizer)
    """
    print(f"\n{'='*60}")
    print(f"Loading Ollama model: {model_name}")
    print(f"{'='*60}")
    
    model = OllamaModelWrapper(model_name, device)
    tokenizer = OllamaTokenizer(model_name)
    
    print(f"✓ Model loaded successfully")
    print(f"✓ Tokenizer initialized")
    
    return model, tokenizer


if __name__ == "__main__":
    # Test the wrapper
    try:
        model, tokenizer = load_ollama_model("hermes3:8b")
        
        # Test generation
        prompt = "What is the capital of France?"
        response = model.generate(prompt, max_new_tokens=50)
        print(f"\nPrompt: {prompt}")
        print(f"Response: {response}")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure Ollama is running:")
        print("  ollama serve")
        print("\nAnd pull the model:")
        print("  ollama pull hermes3:8b")
