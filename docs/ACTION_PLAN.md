# Prime Directive Action Plan – Post-Launch Runtime Operations

This action plan tracks the evolution of the **Prime Directive** repository from its initial conceptual design into a live, agentic GRC runtime environment.

---

## 📊 Current Status (Post-Pivot Evolution)

### ✅ Phase 1: Foundational Architecture (Completed)

- [x] **Repository Public Launch:** Transferred core framework elements to the public workspace under `guts1023/prime-directive`.
- [x] **The Agentic Pivot:** Stripped out passive text files and restructured the codebase root into the three core execution pillars of the NIST AI RMF lifecycle:
  - `governance/` (Govern)
  - `risk-compliance/` (Map, Measure, Manage)
  - `incident-response/` (Govern, Measure, Manage)
- [x] **Poka-Yoke Automation Gate:** Locked down `.github/workflows/prime-directive-gate.yml` to programmatically validate compliance configurations (`context7.json`) and run automated risk evaluation scripts on every commit to `main` and `dev`.
- [x] **Core Agent Specification:** Finalized and tuned `.github/agents/prime-directive-companion.agent.md` to guide workspace LLM engines through programmatic file modifications and verification runbooks.

### 🔄 Phase 2: Active Runtime Expansion (In Progress)

- [ ] **Playbook Serialization:** Fully populate `/playbooks/` subdirectories inside each lifecycle pillar with machine-parseable Markdown validation lists.
- [ ] **Markitdown Data Fabric Integration:** Refine ingestion scripts utilizing Microsoft's `markitdown` engine to programmatically serialize incoming enterprise policies directly into our active layout.
- [ ] **Algorithmic Validation:** Expand Python engines inside `scripts/` (`verify_grc_compliance.py` and `evaluate_project_risk.py`) to output deterministic compliance metrics.

---

## 🛠️ Active Engineering Sprints

### Task 1: Consolidate Historical Design Documents

**Why:** Keep the root of the `docs/` folder clean and highly scannable for external contributors and autonomous coding agents.

- **Action:** Move legacy design profiles (`nist-profile.md`, `FOUNDATIONS.md`, `external-runtime-blueprint.md`, and `RESEARCH_NOTES.md`) out of the docs root and into a dedicated `docs/architecture/` subdirectory.
- **Status:** Staged for directory migration.

### Task 2: Synchronize Community Profiles

**Why:** Ensure standard open-source assets align with our active runtime architecture.

- **Action:** Update `docs/CONTRIBUTING.md` to establish the rule that all new compliance assets must be contributed as executable, machine-parseable playbooks rather than flat text essays.

---

## 🏁 Phase 2 Milestone Targets

| Milestone Target                | Objective                                                                                | Target Completion |
| :------------------------------ | :--------------------------------------------------------------------------------------- | :---------------- |
| **Pillar Playbook Lock**        | Complete 3 core executable playbooks per lifecycle folder.                               | Immediate Sprint  |
| **Deterministic Risk Gate**     | Achieve 100% test passing metrics on local CI/CD automated gates.                        | Continuous        |
| **Enterprise Schema Ingestion** | Successfully ingest a sample corporate PDF using `context7.json` pipeline configuration. | Upcoming Sprint   |

---

**Last Updated:** May 18, 2026  
**Current Branch:** `dev`  
**Tracking Ledger:** Aligned with Version 1.3.0 Workspace Architecture.
