# LLM Security Lab

Practical experiments for securing LLM-enabled enterprise applications.

**Version:** 0.2.0

This repository explores how lightweight defensive controls can be layered around LLM applications and evaluated systematically. It focuses on prompt injection, RAG security, tool-use controls, security logging, and measurable attack/defence testing.

## What is new in v0.2

Version 0.2 adds:

- an attack/defence evaluation dataset;
- automated precision, recall, F1 and confusion-matrix metrics;
- CSV and Markdown evaluation reports;
- security-event logging examples;
- expanded RAG and tool-use controls;
- more unit tests;
- GitHub Actions CI;
- a documented findings report and roadmap.

## Security questions explored

- How well can a simple transparent detector distinguish benign prompts from prompt-injection attempts?
- What happens when malicious instructions arrive through retrieved RAG content rather than directly from the user?
- How should tool invocation be constrained independently of model output?
- What should be logged when an AI-security control detects suspicious behavior?
- How can security controls be evaluated repeatably rather than demonstrated only through hand-picked examples?

## Repository structure

```text
llm-security-lab/
├── .github/workflows/tests.yml
├── data/prompt_injection_eval.csv
├── docs/findings-v0.2.md
├── docs/threat-model.md
├── examples/demo.py
├── examples/security_logging_demo.py
├── scripts/evaluate.py
├── src/llm_security_lab/
│   ├── __init__.py
│   ├── evaluation.py
│   ├── prompt_injection.py
│   ├── rag_guard.py
│   ├── security_logging.py
│   └── tool_policy.py
└── tests/
```

## Quick start

```bash
python -m venv .venv
```

Activate the environment and install:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

Run the demo:

```bash
python examples/demo.py
```

Run the evaluation:

```bash
python scripts/evaluate.py
```

The evaluation script produces `evaluation-results.csv` and `evaluation-report.md`.

## Detection model

The detector is intentionally deterministic, transparent and easy to inspect. It looks for suspicious patterns such as:

- instruction override;
- requests for hidden/system instructions;
- role or policy replacement;
- credential/secret exfiltration;
- attempts to influence tool execution;
- attempts to bypass authorization or safety constraints.

This is **not** a production prompt-injection solution. The point of the lab is to make the strengths and limitations measurable.

## Design principle

> The model should not be the final authority for security decisions.

Authorization, sensitive tool execution, data access and high-impact transactions should be enforced by deterministic components outside the model.

## Evaluation

The dataset includes benign and adversarial examples. Metrics include:

- true positives;
- true negatives;
- false positives;
- false negatives;
- precision;
- recall;
- F1;
- accuracy.

## Enterprise AI security perspective

A secure LLM application should combine controls across:

1. Identity and authorization
2. Data access and retrieval
3. Prompt/context handling
4. Model interaction
5. Tool and API invocation
6. Output handling
7. Monitoring and audit
8. Human approval for high-impact actions

## Limitations

This project is educational and experimental. Real deployments should use layered defenses including least privilege, authorization outside the model, isolation of untrusted content, constrained tool interfaces, approval gates, provenance controls, monitoring and adversarial testing.

## Roadmap

Planned additions:

- indirect prompt-injection corpus;
- paraphrased and multilingual attacks;
- semantic detection experiments;
- secure RAG reference architecture;
- agent/tool abuse scenarios;
- AI supply-chain threats;
- mapping to OWASP LLM, MITRE ATLAS, NIST AI RMF and ISO/IEC 42001 concepts.

## Author

**Dimitris Maketas**

Cybersecurity | AI Governance | Enterprise Architecture | Enterprise Applications
