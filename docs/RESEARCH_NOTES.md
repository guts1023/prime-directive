# Research Notes – Prime Directive

This document collects reference materials, principle sets, frameworks, and checklists that inform Prime Directive. Entries are short bullets, not essays. Goal: gather enough to inform prompt/framework design without getting lost in details.

**Rule:** Only capture what you expect to turn into a prompt, profile, or framework.

---

## Responsible AI Principles – Industry & Standards

### Microsoft (AI Governance & Risk)

- **Source:** Microsoft Responsible AI principles, Azure AI hub documentation
- **Core principles:** Fairness (equity, inclusion), Reliability & Safety, Privacy & Security, Transparency, Accountability
- **Governance emphasis:** Decision ownership, transparency in high-stakes systems, human oversight for autonomous systems
- **Key insight:** Governance is framed as "principle-centered, outcome-aware"; they emphasize impact assessment before deployment

### Google (AI Principles & Responsible Use)

- **Source:** Google AI Principles, responsible use guidance
- **Core principles:** Beneficial AI, Avoid unfair bias, Be transparent/accountable, Respect privacy, Uphold high standards of safety
- **Governance emphasis:** Interdisciplinary review (legal, ethics, policy), broad stakeholder input, context-dependent risk assessment
- **Key insight:** "Not all AI is appropriate for all contexts"; governance must be use-case and domain specific

### OpenAI (Safety & Alignment)

- **Source:** OpenAI safety documentation, usage guardrails
- **Core principles:** Alignment (models behave as intended), Safety (systems resist misuse), Transparency (clear about capabilities and limits)
- **Governance emphasis:** Refusal behavior, jailbreak testing, usage monitoring, incident response
- **Key insight:** Safety is operational; hardening includes prompt testing, adversarial prompts, rate limiting

### Anthropic (Constitutional AI, Alignment)

- **Source:** Constitutional AI papers, safety/alignment guidance
- **Core principles:** Honesty, Harmlessness, Helpfulness; long-term AI alignment
- **Governance emphasis:** Red-teaming, testing for harmful outputs, transparency in model behavior, staged deployment
- **Key insight:** Alignment is not just rules; it's about training and testing for values

### Amazon (Responsible AI Practice)

- **Source:** AWS Responsible AI library, governance frameworks
- **Core principles:** Fairness, Transparency, Explainability, Privacy, Robustness, Accountability
- **Governance emphasis:** Cross-org governance committees, fairness/bias measurement, explainability requirements by risk level
- **Key insight:** Governance is org-wide; metrics and dashboards matter for sustained compliance

### Meta (Responsible AI)

- **Source:** Meta White Papers on Responsible AI, Community Standards
- **Core principles:** Fairness, Transparency, Accountability, Safety in open systems (content moderation at scale)
- **Governance emphasis:** Scale; how to govern AI when millions of users interact with it daily
- **Key insight:** Governance must include rapid incident response and community feedback loops

---

## NIST AI Risk Management Framework (AI RMF)

### Overview

- **Published:** January 2023
- **Scope:** Four core functions for AI risk lifecycle
- **Audience:** Government, enterprises, all sectors

### Four Core Functions

#### 1. Govern

- Establish policies, governance structures, roles & responsibilities
- Integrate AI risk into organizational risk management
- Define oversight boards, approval gates, incident response

#### 2. Map

- Inventory AI systems, use cases, contexts
- Understand data, stakeholders, regulatory environment
- Document dependencies and integration points

#### 3. Measure

- Evaluate AI system performance and risks
- Conduct impact assessments, fairness audits, safety testing
- Monitor in production (metrics, dashboards, alerts)

#### 4. Manage

- Implement mitigation strategies based on risk assessment
- Respond to incidents, monitor emerging risks
- Update policies and controls as needed

### Prime Directive Alignment

- **GOVERN** ← Controls & Approval step + Governance principle
- **MAP** ← Context & Inventory + Risk Assessment steps
- **MEASURE** ← Risk Assessment continued + Monitoring step (pre-deployment testing)
- **MANAGE** ← Monitoring & Incident Response step

---

## Checklists & Control Frameworks

### AI Risk Dimensions (Common Across Most Frameworks)

**Bias & Fairness** – Does the system treat groups equitably?

- Sources: NIST, Google, Microsoft, AWS
- Key checks: Demographic parity, disparate impact, subgroup performance

**Explainability & Transparency** – Can we explain decisions?

- Sources: NIST, Microsoft, Amazon, EU AI Act references
- Key checks: Feature importance, decision trees, human-interpretable rules for high-risk decisions

**Data Privacy & Security** – Is sensitive data protected?

- Sources: GDPR guidance, NIST, Microsoft, Amazon
- Key checks: PII minimization, encryption, access control, audit logs, adversarial testing

**Safety & Robustness** – Does the system behave safely?

- Sources: OpenAI, Anthropic, safety-focused literature
- Key checks: Out-of-distribution testing, adversarial inputs, refusal behavior, failsafes

**Governance & Accountability** – Is there clear ownership and process?

- Sources: NIST, Microsoft, Amazon, all
- Key checks: Defined roles, approval workflows, documentation, incident response

### Example Framework: EU AI Act (Emerging Regulatory)

- **High-risk systems** require human oversight, explainability, bias monitoring
- **Prohibited systems** (e.g., social scoring) not allowed
- **Transparency obligations** for biometric ID, GPT, etc.
- **Key insight:** Regulatory pressure is increasing; governance frameworks must show compliance

---

## Safety & Incident Response

### Prompt Hardening (OpenAI / Anthropic Approaches)

- Test for prompt injection, jailbreaks, prompt leakage
- Implement instruction clarity, explicit refusals, rate limiting
- Monitor for adversarial inputs and log attempts
- **Artifact idea:** Prompt Hardening Checklist (already exists; verify coverage)

### Alignment & Safety Testing

- Red-team the model: What harmful outputs can we elicit?
- Test boundary cases: Out-of-distribution prompts, edge cases
- Use rubrics for "safe" vs. "unsafe" outputs
- **Artifact idea:** Alignment Verification Session (already exists; verify it covers red-teaming)

### Incident Response (NIST Cyber Security Framework adapted)

- **Detect:** Monitoring, alerts, user reports
- **Contain:** Disable system, quarantine data, notify stakeholders
- **Investigate:** Root cause, scope, impact
- **Recover:** Fix, test, redeploy
- **Learn:** Post-mortem, policy updates
- **Artifact idea:** Incident Response Playbook (needed)

---

## Regulatory Landscape (Snapshot)

### Key Regulations & Standards

- **GDPR** (EU): Data protection, right to explanation, high-risk AI safeguards
- **NIST AI RMF** (US): Risk management framework, government AI guidance
- **EU AI Act** (proposed/emerging): Risk-based classification, transparency, human oversight
- **Executive Order 14110** (US): AI governance, equity, safety, security directives
- **ISO/IEC 42001** (emerging): AI management and governance standard

### Prime Directive Positioning

- Neutral to international; principles apply globally
- Map to specific regulations as frameworks evolve
- **Artifact idea:** Regulatory Mapping Template (exists; verify it's agnostic/flexible)

---

## Next Research Priorities

- [ ] Deep-dive on NIST AI RMF full framework (23 practices across 4 functions)
- [ ] EU AI Act specific requirements for high-risk systems (will drive governance checklist)
- [ ] Industry case studies (1–2 from each major company) on governance structures
- [ ] Best practices for fairness metrics (disparate impact, demographic parity, equalized odds)
- [ ] Red-teaming and prompt injection attack taxonomy
- [ ] Incident response playbook examples (NIST CSF, SANS IR, cloud provider guidance)

---

**Last Updated:** March 21, 2026

**Note:** This is a living document. Add to it as you research, and extract findings into prompts/frameworks.
