import nltk
from sacrebleu.metrics import CHRF, BLEU
from nltk.translate.bleu_score import sentence_bleu
from difflib import SequenceMatcher

import json

with open('dataset_with_completions.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

def exact_match_score(generated, reference):
    return int(generated == reference)

exact_match_scores = [exact_match_score(example['generated_middle'], example['middle']) for example in dataset]
exact_match_avg = sum(exact_match_scores) / len(exact_match_scores)
print(f"Exact Match Score: {exact_match_avg}")

chrf_metric = CHRF()
chrf_scores = [chrf_metric.sentence_score(example['generated_middle'], [example['middle']]).score for example in dataset]
chrf_avg = sum(chrf_scores) / len(chrf_scores)
print(f"CHRF Score: {chrf_avg}")

bleu_metric = BLEU(effective_order=True)
bleu_scores = [bleu_metric.sentence_score(example['generated_middle'], [example['middle']]).score for example in dataset]
bleu_avg = sum(bleu_scores) / len(bleu_scores)
print(f"BLEU Score: {bleu_avg}")

def rouge_l_score(generated, reference):
    match = SequenceMatcher(None, generated, reference).find_longest_match(0, len(generated), 0, len(reference))
    longest_common_subsequence = match.size
    precision = longest_common_subsequence / len(generated) if generated else 0
    recall = longest_common_subsequence / len(reference) if reference else 0
    f1 = (2 * precision * recall) / (precision + recall) if precision + recall > 0 else 0
    return f1

rouge_l_scores = [rouge_l_score(example['generated_middle'], example['middle']) for example in dataset]
rouge_l_avg = sum(rouge_l_scores) / len(rouge_l_scores)
print(f"ROUGE-L Score: {rouge_l_avg}")