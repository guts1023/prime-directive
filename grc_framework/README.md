# Prime Directive GRC Framework Hub

Prime Directive aligns with common responsible AI principles (fairness, transparency & explainability, privacy & security, accountability, reliability & safety) and AI risk management frameworks (e.g., NIST AI RMF). It provides reusable prompts and templates to operationalize these ideas in day‑to‑day AI use.

This hub serves as a central repository for organizations to download and implement Prime Directive policies and frameworks, alongside references to established AI GRC standards.

This hub contains opinionated, ready-to-use GRC "profiles" (checklists, policies, and prompt bundles) that organizations can adopt or fork.

## Structure

### Prime Directive Templates

Custom prompts and templates developed by Prime Directive for operationalizing responsible AI practices.

#### Governance

Prompts for establishing organizational structures, oversight boards, and decision-making processes.

**Examples:**

- AI Ethics Board Charter
- Approval Workflow Definitions
- Escalation Procedures

#### Risk & Compliance

Prompts focused on risk assessment, regulatory compliance, and documentation.

**Examples:**

- Regulatory Mapping Templates
- Risk Assessment Checklists
- Compliance Audit Prompts

#### AI Safety

Prompts centered on alignment, transparency, and safe AI behavior.

**Examples:**

- Alignment Verification Prompts
- Transparency & Explainability Checklists
- Responsible Use Guidelines

### Established Frameworks

References and mappings to established AI governance, risk, and compliance frameworks from industry leaders and standards bodies.

Each framework subfolder contains:

- `*_profile.md`: Human-readable framework/policy document
- `*_prompt-bundle.md`: Prompts that generate or maintain that profile

**Example:** [NIST AI RMF Starter Profile](./established-frameworks/nist-ai-rmf/nist-profile.md)

- **nist-ai-rmf/**: NIST AI Risk Management Framework (Govern, Map, Measure, Manage)
- **microsoft/**: Microsoft Responsible AI framework
- **google/**: Google AI Principles and frameworks
- **openai/**: OpenAI's governance and safety approaches
- **facebook/**: Meta's AI governance frameworks
- **anthropic/**: Anthropic's AI safety and alignment frameworks
- **amazon/**: Amazon's AI ethics and governance policies

---

## Contributing

1. Create a `.md` file in the appropriate subdirectory
2. Follow the prompt template (see below)
3. Test the prompt with an AI agent
4. Submit via pull request

## Prompt Template

```markdown
# [Prompt Title]

## Purpose

Brief description of what this prompt is designed to achieve.

## Context

Who should use this? When? In what situations?

## Prompt

[The actual prompt text here]

## Expected Output

What should the AI agent produce?

## Tags

governance, risk, compliance, safety, etc.

## Last Updated

[Date]
```

---

**Total Prompts:** [count will grow]
