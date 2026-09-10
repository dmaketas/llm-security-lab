# LLM Security Lab

A small, practical laboratory for exploring security controls around LLM-enabled enterprise applications.

The project focuses on four areas:

1. **Prompt-injection detection**
2. **RAG input and retrieved-content validation**
3. **Tool-use / excessive-agency controls**
4. **Security logging and risk-oriented evaluation**

The aim is not to claim that simple pattern matching can "solve" LLM security. Instead, the repository demonstrates how multiple lightweight controls can be layered around an LLM application and tested systematically.

## Why this project

Enterprise AI systems increasingly connect language models to internal data, APIs, search systems and business workflows. That creates a larger attack surface than a standalone chatbot.

This lab explores practical questions such as:

- Can suspicious instructions in user input or retrieved documents be detected before they reach the model?
- Can an application distinguish ordinary user content from attempts to override system instructions?
- How should tool calls be constrained?
- What security events should be logged?
- How can AI-security controls be tested in a repeatable way?

## Current scope

The first version contains:

- a lightweight prompt-injection risk scorer;
- a retrieved-content scanner for RAG pipelines;
- a simple allow-list policy for tool invocation;
- unit tests covering benign and suspicious cases;
- example scripts showing how the controls can be used.

## Repository structure

```text
llm-security-lab/
├── README.md
├── pyproject.toml
├── .gitignore
├── src/
│   └── llm_security_lab/
│       ├── __init__.py
│       ├── prompt_injection.py
│       ├── rag_guard.py
│       └── tool_policy.py
├── tests/
│   ├── test_prompt_injection.py
│   ├── test_rag_guard.py
│   └── test_tool_policy.py
├── examples/
│   └── demo.py
└── docs/
    └── threat-model.md
```

## Quick start

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install the project:

```bash
pip install -e ".[dev]"
```

Run the example:

```bash
python examples/demo.py
```

Run the tests:

```bash
pytest
```

## Important limitations

This project is intentionally educational.

The detection logic is heuristic and will produce false positives and false negatives. In real systems, prompt-injection defenses should be layered with architectural controls such as least privilege, isolation of untrusted content, constrained tool interfaces, human approval for sensitive actions, monitoring, rate limits and strong identity/access controls.

## Planned additions

- attack/defense evaluation dataset;
- structured risk scoring;
- secure RAG reference architecture;
- LLM-as-judge evaluation experiments;
- model and supply-chain threat scenarios;
- mapping to common AI-security control frameworks.

## Author

Dimitris Maketas

Cybersecurity | AI Governance | Enterprise Architecture | Enterprise Applications
