from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model(model_name="llama-3.1"):
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
