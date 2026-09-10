# Findings - v0.2

## Objective

Version 0.2 introduces a repeatable evaluation harness for the prompt-injection detector.

The goal is not to demonstrate perfect detection. The goal is to make the behavior of a simple defensive control visible, testable and measurable.

## Findings

A rules-based detector can perform well on explicit attacks that resemble its implemented patterns. That should be interpreted cautiously because attackers can paraphrase, obfuscate, fragment or translate instructions, while benign security discussions can also contain attack terminology.

A lightweight detector can still be useful as one signal for telemetry, alerting, triage, quarantine or approval escalation. It should not be the sole security boundary.

## Key security lesson

The most important mitigation is architectural:

> Even if an attacker influences model output, the model should not automatically gain authority to perform sensitive actions.

Access control must remain outside the model; tool calls should be authorized independently; sensitive actions should use approval gates; retrieved documents should be treated as untrusted input; and security-relevant behavior should be logged.

## Next experiments

- paraphrased and obfuscated prompt injection;
- indirect attacks in retrieved documents;
- multilingual examples;
- adaptive adversarial cases;
- semantic classification;
- threshold trade-offs;
- tool-use attack simulations.
