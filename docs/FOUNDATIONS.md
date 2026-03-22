# Prime Directive Foundations

This document anchors Prime Directive around core responsible AI principles and a minimal GRC lifecycle. All prompts, frameworks, and profiles must support these foundations.

---

## Part 1: Core Responsible AI Principles

Prime Directive is built on six core principles. For each, we define what it means in practice and what "bad" looks like.

### 1. Fairness

**What it means:** AI systems should treat individuals and groups equitably, avoiding unjust discrimination or preference based on protected characteristics.

- **Good:** System applies consistent rules; disparate impacts are regularly audited and addressed.  
- **Bad:** System denies loans, hiring opportunities, or benefits to some demographic groups while approving others with similar profiles.

### 2. Transparency & Explainability

**What it means:** Organizations must understand how and why an AI system makes decisions, and be able to explain it to affected stakeholders.

- **Good:** For high-risk decisions, the system can point to the data and logic that drove the outcome.  
- **Bad:** System outputs a score or label with no way to justify it to a user, regulator, or impacted party.

### 3. Privacy & Security

**What it means:** AI systems must protect personal data from unauthorized access, misuse, and leakage; security controls prevent tampering.

- **Good:** PII is minimized, encrypted, and not shared outside the system; access is audited.  
- **Bad:** Training data leaks in prompts; system is vulnerable to prompt injection or model extraction attacks.

### 4. Accountability

**What it means:** Organizations have clear roles, responsibilities, and decision rights for AI systems; someone is on the hook when things go wrong.

- **Good:** There is a defined owner, approval process, and escalation path; incidents are documented and learned from.  
- **Bad:** Multiple teams blame each other for a system failure; no one took responsibility for oversight.

### 5. Reliability & Safety

**What it means:** AI systems must behave predictably and safely, with controls to mitigate unintended harms or misuse.

- **Good:** System is regularly tested, has failsafes for out-of-distribution inputs, and refuses harmful requests.  
- **Bad:** System confidently gives dangerous advice; outputs are inconsistent across similar inputs; refusal behavior can be easily bypassed.

### 6. Governance

**What it means:** Organizations have documented policies, oversight structures, and processes to ensure responsible AI use at scale.

- **Good:** There is a charter, board meetings, approval gates, and audits; changes to systems are tracked and reviewed.  
- **Bad:** Teams deploy AI in ad hoc ways; no one knows what systems exist or how they're being used.

---

## Part 2: Minimal GRC Lifecycle

This 4-step lifecycle is the backbone of Prime Directive prompts and frameworks. It mirrors the NIST AI RMF (Govern, Map, Measure, Manage) but in simpler terms.

### Step 1: Context & Inventory (Map)

**Goal:** Know what AI systems you have and why you're using them.

**Key questions:**

- What is the system's purpose and who uses it?  
- What data does it use (scope, sensitivity, sources)?  
- What decisions does it influence (recommendation, approve/deny, inform)?  
- Who are the stakeholders (users, operators, affected parties, regulators)?

**Artifacts:** Use case intake form, system inventory, stakeholder map.

### Step 2: Risk Assessment (Map / Measure)

**Goal:** Classify systems by data sensitivity, autonomy, and potential impact.

**Key questions:**

- What's the worst that could go wrong (bias, privacy breach, bad advice, security attack)?  
- How sensitive is the data (PII, medical, financial, sensitive inferences)?  
- How autonomous is the system (advisory, approve/deny, auto-execute)?  
- What's the potential impact (financial, legal, reputational, physical harm)?

**Artifacts:** Risk scoring rubric, risk register, impact assessment.

### Step 3: Controls & Approval (Govern)

**Goal:** Decide what safeguards are needed and who must sign off.

**Key questions:**

- Based on risk level, what controls are required (human review, audit logging, fairness testing, explainability)?  
- Who must approve deployment (business owner, legal, security, privacy, ethics)?  
- What documentation must be in place (charter, policy, exception handling)?  
- What's the escalation path if something goes wrong?

**Artifacts:** Governance charter, approval workflow, control matrix, exception procedures.

### Step 4: Monitoring & Incident Response (Manage)

**Goal:** Watch systems in production and respond when issues arise.

**Key questions:**

- What metrics are we tracking (performance, fairness, safety, security, compliance)?  
- How do we detect problems (dashboards, alerts, user reports, audits)?  
- What's the incident response playbook (triage, contain, investigate, fix, communicate)?  
- How do we learn and improve (post-mortems, policy updates, retraining)?

**Artifacts:** Monitoring dashboard, incident response guide, post-mortem template, continuous improvement plan.

---

## Part 3: How Principles & Lifecycle Work Together

Each step in the GRC lifecycle is grounded in the six principles.

- **Context & Inventory:** Ensures Governance and Accountability (you know what you have).  
- **Risk Assessment:** Supports Fairness, Privacy & Security, Reliability & Safety (you understand what could go wrong).  
- **Controls & Approval:** Operationalizes Transparency & Explainability, Accountability, Governance (you enforce safeguards).  
- **Monitoring & Incident Response:** Enables Reliability & Safety and Accountability (you detect and respond to issues).

All Prime Directive prompts and frameworks should map back to one or more principles and lifecycle steps.

---

## Part 4: Prompt & Framework Design Rules

When creating a new prompt or framework profile:

1. **Start with a principle.** What responsible AI value are you supporting?  
2. **Anchor to a lifecycle step.** Does it help with inventory, risk, controls, or monitoring?  
3. **Be practical.** The output should be something a team can actually use (a checklist, diagram, policy draft).  
4. **Expect iteration.** AI-generated content is a starting point; teams refine it with domain knowledge.  
5. **Document assumptions.** Who should use this? What constraints or contexts does it assume?

---

## Next Steps

- Validate and refine these principles with stakeholders.  
- Draft at least one prompt per lifecycle step to demonstrate each principle in action.  
- Map existing prompts back to principles and lifecycle steps (for example, via tags or a simple table).  
- Test prompts with real use cases before publishing.

**Last Updated:** March 21, 2026
