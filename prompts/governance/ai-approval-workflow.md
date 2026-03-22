# AI Use Case Approval Workflow

## Purpose

Provide a repeatable workflow for evaluating, classifying, and approving AI use cases before deployment.

## Context

Use when defining how teams request approval for new AI systems or significant changes to existing systems.

## Prompt

You are an AI risk and compliance specialist.

Design an "AI Use Case Approval Workflow" that:

- Starts from a simple intake form capturing:
  - Business objective and stakeholders.
  - Data categories used (including personal, sensitive, regulated data).
  - Expected users and impacted populations.
- Classifies the use case into risk tiers (e.g., low, medium, high) based on:
  - Data sensitivity, autonomy level, and regulatory exposure.
- Specifies required controls by tier, for example:
  - Low: basic documentation, periodic review.
  - Medium: model card, data documentation, human-in-the-loop for key steps.
  - High: formal ethics board review, continuous monitoring, strict access control.
- Assigns roles and responsibilities (RACI) across product, ML, security, legal, and compliance.
- Includes checkpoints across the AI lifecycle:
  - Design, development, pre-deployment review, production monitoring, and incident response.

Output this as:
1. A high-level flow description.
2. A table mapping risk tiers to required controls and approvals.

## Expected Output

A clearly described workflow and a tier-to-control mapping that can be turned into an internal SOP or policy.

## Tags

governance, workflow, risk, approval, lifecycle