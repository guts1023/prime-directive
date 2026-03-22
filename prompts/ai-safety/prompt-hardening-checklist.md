# Prompt Hardening & Safety Checklist

## Purpose

Help teams design prompts that reduce risk of prompt injection, data leakage, harmful outputs, and policy violations.

## Context

Use when creating or reviewing prompts for production systems, especially those exposed to end users or handling sensitive data.

## Prompt

You are an AI safety engineer focused on prompt hardening and misuse prevention.

Create a "Prompt Hardening & Safety Checklist" that:

- Identifies common risks, including:
  - Prompt injection and jailbreaks.
  - Leakage of sensitive or proprietary information.
  - Harmful, biased, or illegal content generation.
- Lists concrete mitigations, such as:
  - Clear system instructions and refusal behavior.
  - Input validation and sanitization.
  - Output filtering and content moderation layers.
  - Avoiding inclusion of real PII or confidential details in prompts.
- Adds checks specific to:
  - Enterprise prompt libraries (classification of prompts by sensitivity, review and approval, version control and logging).
- Structures the checklist into phases:
  - Design-time checks, pre-deployment review, runtime and monitoring checks.

Format the output as a checklist with short, actionable items that a product or engineering team can run through.

## Expected Output

A practical, implementation-focused checklist for designing safer prompts and reviewing existing ones.

## Tags

safety, security, prompt-injection, privacy