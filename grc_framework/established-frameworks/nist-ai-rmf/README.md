# NIST AI Risk Management Framework (AI RMF) – Prime Directive Hub

This folder anchors Prime Directive to the official NIST AI Risk Management Framework (AI RMF 1.0). It provides a short overview, links to the source, and Prime Directive–specific profiles and mappings built on top of NIST.

---

## Official NIST AI RMF

- Title: NIST AI 100-1: Artificial Intelligence Risk Management Framework (AI RMF 1.0)
- Publisher: National Institute of Standards and Technology (NIST)
- Publication date: January 2023

Official resources:

- [Framework page](https://www.nist.gov/itl/ai-risk-management-framework)
- [PDF (AI 100-1)](https://doi.org/10.6028/NIST.AI.100-1)

In this repository:

- `nist.ai.100-1.md` – a Markdown conversion of the official AI RMF 1.0 PDF for local reference.  
  This is provided for convenience; the official source remains NIST.

---

## NIST AI RMF in brief

The NIST AI RMF is a voluntary framework to help organizations identify, assess, and manage risks from AI systems. It is:

- Rights-preserving and sector-agnostic
- Designed for organizations of all sizes
- Intended to be used across the entire AI lifecycle

The framework is organized into two main parts:

- **Part 1 – Foundational information**
  - How to frame AI risks, impacts, and harms
  - Who the framework is for (AI “actors” across the lifecycle)
  - Characteristics of trustworthy AI systems (e.g., valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed)

- **Part 2 – Core and profiles**
  - Four core Functions: **Govern, Map, Measure, Manage**
  - Categories and subcategories under each Function
  - “Profiles” that tailor the framework to specific use cases or organizations

### Core Functions

- **Govern** – Organizational foundation: policies, roles, responsibilities, culture, and accountability for AI risk.
- **Map** – Understand AI systems and context: inventory, data, stakeholders, potential impacts and harms.
- **Measure** – Assess AI performance and risks: metrics, testing, monitoring, and evaluation.
- **Manage** – Prioritize and respond to risks over time: mitigation, incident response, continuous improvement.

---

## How Prime Directive uses NIST AI RMF

Prime Directive does not reimplement the NIST AI RMF. Instead, it provides:

- **Profiles** – Opinionated, markdown-based “implementation profiles” that show how a team might operationalize Govern / Map / Measure / Manage using Prime Directive prompts and artifacts.
- **Prompt bundles** – Prompts that help generate or maintain NIST-aligned charters, workflows, risk rubrics, checklists, and incident playbooks.
- **Mappings** – Clear references back to NIST Functions and (where appropriate) Categories/Subcategories so teams can show how their internal artifacts support the framework.

Prime Directive’s minimal lifecycle aligns with the NIST Functions as follows:

- Context & Inventory → Map
- Risk Assessment → Map / Measure
- Controls & Approval → Govern
- Monitoring & Incident Response → Manage

---

## Folder contents

- `nist.ai.100-1.md` – Local Markdown conversion of the official NIST AI RMF 1.0 (for reference only).
- `nist-profile.md` – Prime Directive’s NIST-aligned starter implementation profile (how to adopt a lightweight AI RMF baseline).
- `nist-profile-prompt-bundle.md` – Prompt(s) that help generate a customized NIST AI RMF implementation pack for a given organization.

You can:

- Use `nist-profile.md` as a starting point for your own internal AI governance documentation.
- Run the prompt bundle to generate a tailored implementation pack for your organization.
- Extend this folder with additional profiles (e.g., sector-specific or jurisdiction-specific variants) that still map back to the NIST AI RMF.

---

## Notes

- Always treat the NIST AI RMF itself as the source of truth.
- Use this folder to keep your NIST-related content organized and clearly separated from Prime Directive’s own opinionated frameworks.
