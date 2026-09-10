from dataclasses import dataclass
from typing import Iterable
from .prompt_injection import assess_prompt

@dataclass(frozen=True)
class EvaluationMetrics:
    true_positive: int
    true_negative: int
    false_positive: int
    false_negative: int
    precision: float
    recall: float
    f1: float
    accuracy: float

def _safe_div(a, b):
    return float(a / b) if b else 0.0

def evaluate_examples(examples: Iterable[dict], threshold: int = 30):
    if not 0 <= threshold <= 100:
        raise ValueError("threshold must be between 0 and 100")
    tp = tn = fp = fn = 0
    rows = []
    for example in examples:
        text = str(example["text"])
        expected = int(example["label"])
        result = assess_prompt(text)
        predicted = 1 if result.score >= threshold else 0
        if expected == 1 and predicted == 1: tp += 1
        elif expected == 0 and predicted == 0: tn += 1
        elif expected == 0 and predicted == 1: fp += 1
        elif expected == 1 and predicted == 0: fn += 1
        else: raise ValueError("label must be 0 or 1")
        rows.append({
            **example,
            "predicted": predicted,
            "score": result.score,
            "level": result.level,
            "indicators": ",".join(result.indicators),
        })
    precision = _safe_div(tp, tp + fp)
    recall = _safe_div(tp, tp + fn)
    f1 = _safe_div(2 * precision * recall, precision + recall)
    accuracy = _safe_div(tp + tn, tp + tn + fp + fn)
    return EvaluationMetrics(tp, tn, fp, fn, precision, recall, f1, accuracy), rows
