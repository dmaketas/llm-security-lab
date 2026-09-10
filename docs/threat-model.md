# Threat Model

## System

A generic enterprise LLM application with a chat interface, RAG, internal knowledge access, optional tools/APIs, identity and logging.

## Assets

- confidential enterprise data;
- identities and authorization context;
- system/developer instructions;
- model/application configuration;
- API credentials;
- business records;
- security logs.

## Trust boundaries

1. User input -> application
2. Retrieved content -> model context
3. Model output -> tool router
4. Tool router -> enterprise APIs
5. Model/provider -> enterprise environment

## Threats and controls

### Direct prompt injection
Controls: input classification, instruction/data separation, least-privileged tools, authorization outside the model.

### Indirect prompt injection
Controls: treat retrieved content as untrusted, provenance, scanning, and prevent retrieved text from directly controlling tools.

### Excessive agency
Controls: allow-lists, narrow schemas, transaction limits, approval gates, deterministic authorization.

### Sensitive information disclosure
Controls: authorization before retrieval, filtering, secret management, output checking and monitoring.

### Authorization bypass through tool use
Controls: validate user context at the API boundary, re-check permissions, use scoped credentials and independent policy enforcement.

## Principle

**The model should not be the final authority for security decisions.**

The model can propose. Deterministic application components should authorize.
