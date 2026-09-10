# Threat Model

## System considered

A generic enterprise LLM application with:

- a user-facing chat interface;
- retrieval-augmented generation (RAG);
- access to internal knowledge;
- optional tools or APIs;
- centralized identity and logging.

## Assets

- confidential enterprise data;
- user identity and authorization context;
- system/developer instructions;
- model and application configuration;
- API credentials;
- business records accessible through tools;
- security logs and audit trails.

## Trust boundaries

1. User input -> application
2. Retrieved content -> model context
3. Model output -> tool router
4. Tool router -> enterprise APIs
5. External model/provider -> enterprise environment

## Example threats

### Direct prompt injection

An attacker places instructions in the user prompt intended to override application policy.

**Controls**

- input classification;
- separation of instructions from data;
- least-privileged tool interfaces;
- deterministic authorization outside the model.

### Indirect prompt injection

Malicious instructions are embedded in content retrieved from a document, website or knowledge base.

**Controls**

- treat retrieved content as untrusted;
- scan and label retrieved material;
- constrain which retrieved content can influence tool invocation;
- apply provenance and source controls.

### Excessive agency

The model is allowed to execute actions beyond what is necessary for the task.

**Controls**

- allow-listed tools;
- narrow tool schemas;
- transaction limits;
- human approval for sensitive actions;
- independent authorization checks.

### Sensitive-information disclosure

The model returns data that the user is not authorized to access.

**Controls**

- authorization before retrieval;
- attribute-aware filtering;
- output checks for sensitive data;
- audit logging and alerting.

## Security principle

**The model should not be the final authority for security decisions.**

Authorization, data access, transaction approval and other high-impact controls should be enforced by deterministic application components outside the model.
