# Research Ledger – Prime Directive Framework Foundations

This ledger documents the industry principle sets, legislative frameworks, and algorithmic safety standards that actively inform the programmatic runtime rules of the **Prime Directive** repository.

---

## 🏢 Big-Tech Governance Models & Mappings

### 1. Microsoft (Responsible AI Core)

- **Key Vectors:** Principle-centered, outcome-aware; strong emphasis on pre-deployment impact assessments and clear ownership limits for autonomous actions.
- **Implementation Mapping:** Operationalized inside `/governance/playbooks/` intake routines and enforced by the strict input validation guardrails of `.github/agents/prime-directive-companion.agent.md`.

### 2. Google (Contextual Adaptability)

- **Key Vectors:** Interdisciplinary reviews across ethics, legal, and engineering; explicit focus on avoiding unfair systemic skew by evaluating use-case and domain specificity.
- **Implementation Mapping:** Achieved via the centralized configuration matrices defined inside `context7.json` and the multi-tier schema parsing logic of our pipeline scripts.

### 3. OpenAI & Anthropic (Operational Hardening & Constitutional Safety)

- **Key Vectors:** Structural refusal behaviors, red-teaming boundary evaluations, jailbreak testing, and automated monitoring arrays to mitigate adversarial prompt injection strings.
- **Implementation Mapping:** Programmed into the automated verification steps of `.github/workflows/prime-directive-gate.yml` using `.github/prompts/bias-assessment.prompt.md` and related slash-command profiles.

---

## 📋 Standard Regulatory & Framework Mappings

### 1. NIST AI Risk Management Framework (AI RMF 1.0)

The absolute core blueprint for this repository. Our runtime layout converts the four flat NIST functions into executable directory and execution gates:

- **GOVERN:** Implemented within the `/governance/` directory and validated via the `verify-c7` workflow step.
- **MAP & MEASURE:** Implemented within the `/risk-compliance/` directory and evaluated via the `scripts/evaluate_project_risk.py` calculation engine.
- **MANAGE:** Implemented within the `/incident-response/` directory and triggered via real-time circuit-breaker protocols.

### 2. European Union AI Act (EU AI Act)

- **Key Vectors:** Strict, risk-tiered classification structures (Prohibited, High-Risk, Limited-Risk). High-risk systems mandate continuous logging, guaranteed human oversight windows, and deterministic bias tracing loops.
- **Implementation Mapping:** Maintained inside `docs/architecture/nist-profile.md` metadata structures and evaluated during automated pipeline execution sweeps.

### 3. Cross-Industry Compliance Baselines

- **ISO/IEC 42001 (AI Management System Standard):** Enforced via versioned repository ledger adjustments.
- **US Executive Order 14110:** Operationalized through strict structural boundary restrictions regarding sensitive PII and financial log processing streams.

---

## ⚡ Algorithmic Hardening & Response Architectures

### 1. Model Adversarial Protection

- **Attack Vector:** Prompt injection payloads, indirect system instruction extraction attempts, and target boundary bypasses.
- **Mitigation Strategy:** Enforce bounded execution frameworks by leveraging explicit instruction isolation zones and programmatic validation scripts before data hits running endpoints.

### 2. Incident Management Pipeline

- **Detect:** Intercept pipeline formatting errors or out-of-distribution tracking metrics using localized scripts.
- **Contain:** Execute software circuit-breakers to isolate malfunctioning agent processes.
- **Investigate & Recover:** Utilize clean forensic ledger formatting rules to draft comprehensive post-mortem logs.

---

## 🏁 Operationalized Ledger Tracking

| Research Vector Source      | Active Implementation Asset      | Pipeline Verification Hook |
| :-------------------------- | :------------------------------- | :------------------------- |
| **Microsoft / NIST Govern** | `context7.json` Data Schema      | `verify-c7` Gate           |
| **OpenAI / NIST Measure**   | `.github/prompts/` Command Layer | `verify-copilot` Gate      |
| **EU AI Act / NIST Manage** | `scripts/` Evaluation Engines    | `grc-audit` Gate           |

---

**Last Updated:** May 18, 2026  
**Ledger Alignment:** Version 1.3.0 Architecture Matrix.
