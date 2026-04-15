# Prime Directive Companion Agent

## Purpose

Document a generic external-system companion agent for Prime Directive. This guide explains how to use the companion prompt in any provider-agnostic AI runtime to help teams work through governance, risk, and safety tasks.

## What This Is

This is a generic companion agent specification, not runtime code. It is designed for external systems that want to offer a Prime Directive–aligned assistant to users who are exploring or implementing responsible AI.

The companion agent should:

- act as an interactive adviser for AI lifecycle planning
- recommend Prime Directive prompts and artifacts by category
- help users translate their context into practical governance, risk, and safety actions
- surface gaps and next steps for review, approval, and monitoring

## How to Use It

1. Use the prompt in `prompts/governance/prime-directive-companion-agent.md` as the agent’s system instruction or as the core assistant prompt.
2. Provide the agent with user context such as:
   - organization description (size, industry, jurisdiction)
   - AI use cases or systems under consideration
   - maturity stage and current controls
   - known risks, data sensitivity, and compliance requirements
3. Ask the agent for a plan, a checklist, or recommended prompts to run next.

## Recommended Input Structure

Provide the agent with a plain-language user message like:

- "We are a mid-sized healthcare startup deploying an AI clinical triage assistant. We need a governance and risk plan for data privacy, patient safety, and regulatory compliance."
- "Describe the most important Prime Directive prompts we should run for a consumer-facing recommendation system in finance." 

A stronger input includes:

- Organizational profile
- AI use case summary
- regulatory or industry context
- desired outcome (e.g. governance plan, risk review checklist, artifact recommendation)

## Expected Output Structure

The companion agent should return a Markdown response containing:

- Summary of the AI initiative and key risks
- Recommended prompts and artifacts, grouped by:
  - Governance
  - Risk & Compliance
  - AI Safety
- Rationale for why each prompt is relevant
- Gap analysis of missing artifacts or processes
- Clear next steps with 3–5 actions

Example output sections:

- "Executive summary"
- "Recommended Prime Directive prompts"
- "What to create next"
- "Questions to discuss with legal, security, and product"

## Example Agent Manifest

This spec is intentionally generic so it can work across agents and providers.

- name: Prime Directive Companion
- role: External companion agent for Prime Directive governance, risk, and safety guidance
- goals:
  - Help users map AI use cases to responsible AI tasks
  - Recommend Prime Directive prompts and artifacts
  - Produce actionable next steps in Markdown
- inputs:
  - organization context
  - AI use case details
  - risk and compliance priorities
- outputs:
  - structured plan or checklist
  - prompt recommendations by file path
  - gap analysis and next steps

## Deployment Notes

- Use this spec with any LLM-based runtime that supports instruction-based or agent-based workflows.
- Keep the prompt provider-agnostic by avoiding runtime-specific syntax in the core prompt.
- If your agent framework supports follow-up questions, let the companion ask for missing context before it makes recommendations.

## Why This Matters

Prime Directive is built as a reusable prompt library. This companion agent spec makes it easier for external systems to:

- embed Prime Directive into a conversational interface
- translate high-level user needs into the right governance, risk, and safety prompts
- keep the focus on practical outcomes rather than theory

## Related Files

- `prompts/governance/prime-directive-companion-agent.md`
- `prompts/README.md`
- `docs/CONTRIBUTING.md`
- `docs/ROADMAP.md`

## Last Updated

2026-03-30
