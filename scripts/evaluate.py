from __future__ import annotations
import csv
from pathlib import Path
from llm_security_lab.evaluation import evaluate_examples

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "prompt_injection_eval.csv"
CSV_OUTPUT = ROOT / "evaluation-results.csv"
REPORT_OUTPUT = ROOT / "evaluation-report.md"

def load_examples(path: Path):
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return [{"id": r["id"], "category": r["category"], "label": int(r["label"]), "text": r["text"]} for r in rows]

def main():
    examples = load_examples(DATASET)
    metrics, rows = evaluate_examples(examples, threshold=30)

    with CSV_OUTPUT.open("w", encoding="utf-8", newline="") as f:
        fields = ["id","category","label","text","predicted","score","level","indicators"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    errors = [r for r in rows if int(r["label"]) != int(r["predicted"])]
    report = [
        "# LLM Security Lab - Evaluation Report", "",
        "Detection threshold: **30**", "",
        "## Metrics", "",
        f"- True positives: {metrics.true_positive}",
        f"- True negatives: {metrics.true_negative}",
        f"- False positives: {metrics.false_positive}",
        f"- False negatives: {metrics.false_negative}",
        f"- Precision: {metrics.precision:.3f}",
        f"- Recall: {metrics.recall:.3f}",
        f"- F1: {metrics.f1:.3f}",
        f"- Accuracy: {metrics.accuracy:.3f}", "",
        "## Misclassified examples", "",
    ]
    if not errors:
        report.append("No misclassifications in this small evaluation set.")
    else:
        for r in errors:
            report += [
                f"### {r['id']} - {r['category']}", "",
                f"- Expected: {r['label']}",
                f"- Predicted: {r['predicted']}",
                f"- Score: {r['score']}",
                f"- Indicators: {r['indicators'] or 'none'}",
                f"- Text: `{r['text']}`", "",
            ]
    report += [
        "## Interpretation", "",
        "This dataset is intentionally small and should not be treated as a benchmark.",
        "Its purpose is to make detector behavior measurable and expose false positives and false negatives.",
        "Future versions should add indirect prompt injection, paraphrased attacks, multilingual examples and adaptive adversarial cases."
    ]
    REPORT_OUTPUT.write_text("\n".join(report), encoding="utf-8")

    print(f"Examples: {len(rows)}")
    print(f"Precision: {metrics.precision:.3f}")
    print(f"Recall: {metrics.recall:.3f}")
    print(f"F1: {metrics.f1:.3f}")
    print(f"Accuracy: {metrics.accuracy:.3f}")

if __name__ == "__main__":
    main()
