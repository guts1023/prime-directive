# NIST AI RMF Implementation Profile (Prime Directive Starter)

## Purpose

Provide a lightweight, NIST AI RMF–aligned implementation profile that organizations can adopt as a starting point for AI governance, risk management, and safety.

## Context

Use this as a baseline for small to mid-sized teams that want to say: “We are aligned with the spirit of NIST AI RMF” without implementing every subcategory.

## Scope

This profile maps NIST AI RMF Core Functions (Govern, Map, Measure, Manage) to:

- Prime Directive prompt bundles
- Minimal process expectations
- Documentation artifacts

## Core Functions and Actions

### 1. Govern

**Goal:** AI risk management is integrated into organizational governance.

- Required artifacts:
  - AI Ethics Board Charter (from `prompts/governance/ai-ethics-board-charter.md`)
  - AI Use Case Approval Workflow (from `prompts/governance/ai-approval-workflow.md`)
- Minimal expectations:
  - Named accountable owner for AI risk.
  - Defined approval path for high-risk AI systems.

### 2. Map

**Goal:** AI use cases, contexts, and risks are understood and documented before deployment.

- Required artifacts:
  - AI Use Case Intake Form (to be created).
  - Regulatory Mapping Template (from `prompts/risk-compliance/regulatory-mapping-template.md`).
- Minimal expectations:
  - Every production AI system has an intake record.
  - Regulatory touchpoints are identified and reviewed.

### 3. Measure

**Goal:** AI risks and performance are measured using appropriate metrics and evaluations.

- Required artifacts:
  - AI Risk Scoring Model (from `prompts/risk-compliance/ai-risk-scoring-model.md`).
  - Alignment Verification Session Plan (from `prompts/ai-safety/alignment-verification-session.md`).
- Minimal expectations:
  - Risk tier assigned for each AI system.
  - At least one alignment verification session before major launch.

### 4. Manage

**Goal:** AI risks are prioritized and treated over time across the lifecycle.

- Required artifacts:
  - AI Use Case Approval Workflow (reuse from Govern).
  - Incident Response Playbook (to be created).
- Minimal expectations:
  - High-risk systems have ongoing monitoring.
  - Documented process for responding to AI incidents.

## How to Use This Profile

1. Copy this file into your own repo under `docs/ai/` or similar.  
2. Instantiate each “Required artifact” using the linked Prime Directive prompts.  
3. Record where each artifact lives (URL/path) in your own environment.  
4. Review with legal, security, and data teams, then adapt as needed.

## Tags

nist-ai-rmf, governance, risk, safety, compliance
