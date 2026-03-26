# NIST AI RMF Profile Builder

## Purpose

Help an organization generate a customized NIST AI RMF–aligned governance pack using Prime Directive prompts and their own context.

## Context

Use when an organization wants a first version of its AI governance documentation (charter, risk model, workflows) that is roughly aligned with NIST AI RMF and can be refined by humans.

## Prompt

You are an AI governance architect familiar with the NIST AI Risk Management Framework (AI RMF) and enterprise policy writing.

You are working with the "Prime Directive" prompt library, which provides building blocks for:

- Governance (e.g., AI Ethics Board Charter, AI Use Case Approval Workflow).
- Risk & Compliance (e.g., AI Risk Scoring Model, Regulatory Mapping Template).
- AI Safety (e.g., Alignment Verification Session, Prompt Hardening & Safety Checklist).

Given:
- A description of the organization (size, industry, jurisdictions, risk appetite).
- A list of planned or existing AI use cases.

Produce a tailored “NIST AI RMF Implementation Pack” that includes:

1. A short summary of how the organization will address each NIST Core Function: Govern, Map, Measure, Manage.
2. A checklist of Prime Directive prompts they should run (by filename/path) to generate:
   - Governance artifacts.
   - Risk and compliance artifacts.
   - Safety and alignment artifacts.
3. A suggested directory structure for their own repo (e.g., `docs/ai/`) and where each artifact should live.
4. A list of follow-up questions they should discuss internally with legal, security, and product.

Write the output in Markdown with clear headings and checklists.

## Expected Output

A practical, copy-pasteable implementation pack outline plus a to-do list that a team can follow to stand up a NIST-aligned AI governance baseline in days, not months.

## Tags

nist-ai-rmf, governance, risk, safety, framework
