# Prime Directive - Regulatory Crosswalk & Compliance Map

**Version:** 1.0.0 (Core Release 2026)
**Target Lifecycle Phase:** Legal Architecture Audit & Compliance Alignment (NIST AI RMF - Govern)

## 1. Scope

This crosswalk functions as a structural translation layer between technical engineering files (Model Cards, prompt layers, validation logs) and global regulatory compliance targets (NIST AI RMF, GDPR, CCPA).

## 2. Structural Crosswalk Reference Map

### 2.1 NIST AI RMF 1.0 Realization

- **Govern Layer:** Satisfied by the active execution of the `/ethics-board` escalation protocol and centralized tracking logs.
- **Map Layer:** Satisfied by the continuous programmatic execution of `scripts/evaluate_project_risk.py` against active branches.
- **Measure Layer:** Verified via the execution of the `/assess-bias` and `/verify-alignment` workspace command outputs.

### 2.2 Data Sovereignty & Consumer Privacy (GDPR / CCPA)

- **Right to Deletion / Purging:** If vector index poisoning or PII exposure occurs, systems must execute target data purging according to the mandates defined in the core containment standards.
- **Algorithmic Transparency:** Every deployment tiering level must maintain human-scannable configuration manifests inside the repository root to guarantee auditable lineage traces.
