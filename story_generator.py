from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import os

class StoryGenerator:
    def __init__(self, model_path='./local_gpt_neo_model'):
        # Check if the model path exists
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model path '{model_path}' does not exist. Ensure you have downloaded the model.")
        
        try:
            # Load the GPT-Neo model and tokenizer
            self.model = GPTNeoForCausalLM.from_pretrained(model_path)
            self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
            
            # Set pad_token to eos_token explicitly
            self.tokenizer.pad_token = self.tokenizer.eos_token
            self.model.config.pad_token_id = self.tokenizer.pad_token_id
        except Exception as e:
            raise RuntimeError(f"Error loading model or tokenizer: {e}")
    
    def generate_story(self, prompt, max_length=150):
        try:
            # Tokenize input prompt
            inputs = self.tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)
            
            # Generate story with improved settings
            outputs = self.model.generate(
                inputs['input_ids'], 
                attention_mask=inputs['attention_mask'],
                max_length=max_length, 
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.2,
                no_repeat_ngram_size=2,
                pad_token_id=self.tokenizer.pad_token_id
            )
            
            # Decode and return the generated story
            story = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return story
        except Exception as e:
            raise RuntimeError(f"Error during story generation: {e}")
