from transformers import GPTNeoForCausalLM, GPT2Tokenizer

def save_model(model_name='EleutherAI/gpt-neo-1.3B', save_directory='./local_gpt_neo_model'):
    # Load the GPT-Neo model and tokenizer
    model = GPTNeoForCausalLM.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    
    # Save model and tokenizer locally
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)

    print(f"Model and tokenizer have been saved to {save_directory}")

if __name__ == "__main__":
    save_model()
