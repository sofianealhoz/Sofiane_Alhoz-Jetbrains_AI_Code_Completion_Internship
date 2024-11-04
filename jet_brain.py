import os
import json
import random
import sys

def collect_code_files(dir_path, extensions=None):
    if extensions is None:
        extensions = ['.py', '.js', '.java', '.cpp', '.c', '.rb', '.go', '.ts']
    
    code_files = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                code_files.append(os.path.join(root, file))
    return code_files

def create_examples(file_path, max_per_file=5, total_limit=50):
    examples = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.readlines()
    except Exception as e:
        print(f"Erreur en lisant {file_path}: {e}")
        return examples
    
    if len(content) < 3:
        return examples
    
    possible_positions = list(range(1, len(content) - 1))
    selected = random.sample(possible_positions, min(max_per_file, len(possible_positions)))
    
    for pos in selected:
        prefix = ''.join(content[:pos])
        middle = content[pos].strip()
        suffix = ''.join(content[pos+1:])
        
        if middle:
            examples.append({
                'file_path': file_path,
                'prefix': prefix,
                'middle': middle,
                'suffix': suffix
            })
        
        if len(examples) >= total_limit:
            break
    return examples

def build_dataset(repo_path, output_json, desired_examples=50, per_file=5):
    files = collect_code_files(repo_path)
    print(f"Trouvé {len(files)} fichiers de code.")
    
    dataset = []
    for file in files:
        new_examples = create_examples(file, per_file, desired_examples)
        dataset.extend(new_examples)
        print(f"Ajout de {len(new_examples)} exemples depuis {file}.")
        if len(dataset) >= desired_examples:
            break
    
    dataset = dataset[:desired_examples]
    
    try:
        with open(output_json, 'w', encoding='utf-8') as out_file:
            json.dump(dataset, out_file, indent=2, ensure_ascii=False)
        print(f"Jeu de données sauvegardé dans {output_json} avec {len(dataset)} exemples.")
    except Exception as e:
        print(f"Erreur en écrivant le fichier JSON: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_dataset.py <chemin_dépôt> <fichier_sortie.json> [nombre_exemples] [exemples_par_fichier]")
        sys.exit(1)
    
    repo = sys.argv[1]
    output = sys.argv[2]
    num = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    per_file = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    
    build_dataset(repo, output, num, per_file)

if __name__ == "__main__":
    main()




