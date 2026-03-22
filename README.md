# Prime Directive

A comprehensive markdown library of AI governance, risk, and compliance prompts designed to help organizations and individuals establish baseline directives for responsible AI deployment.

## Why Prime Directive?

Modern AI is powerful, but without guardrails it can create legal, ethical, and security risk. Prime Directive provides reusable prompt and framework templates so teams can:

- **Establish AI governance** (boards, approvals, RACI, decision rights).
- **Manage risk** (classify use cases, score risk, plan mitigations).
- **Ensure compliance** (map to regulations and standards).
- **Promote safety** (alignment checks, prompt hardening, incident response).

Prime Directive is framework‑aware: it aligns with common responsible AI principles (fairness, transparency & explainability, privacy & security, accountability, reliability & safety) and AI risk management guidance such as the NIST AI Risk Management Framework (Govern, Map, Measure, Manage).

## Foundations & Guidance

New to Prime Directive? Start here:

- **[docs/FOUNDATIONS.md](./docs/FOUNDATIONS.md)** – Core principles (fairness, transparency, privacy, accountability, safety, governance) and a minimal GRC lifecycle that anchors all prompts and frameworks.
- **[docs/RESEARCH_NOTES.md](./docs/RESEARCH_NOTES.md)** – Reference materials: industry AI principles (Microsoft, Google, OpenAI, etc.), NIST AI RMF, regulatory landscape, and safety practices.
- **[docs/ACTION_PLAN.md](./docs/ACTION_PLAN.md)** – Tactical Phase 1 work plan (before GitHub): what's completed, what's in progress, and what's next.

## Directory Structure

```text
Prime-Directive/
├── docs/                 # Project governance, contribution, and meta-docs
│   ├── CONTRIBUTING.md
│   └── GOVERNANCE.md
├── grc_framework/        # Opinionated GRC "profiles" and framework bundles
│   ├── ai-safety/
│   ├── established-frameworks/
│   │   ├── amazon/
│   │   ├── anthropic/
│   │   ├── facebook/
│   │   ├── google/
│   │   ├── microsoft/
│   │   ├── nist-ai-rmf/
│   │   └── openai/
│   ├── governance/
│   └── risk-compliance/
├── prompts/              # Atomic, reusable prompt files
│   ├── ai-safety/
│   ├── governance/
│   └── risk-compliance/
├── LICENSE
└── README.md
```

## What's What?

- **`prompts/`** – individual prompts ready to plug into agents, workflows, or SOPs.
- **`grc_framework/`** – opinionated "profiles" that bundle prompts into ready‑to‑use governance, risk, and safety packs (for example, NIST‑aligned or cloud‑provider‑inspired profiles).
- **`docs/`** – how the Prime Directive project itself is organized and maintained.

## Prompt Library

All prompts live under `prompts/` and follow a common template (Purpose, Context, Prompt, Expected Output, Tags, Last Updated). This keeps prompts composable and easy to review.

### Governance

Prompts for establishing organizational structures, oversight boards, and decision-making processes, such as:

- AI Ethics Board Charter
- AI Use Case Approval Workflow
- Escalation and exception procedures

These help teams embed AI governance into existing decision forums rather than creating "AI in a silo."

### Risk & Compliance

Prompts focused on risk assessment, regulatory alignment, and documentation, such as:

- AI risk scoring models
- Regulatory mapping templates
- Compliance audit checklists

Use these to map AI use cases to relevant laws, standards, and internal policies and to decide which controls apply.

### AI Safety

Prompts centered on alignment, transparency, and safe AI behavior, such as:

- Alignment verification sessions
- Transparency & explainability checklists
- Prompt hardening and safety checklists

These help teams probe models for misalignment, reduce prompt‑injection and leakage risk, and codify refusal behavior.

## GRC Frameworks

The `grc_framework/` directory contains higher‑level, ready‑to‑adopt GRC "profiles" and mappings.

### Prime Directive Templates

Opinionated profiles (for example, a NIST AI RMF starter, small‑startup profile, or domain‑specific packs) that assemble multiple prompts into a governance program.

### Established Frameworks

References and mappings to industry and standards‑body approaches, including:

- **nist-ai-rmf/** – NIST AI Risk Management Framework
- **microsoft/** – Microsoft Responsible AI principles
- **google/** – Google AI principles
- **openai/, anthropic/, amazon/, facebook/** – public responsible-AI and AI safety materials from major providers

## Frameworks vs. Prompts

- Use `prompts/` when you want individual building blocks.
- Use `grc_framework/` when you want a pre‑assembled governance/risk/safety pack that you can fork and adapt.

## Getting Started

### Browse Prompts

1. Explore `prompts/governance`, `prompts/risk-compliance`, and `prompts/ai-safety`.
2. Pick 1–2 prompts per area that match a real AI use case in your organization.

### Run on a Real Use Case

Feed the selected prompts to your preferred AI assistant along with your context (org size, industry, jurisdictions, example systems).

Save the outputs into your own repo (for example, under `docs/ai/`) as draft policies, workflows, and checklists.

### Adopt a Framework Profile (Optional)

1. Open `grc_framework/` and pick a profile (for example, a NIST‑aligned starter).
2. Use its instructions to stitch individual prompt outputs into an overall AI governance baseline.

### Review with Humans

Have legal, security, data, and product teams review, edit, and formally adopt the artifacts.

**⚠️ Treat AI‑generated content as a starting point, not final legal or compliance advice.**

## Contributing

Prime Directive is community‑driven. We welcome contributions from practitioners, researchers, and policy experts.

- Read [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md) for contribution guidelines (prompt template, review process, commit conventions).
- Add new prompts under the appropriate `prompts/` subdirectory using the standard template.
- Propose new GRC profiles or framework mappings in `grc_framework/` (for example, a sector‑specific profile or a mapping to an emerging standard).

Please prioritize:

- Clarity and testability of prompts.
- Alignment with established governance and risk guidance.
- Inclusive, accessible language.

## Roadmap

See [docs/ROADMAP.md](./docs/ROADMAP.md) for a 3-phase plan to build Prime Directive from a core library into a community-driven GRC resource. Learn what's planned for Phase 1 (solidify core), Phase 2 (frameworks & adoption), and Phase 3 (community & integrations).

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for full details.

## Contact

- Open an issue for questions, bugs, or framework/profile requests.
- Pull requests are welcome for new prompts, profiles, and documentation improvements.
