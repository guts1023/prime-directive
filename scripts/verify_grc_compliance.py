#!/usr/bin/env python3
"""
Prime Directive GRC - Structural Verification Script
Version: 1.0.2 (Context7 Unified)
Description: Programmatically enforces the presence of all required GRC playbooks,
             slash command prompts, and structural configuration maps.
"""

import os
import sys
import json
from pathlib import Path

class GRCValidator:
    def __init__(self):
        self.repo_root = self.find_repo_root()
        self.config_path = self.repo_root / "context7.json" if self.repo_root else None

    def find_repo_root(self):
        """Walks up from the script location to find the true repo root containing context7.json."""
        current = Path(__file__).resolve().parent
        for parent in [current] + list(current.parents):
            if (parent / "context7.json").exists():
                return parent
        return Path(os.getcwd()).resolve()

    def load_config(self):
        """Loads and parses the unified context7.json configuration file."""
        if not self.config_path or not self.config_path.exists():
            print(f"❌ CRITICAL ERROR: Configuration file 'context7.json' not found.")
            print(f"   Searched root location: {self.repo_root}")
            return None
        try:
            with open(self.config_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ CRITICAL ERROR: Failed to parse 'context7.json'. Invalid JSON formatting: {e}")
            return None

    def validate_repository(self):
        """Executes full structural validation against directories and file maps."""
        print("⚡ [Prime Directive GRC] Starting Repository Integrity Audit...")
        config = self.load_config()
        if not config:
            return False

        error_count = 0
        
        # 1. Validate Target Subdirectories
        print("\n📁 Auditing Directory Infrastructure:")
        directories = config.get("directories", {})
        for key, relative_path in directories.items():
            full_dir_path = self.repo_root / relative_path
            if full_dir_path.exists() and full_dir_path.is_dir():
                print(f"  ✅ [FOUND] Configured Path '{key}': {relative_path}/")
            else:
                print(f"  ❌ [MISSING] Expected Directory '{key}' at location: {relative_path}/")
                error_count += 1

        # 2. Validate Active Slash Command Prompt Files
        print("\n🤖 Auditing Active Slash Command Prompt Assets:")
        slash_commands = config.get("slash_commands", {})
        for command, relative_file_path in slash_commands.items():
            full_file_path = self.repo_root / relative_file_path
            if full_file_path.exists() and full_file_path.is_file():
                print(f"  ✅ [READY] Command '{command}' mapped to: {relative_file_path}")
            else:
                print(f"  ❌ [MISSING] Active prompt asset for '{command}' at: {relative_file_path}")
                error_count += 1

        # Final Report Aggregation
        print("\n📊 GRC Structural Integrity Summary:")
        if error_count > 0:
            print(f"❌ AUDIT FAILED: {error_count} structural non-compliance errors identified.")
            return False
        
        print("✅ AUDIT PASSED: Repository architecture complies perfectly with Prime Directive specifications.")
        return True

if __name__ == "__main__":
    validator = GRCValidator()
    if not validator.validate_repository():
        sys.exit(1)
    sys.exit(0)