# Prime Directive

An actionable, agentic Governance, Risk, and Compliance (GRC) framework and safety runtime designed to align AI systems with the NIST AI Risk Management Framework (RMF).

## 🚀 The Agentic Philosophy

Unlike traditional, passive GRC documentation, **Prime Directive** is built as an operational runtime. Every policy, checklist, and workflow is structured as a modular playbook designed to be programmatically parsed, evaluated, and executed by AI agents or safety engineers within continuous integration pipelines.

## 📂 Repository Architecture

The workspace is strictly aligned to the core lifecycles of the NIST AI RMF:

- `governance/` - **[Govern]** Cultivating a culture of AI risk management, board charters, and use-case intake workflows.
- `risk-compliance/` - **[Map / Measure / Manage]** Practical risk scoring models, regulatory mapping templates, and safety checklists.
  - `risk-compliance/playbooks/` - High-velocity verification assets and runtime SOPs.
- `incident-response/` - **[Incident Plan]** Live operational continuity plans and phase-specific incident runbooks.
- `scripts/` - Programmatic Python validation, risk evaluation, and compliance parsing engines.

## 🛠️ Integrated Tooling: Markitdown

This repository integrates with Microsoft's `markitdown` engine to instantly ingest and serialize unstructured regulatory artifacts (PDFs, spreadsheets, DOCX) into clean Markdown for automated ingestion and compliance verification.

## ⚡ Automated Verification

Run the integrated testing suite to check system compliance and calculate use-case risk:

```bash
python scripts/verify_grc_compliance.py
python scripts/evaluate_project_risk.py
```
