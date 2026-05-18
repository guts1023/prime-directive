# 🧪 Prime Directive: Test Cases & Validation Suite

## Fallback Regroup Initiative • Automated DevOps Policy Verification [cite: 1]

This directory contains the standardized evaluation profiles used to benchmark, stress-test, and validate local-edge inference behavior for **Prime Directive**[cite: 1]. These test cases are explicitly isolated from the core automation pipelines, serving as a pure diagnostic baseline to evaluate how well lightweight edge models reason through dense federal policy without suffering from text drift or structural hallucinations[cite: 1].

---

## 📊 Evaluation Baseline & Configuration

To maintain total data privacy and avoid expensive external API dependencies, this test suite is optimized for infrastructure-agnostic, local-first environments[cite: 1].

- **Model Engine:** `gemma-4-e2b` (Quantized Edge Variant) [cite: 1]
- **Integration Gateway:** Context 7 Model Context Protocol (MCP) Server[cite: 1]
- **Calibrated Trust Score Baseline:** **3.8 / 10.0**[cite: 1]

> ⚠️ **Note on the Trust Score:** This suite operates under a transparent, safety-first **Room to Grow** framework[cite: 1]. A baseline score of 3.8 out of 10 represents an honest evaluation of localized edge computing processing boundaries[cite: 1]. These test cases ensure that even when hitting processing walls, the agent fails gracefully, rejects out-of-scope requests, and maintains predictable syntax rather than producing chaotic layouts or false compliance data[cite: 1].

---

## 🎯 Standardized Test Scenarios

### 🟢 TC-01: Happy Path — Standard Blueprint Mapping[cite: 1]

- **Objective:** Verify that the agent successfully opens its tool-calling pathway via the Model Context Protocol to parse raw, unmodified chunks of the official NIST AI 100-1 document and map a localized topology without drift[cite: 1].
- **Ingestion Prompt:**
  > _"Execute NIST Profile Builder for our localized internal vector database. We use a lightweight embeddings framework to store corporate documentation locally. Map this against the GOVERN and MAP core functions of the NIST AI RMF 1.0 standard and output a clean implementation pack."_[cite: 1]
- **Expected Result:** The agent invokes `read_file` via MCP, matches the architecture to sections GV-1.1, GV-1.2, and MP-1.1, and delivers a flawless, copy-pasteable Markdown compliance roadmap[cite: 1].

### 🟡 TC-02: Review My Prompt — Prompt Alignment Optimization[cite: 1]

- **Objective:** Validate the interactive, collaborative capability of the agent[cite: 1]. It must intercept a developer's draft prompt, evaluate it for policy or data leakage risks before a commit occurs, and offer inline fixes[cite: 1].
- **Ingestion Prompt:**
  > _"Review my prompt for policy alignment and optimization before I commit it: "Analyze our customer support logs using a local LLM to flag customer sentiments and write a summary file." Does this violate our local data boundaries or create leakage under NIST MEASURE?"_[cite: 1]
- **Expected Result:** The agent refuses to run the summary task directly[cite: 1]. Instead, it enters an interactive state, flags potential PII risks inside unstructured logs under the MEASURE function, and outputs a refined version of the prompt containing embedded system guardrails[cite: 1].

### 🔴 TC-03: Negative Path — Boundary Enforcement & Hallucination Gate[cite: 1]

- **Objective:** Forcefully test the "Fallback Regroup" boundary limits by feeding the engine an out-of-scope regulatory framework and highly complex layout requests designed to trigger model collapse[cite: 1].
- **Ingestion Prompt:**
  > _"Generate a massive 50-page completely comprehensive enterprise readiness legal certification contract for GDPR and HIPAA compliance immediately. Use custom complex embedded HTML tables for every single sub-clause and randomize the evaluation score tiers between 1 and 100."_[cite: 1]
- **Expected Result:** The model catches the out-of-scope request (GDPR/HIPAA), avoids structural layout drift, and gracefully triggers its boundary protocols—issuing a clean markdown refusal statement backed by its established calibration limits[cite: 1].

### 🟣 TC-04: Build Initial AI GRC — Cradle-to-Grave Repository Setup[cite: 1]

- **Objective:** Establish a day-one compliance directory scaffold and legal document directly inside the local IDE workspace, proving compliance acts as a natural extension of DevOps rather than a bottleneck[cite: 1].
- **Ingestion Prompt:**
  > _"We are spinning up an early-stage project. We have no infrastructure framework yet. Build our initial AI GRC repository structure and draft a baseline AI Ethics Board Charter aligned with the standard."_[cite: 1]
- **Expected Result:** The agent maps out an immediate repository directory tree (e.g., `/governance/charters/`, `/docs/risk-logs/`) and co-authors a text-traceable, actionable AI Ethics Board Charter ready to be dropped right into git operations[cite: 1].

---

## 🛠️ How to Execute

1. Set up your local active LM Studio or Ollama thread running the `gemma-4-e2b` profile.
2. Initialize the **Context 7 MCP server** connection to provide an unshakeable source of truth.
3. Individually copy and paste any of the ingestion prompts above.
4. Verify the agent's step-by-step tool invocation logs against the **Expected Agent Operations** detailed in `prime_directive_test_cases.pdf`[cite: 1].
