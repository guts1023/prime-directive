# Prime Directive Action Plan – Phase 1 (Pre-GitHub)

This plan outlines the foundational work to complete before opening a GitHub repository. It aligns with the 3-phase roadmap and reflects feedback from Perplexity AI.

---

## Current Status

### ✅ Completed

- [x] README.md – comprehensive project overview with "Why Prime Directive?", directory structure, frameworks vs. prompts
- [x] docs/ROADMAP.md – 3-phase plan (Phase 1: 0–3 months, Phase 2: 3–9 months, Phase 3: 9–18 months)
- [x] docs/GOVERNANCE.md – established (needs review/update after foundations)
- [x] docs/CONTRIBUTING.md – established (needs review/update after foundations)
- [x] Initial prompt library:
  - 2 governance prompts (AI Ethics Board Charter, AI Approval Workflow)
  - 2 risk/compliance prompts (AI Risk Scoring Model, Regulatory Mapping Template)
  - 2 safety prompts (Alignment Verification Session, Prompt Hardening Checklist)
- [x] Initial framework profile:
  - grc_framework/nist-ai-rmf/nist-profile.md (NIST AI RMF starter profile)
  - grc_framework/nist-ai-rmf/nist-prompt-bundle.md (prompt bundle to generate NIST pack)
- [x] docs/FOUNDATIONS.md – principles and minimal GRC lifecycle
- [x] docs/RESEARCH_NOTES.md – targeted research list (principles, NIST, checklists, regs)

### 🔄 In Progress / Needs Review

- [ ] Validate existing prompts against FOUNDATIONS.md (do they support core principles + lifecycle steps?)
- [ ] Expand prompt library to 3–5 prompts per category (governance, risk/compliance, safety)
- [ ] Verify NIST profile bundle is complete and actionable
- [ ] Update docs/CONTRIBUTING.md to reference FOUNDATIONS.md and lifecycle
- [ ] Update docs/GOVERNANCE.md to clarify principles-first approach

### ⏭️ To Do (Before GitHub)

- [ ] Draft 1 additional prompt per pillar (to reach 3 per category minimum)
  - Governance: Escalation & Exception Procedures (or AI Incident Response Protocol)
  - Risk/Compliance: AI System Inventory Template or Compliance Audit Checklist
  - Safety: Transparency & Explainability Checklist or Safety Checklist for Public-Facing Systems
- [ ] Complete RESEARCH_NOTES.md with 1–2 paragraphs per regulatory framework
- [ ] Link docs/FOUNDATIONS.md and docs/RESEARCH_NOTES.md from README, ROADMAP, and CONTRIBUTING
- [ ] Create a simple self-check: "Is this prompt principle-aligned?"
- [ ] Draft brief intro paragraphs for grc_framework/README.md (clarity on profiles)

---

## Detailed Task Breakdown – Phase 1 Foundations

### Task 1: Validate & Update Existing Prompts (High Priority)

**Why:** Ensure all current prompts support FOUNDATIONS.md principles and lifecycle.

**Steps:**

1. Review each existing prompt (6 total: 2 gov, 2 risk, 2 safety)
2. For each, check:
   - Does it map clearly to one or more principles? (Add a "Principles" section if missing)
   - Does it fit in the GRC lifecycle? (Add a "Lifecycle Step" section if missing)
   - Is the "Expected Output" testable and practical?
3. Add missing sections or update prompts to clarify alignment.

**Estimated effort:** 2–3 hours

**Success criteria:** All 6 prompts have principle + lifecycle + testable output clearly documented.

---

### Task 2: Draft 3 Additional Prompts (High Priority)

**Why:** Reach 3–5 prompts per category to demonstrate breadth and completeness.

**Suggestions:**

#### Governance (pick 1):

- **Option A:** AI Incident Response Protocol
  - Purpose: Define how to detect, contain, investigate, and recover from AI mishaps.
  - Lifecycle: Monitoring & Incident Response
  - Principles: Reliability & Safety, Accountability
- **Option B:** Escalation & Exception Procedures
  - Purpose: Define when and how to escalate AI governance decisions and handle exceptions.
  - Lifecycle: Controls & Approval
  - Principles: Accountability, Governance

#### Risk & Compliance (pick 1):

- **Option A:** AI System Inventory Template
  - Purpose: Audit your AI systems; document what you have and why.
  - Lifecycle: Context & Inventory
  - Principles: Governance, Accountability
- **Option B:** Compliance Audit Checklist
  - Purpose: Audit a system against regulations (GDPR, NIST AI RMF, company policy).
  - Lifecycle: Measuring (audit-phase)
  - Principles: Compliance, Accountability

#### Safety (pick 1):

- **Option A:** Transparency & Explainability Checklist
  - Purpose: Audit how well a system explains its decisions to end users and stakeholders.
  - Lifecycle: Controls & Approval + Monitoring
  - Principles: Transparency & Explainability, Accountability
- **Option B:** Safety Checklist for Public-Facing Systems
  - Purpose: Before launching a public chatbot, LLM, or recommendation system, verify safety guardrails.
  - Lifecycle: Controls & Approval
  - Principles: Reliability & Safety, Accountability

**Estimated effort:** 1–2 hours per prompt (rough draft)

**Success criteria:** 3 new prompts drafted, follow standard template, map to principles + lifecycle.

---

### Task 3: Complete RESEARCH_NOTES.md (Medium Priority)

**Why:** Have a reference library to inform future framework profiles.

**Steps:**

1. Flesh out each framework section with 3–5 specific bullets (don't write essays).
2. Add 1–2 key links per framework (official docs, key papers).
3. Add emerging regulations section (GDPR, NIST, EU AI Act, EO 14110).
4. Identify 2–3 "next research priorities" in order.

**Estimated effort:** 2–3 hours

**Success criteria:** RESEARCH_NOTES.md is 2–3 pages, organized by topic, ready to reference when designing frameworks.

---

### Task 4: Link Foundations Throughout Project (Low Effort, High Value)

**Why:** Make it clear that FOUNDATIONS.md is the north star.

**Steps:**

1. Add header to README: "See [docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md) for core principles and GRC lifecycle."
2. Update docs/CONTRIBUTING.md to reference FOUNDATIONS.md: "All prompts must align with core principles (fairness, transparency, privacy, accountability, safety, governance)."
3. Add a "Principles Check" section to CONTRIBUTING.md as a quick checklist for contributors.
4. Link docs/RESEARCH_NOTES.md from README under "Learning Resources" section.

**Estimated effort:** 1 hour

**Success criteria:** FOUNDATIONS.md and RESEARCH_NOTES.md are discoverable and referenced throughout the project.

---

### Task 5: Quick Framework Hub Update (Medium Priority)

**Why:** Make it clear what GRC profiles are and how they're structured.

**Steps:**

1. Update grc_framework/README.md to include a "What Is a Profile?" section explaining:
   - Profile = a bundle of policies, checklists, and prompts aligned to a specific framework (e.g., NIST, startup, enterprise).
   - Each profile contains: `*_profile.md` (human-readable) and `*_prompt-bundle.md` (AI runnable).
2. Use NIST profile as the worked example.
3. Include a "How to Create a Profile" section for future contributors.

**Estimated effort:** 1–2 hours

**Success criteria:** grc_framework/README.md clearly explains what profiles are and how NIST profile demonstrates the pattern.

---

## Estimated Timeline – Phase 1 Foundations (Before GitHub)

| Task                               | Effort    | Days    | Priority |
| ---------------------------------- | --------- | ------- | -------- |
| Task 1: Validate existing prompts  | 2–3h      | 1       | High     |
| Task 2: Draft 3 new prompts        | 3–6h      | 2–3     | High     |
| Task 3: Complete RESEARCH_NOTES.md | 2–3h      | 1       | Medium   |
| Task 4: Link foundations           | 1h        | <1      | High     |
| Task 5: Update framework hub       | 1–2h      | 1       | Medium   |
| **Total (estimated)**              | **9–15h** | **5–7** | —        |

**Realistic workload:** ~2 hours/day → 5–7 working days to complete Phase 1 foundations.

---

## Success Criteria – Phase 1 Foundations Complete

- [x] docs/FOUNDATIONS.md exists with principles, GRC lifecycle, design rules
- [x] docs/RESEARCH_NOTES.md exists with targeted research bullets (no essays)
- [ ] At least 3–5 prompts per category (governance, risk/compliance, safety) — **currently 2 each, need 1 more each**
- [ ] All prompts clearly map to principles + lifecycle step
- [ ] NIST AI RMF profile is complete and actionable
- [ ] CONTRIBUTING.md references FOUNDATIONS.md and includes principles check
- [ ] README links to FOUNDATIONS.md and RESEARCH_NOTES.md
- [ ] grc_framework/README.md explains what profiles are and how to build them

Once all above are done: **Ready to open GitHub repo and start Phase 2.**

---

## GitHub Readiness Checklist (Before Public Launch)

- [ ] README is clear and navigable
- [ ] docs/FOUNDATIONS.md anchors the whole project
- [ ] docs/CONTRIBUTING.md is actionable for first contributors
- [ ] At least 3–5 prompts per category + NIST profile demonstrate value
- [ ] RESEARCH_NOTES.md signals that project is informed by industry best practices
- [ ] .gitignore and LICENSE are in place
- [ ] No sensitive data or incomplete TODOs in committed files

---

**Last Updated:** March 21, 2026

**Next Review:** After Tasks 1–2 completed (roughly 3–4 working days)
