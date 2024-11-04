import os
import json
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    if torch.cuda.is_available():
        model.to('cuda')
    return tokenizer, model

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_completion(prefix, tokenizer, model, max_length=50):
    inputs = tokenizer(prefix, return_tensors="pt")
    input_ids = inputs["input_ids"]
    if torch.cuda.is_available():
        input_ids = input_ids.to('cuda')
    with torch.no_grad():
        outputs = model.generate(
            input_ids,
            max_length=input_ids.shape[1] + max_length,
            temperature=0.7,
            top_p=0.9,
            do_sample=True,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id
        )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    completion = generated_text[len(prefix):]
    return completion.strip()

def main():
    if len(sys.argv) < 3:
        print("Usage: python run_tiny_starcoder.py <dataset.json> <output.json>")
        sys.exit(1)
    
    dataset_file = sys.argv[1]
    output_file = sys.argv[2]
    model_name = "bigcode/tiny_starcoder_py"  

    print("Chargement du modèle...")
    tokenizer, model = load_model(model_name)
    print("Modèle chargé.")

    print("Chargement du dataset...")
    dataset = load_dataset(dataset_file)
    print(f"{len(dataset)} exemples chargés.")

    print("Génération des complétions...")
    for idx, example in enumerate(dataset, start=1):
        prefix = example['prefix']
        actual_middle = example['middle']
        generated_middle = generate_completion(prefix, tokenizer, model)
        example['generated_middle'] = generated_middle
        print(f"Exemple {idx}/{len(dataset)}: Généré.")

    print("Sauvegarde des complétions générées...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=4, ensure_ascii=False)
    print(f"Jeu de données sauvegardé dans {output_file}.")

if __name__ == "__main__":
    main()