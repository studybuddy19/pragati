import pickle
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForMaskedLM, AutoModelForQuestionAnswering

# Load the FLAN-T5 model and tokenizer for question generation
flan_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
flan_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")

# Load the DistilBERT model and tokenizer for question answering
qa_model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")
qa_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")

# Load the RoBERTa model and tokenizer for generating distractors
mlm_model = AutoModelForMaskedLM.from_pretrained("roberta-base")
mlm_tokenizer = AutoTokenizer.from_pretrained("roberta-base")

# Save the models and tokenizers to .pkl files
def save_model_to_pkl(model, tokenizer, model_name):
    with open(f"{model_name}_model.pkl", "wb") as model_file:
        pickle.dump(model, model_file)
    with open(f"{model_name}_tokenizer.pkl", "wb") as tokenizer_file:
        pickle.dump(tokenizer, tokenizer_file)
    print(f"{model_name} and tokenizer saved successfully.")

# Save all models and tokenizers
save_model_to_pkl(flan_model, flan_tokenizer, "flan_t5")
save_model_to_pkl(qa_model, qa_tokenizer, "distilbert_qa")
save_model_to_pkl(mlm_model, mlm_tokenizer, "roberta_mlm")
