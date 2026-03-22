# Alignment Verification Session

_Principles: fairness, transparency, privacy & security, accountability, reliability & safety_  
_Lifecycle: testing, evaluation, verification_  
_Framework: nist-ai-rmf (Measure)_

## Purpose

Guide a structured test session to verify that an AI system behaves consistently with stated responsible AI principles and policies.

## Context

Use when preparing to deploy or significantly update an AI system that impacts users or automated decisions.

## Prompt

You are a responsible AI auditor.

Design a "Alignment Verification Session" protocol that:

- Starts from an explicit list of principles (e.g., fairness, transparency, privacy & security, accountability, reliability & safety).
- For each principle, defines:
  - Test scenarios and prompts to probe behavior.
  - What "good" behavior looks like.
  - Red flags and failure patterns to watch for.
- Includes:
  - Stress tests for edge cases and ambiguous instructions.
  - A simple rubric for recording findings and severity.
  - Guidance on when issues should block deployment vs. be logged for future improvement.

Output as a step-by-step guide plus a table that auditors can fill in during a live test session.

## Expected Output

A structured playbook for running alignment tests on an AI system before or after deployment.

## Tags

alignment, safety, testing, audit
