# AI Risk Scoring Model

## Purpose

Help teams build a simple, transparent AI risk scoring model that guides controls and oversight.

## Context

Use when an organization needs to categorize AI systems into risk tiers to decide which controls and approvals apply.

## Prompt

You are an AI risk management expert familiar with frameworks like the NIST AI RMF and common enterprise risk practices.

Design a 3–4 tier AI risk scoring model that:

- Uses at least these dimensions:
  - Data sensitivity (e.g., public, internal, personal, sensitive regulated).
  - Autonomy level (advisory, decision-support, fully automated decisions).
  - Regulatory and reputational impact.
- Provides:
  - A scoring rubric for each dimension.
  - Thresholds for each risk tier (e.g., scores 1–5 = low, 6–10 = medium, 11+ = high).
- Maps each risk tier to:
  - Required documentation (model cards, data sheets).
  - Required governance (who must approve).
  - Monitoring expectations (frequency and metrics).

Format the output as:
- A short narrative explanation.
- A table with dimensions, scores, and tier thresholds.
- A table mapping tiers to required controls.

## Expected Output

A ready-to-use risk scoring model specification, suitable for adaptation into an internal AI risk policy.

## Tags

risk, compliance, NIST, scoring, controls
