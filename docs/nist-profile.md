---
framework: "NIST AI RMF Core Alignment Profile"
registry_key: "nist_ai_rmf_govern"
version: "1.1.0"
category: "Risk & Compliance Architecture"
last_updated: 2026-05-18
---

# NIST AI RMF 'Govern' Phase Profile

This profile establishes the programmatic translation layer between the National Institute of Standards and Technology (NIST) AI Risk Management Framework core functions and the executable assets of the **Prime Directive** repository.

---

## 🏛️ GOVERN 1: Policies, Processes, and Procedures

### NIST Core Alignment

- **Subcategory Mapping:** GOVERN 1.1, GOVERN 1.2 (Organizational policies, processes, and procedures for classifying, diagnosing, and managing AI risks are established and deployed).
- **Control Intent:** Mandate and standardize organizational workflows for system inventory tracking, risk classifications, and operational boundaries.

### Runtime Asset Configuration

- **Data Fabric Key:** `context7.json -> parameter: upstream_frameworks.nist`
- **Operational Execution Module:** `/governance/playbooks/intake-boundaries.md`
- **Automated Verification Script:** `scripts/verify_grc_compliance.py`

---

## ⚖️ GOVERN 2: Workforce Diversity and Culture

### NIST Core Alignment - Govern

- **Subcategory Mapping:** GOVERN 2.1, GOVERN 2.2 (Workplace teams represent diverse perspectives, and a culture of shared responsibility for AI safety is cultivated).
- **Control Intent:** Orchestrate cross-functional evaluation routines to identify algorithmic bias, adversarial edge cases, and systemic model failure points before product deployment.

### Runtime Asset Configuration - Govern

- **Workspace Agent Instruction:** `.github/agents/prime-directive-companion.agent.md`
- **Active Platform Slash Command:** `.github/prompts/bias-assessment.prompt.md`
- **Operational Execution Module:** `/risk-compliance/playbooks/bias-mitigation.md`

---

## 🏁 Automated Profile Compliance Status

| NIST Function Block       | Local Code Path    | Pipeline Hook    | Status                        |
| :------------------------ | :----------------- | :--------------- | :---------------------------- |
| **GOVERN 1.1** (Policies) | `/governance/`     | `verify-c7`      | :white_check_mark: Verified   |
| **GOVERN 2.1** (Culture)  | `.github/prompts/` | `verify-copilot` | :white_check_mark: Locked     |
| **MEASURE 1.1** (Metrics) | `scripts/`         | `grc-audit`      | :white_check_mark: Executable |
