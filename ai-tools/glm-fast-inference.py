"""
GLM Model - Optimized Fast Inference
Uses transformers with GPU acceleration for your Quadro P1000
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import time

class GLMModel:
    """Optimized GLM model loader and runner"""
    
    def __init__(self, model_name="zai-org/GLM-5"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = None
        self.model = None
        self.pipe = None
        
    def load_fast(self):
        """Load model with optimizations for speed"""
        print(f"Loading GLM model: {self.model_name}")
        print(f"Device: {self.device}")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            trust_remote_code=True
        )
        
        # Load model with optimizations
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            trust_remote_code=True,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None,
            low_cpu_mem_usage=True
        )
        
        if self.device == "cpu":
            self.model = self.model.to(self.device)
        
        # Create optimized pipeline
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
        )
        
        print("✅ Model loaded!")
        
    def chat(self, message, max_tokens=256):
        """Quick chat with model"""
        messages = [
            {"role": "user", "content": message}
        ]
        
        start = time.time()
        outputs = self.pipe(messages, max_new_tokens=max_tokens)
        elapsed = time.time() - start
        
        response = outputs[0]['generated_text'][-1]['content']
        
        print(f"\n⏱️  Response time: {elapsed:.2f}s")
        print(f"\n🤖 GLM: {response}\n")
        
        return response
    
    def generate(self, prompt, max_tokens=256):
        """Generate text with full control"""
        messages = [
            {"role": "user", "content": prompt}
        ]
        
        inputs = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        )
        
        if self.device == "cuda":
            inputs = {k: v.to('cuda') for k, v in inputs.items()}
        
        start = time.time()
        outputs = self.model.generate(**inputs, max_new_tokens=max_tokens)
        elapsed = time.time() - start
        
        response = self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        )
        
        print(f"\n⏱️  Response time: {elapsed:.2f}s")
        print(f"\n🤖 GLM: {response}\n")
        
        return response


def main():
    """Interactive chat with GLM"""
    print("="*60)
    print("  GLM Model - Fast Inference")
    print("  Optimized for your Quadro P1000")
    print("="*60)
    print()
    
    model = GLMModel()
    model.load_fast()
    
    print("\nCommands:")
    print("  Type your message and press Enter")
    print("  'quit' or 'exit' to stop")
    print()
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        model.chat(user_input)


if __name__ == "__main__":
    main()
