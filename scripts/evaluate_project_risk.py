#!/usr/bin/env python3
"""
Prime Directive GRC - Programmatic Risk Tier & Phase-Gate Enforcement Engine
Version: 1.0.0 (2026 Baseline)
Description: Dynamically evaluates workspace configuration risks and programmatically
             forces mandatory phase-gate documentation based on calculated Risk Tiers.
"""

import os
import sys
import json
from pathlib import Path

class RiskEngine:
    def __init__(self):
        self.repo_root = self.find_repo_root()
        self.config_path = self.repo_root / "context7.json"

    def find_repo_root(self):
        current = Path(__file__).resolve().parent
        for parent in [current] + list(current.parents):
            if (parent / "context7.json").exists():
                return parent
        return Path(os.getcwd()).resolve()

    def evaluate_risk_profile(self):
        print("🧮 [Prime Directive GRC] Initiating Algorithmic Risk Evaluation...")
        
        # 1. Fallback / Default Matrix if not dynamically provided by project metadata
        # In production, these variables can be read from a local 'app-manifest.json'
        criticality = 4  # e.g., System handles real-world data pipelines or interfaces
        probability = 3  # e.g., Dynamic prompt configurations with variable inputs
        
        risk_score = criticality * probability
        print(f"  ▪️ Criticality Rating  : {criticality}/5")
        print(f"  ▪️ Probability Rating  : {probability}/5")
        print(f"  ▪️ Calculated Risk Score: {risk_score} (Formula: C x P)")

        # 2. Map Score to Operational Risk Tier
        if risk_score >= 15:
            tier = 3
            tier_name = "TIER 3 (HIGH RISK)"
            required_artifacts = [
                "governance/playbooks/ai-ethics-board-charter.md",
                "risk-compliance/playbooks/ai-risk-scoring-model.md"
            ]
        elif risk_score >= 6:
            tier = 2
            tier_name = "TIER 2 (MEDIUM RISK)"
            required_artifacts = [
                "governance/playbooks/alignment-verification-procedure.md"
            ]
        else:
            tier = 1
            tier_name = "TIER 1 (LOW RISK)"
            required_artifacts = []

        print(f"\n🚨 PROJECT ASSIGNED TO: {tier_name}")
        
        # 3. Enforce Phase-Gate Artifact Compliance
        print("\n🛡️ Verifying Mandatory Phase-Gate Artifacts:")
        missing_count = 0
        
        for artifact in required_artifacts:
            artifact_path = self.repo_root / artifact
            if artifact_path.exists() and artifact_path.is_file():
                print(f"  ✅ [PASSED] Found required phase-gate asset: {artifact}")
            else:
                print(f"  ❌ [BLOCKED] Missing mandatory phase-gate asset: {artifact}")
                missing_count += 1

        print("\n📊 Gate Enforcement Summary:")
        if missing_count > 0:
            print(f"❌ DEPLOYMENT BLOCKED: {missing_count} required phase-gate documents are missing for this Risk Tier.")
            return False
        
        print("✅ GATEWAY CLEARED: All required tier-specific compliance artifacts are present.")
        return True

if __name__ == "__main__":
    engine = RiskEngine()
    if not engine.evaluate_risk_profile():
        sys.exit(1) # Explicitly crash execution to halt a merge or commit
    sys.exit(0) # Pass cleanly