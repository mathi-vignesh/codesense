# repoguard/static_analysis.py
# Handles the execution of the Bandit static analysis tool.

import subprocess
import json
import os
from . import config
from .utils import redact_and_log_secret

def run_static_analysis(repo_path: str) -> bool:
    """
    Runs Bandit on the repository, saves the full report, and a simplified version.

    Args:
        repo_path: The absolute path to the Git repository.

    Returns:
        True if the analysis was successful, False otherwise.
    """
    print("\n[Layer 2/2] 🔍 Starting Static Analysis with Bandit...")
    
    bandit_raw_output = os.path.join(config.OUTPUT_DIR, "bandit_raw.json")
    
    # Construct the Bandit command
    command = [
        "bandit",
        "-r", repo_path,
        "-f", "json",
        "-o", bandit_raw_output,
        # Add arguments to exclude the venv folder to avoid scanning dependencies
        "-x", "./venv,./.venv" 
    ]

    try:
        subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False # Don't raise error if vulnerabilities are found (non-zero exit code)
        )

        if not os.path.exists(bandit_raw_output):
             print("❌ Error: Bandit did not produce an output file. There might be an issue with Bandit itself.")
             return False

        # Process the raw output to create a simplified version
        parse_and_simplify_bandit_report(bandit_raw_output)
        return True

    except FileNotFoundError:
        print("❌ Error: 'bandit' command not found.")
        print("   Please ensure Bandit is installed in your virtual environment (`pip install bandit`).")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred while running Bandit: {e}")
        return False

def parse_and_simplify_bandit_report(raw_report_path: str):
    """
    Reads the full JSON report from Bandit and creates a simplified,
    more readable version, redacting secrets along the way.
    """
    try:
        with open(raw_report_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        simplified_results = []
        vulnerability_count = 0

        # Clear the secrets log for this run
        if os.path.exists(config.SECRETS_LOG_PATH):
            os.remove(config.SECRETS_LOG_PATH)
        
        for issue in data.get("results", []):
            vulnerability_count += 1
            
            # Check if the finding is a potential hardcoded secret
            if issue.get("test_id") == "B105": # B105 is the test for hardcoded passwords
                redacted_code = redact_and_log_secret(issue)
                issue["code"] = redacted_code

            simplified_issue = {
                "file": issue.get("filename"),
                "line": issue.get("line_number"),
                "test_id": issue.get("test_id"),
                "issue_text": issue.get("issue_text"),
                "severity": issue.get("issue_severity"),
                "code_snippet": issue.get("code", "").strip()
            }
            simplified_results.append(simplified_issue)
        
        if not simplified_results:
             print("   ✅ Bandit found no security issues.")
             return

        print(f"   Bandit found {vulnerability_count} potential issues. Processing report...")
        output_data = {
            "vulnerability_count": vulnerability_count,
            "vulnerabilities": simplified_results
        }
        
        # Save the pretty-printed simplified report
        with open(config.BANDIT_SIMPLIFIED_OUTPUT_PATH, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=4)
        
        # Save the minified simplified report
        with open(config.BANDIT_MINIFIED_OUTPUT_PATH, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, separators=(',', ':'))

        print(f"   Parsing and simplifying Bandit output...")
        print(f"   ✅ Simplified report saved to: {config.BANDIT_SIMPLIFIED_OUTPUT_PATH}")
        print(f"   ✅ Compact report saved to: {config.BANDIT_MINIFIED_OUTPUT_PATH}")

    except json.JSONDecodeError:
        print(f"❌ Error: Could not parse the Bandit JSON report at '{raw_report_path}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while parsing the Bandit report: {e}")
