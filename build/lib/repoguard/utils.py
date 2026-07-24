import os
import json
from . import config

def setup_output_directory():
    """
    Ensures the output directory exists.
    """
    try:
        os.makedirs(config.OUTPUT_DIR, exist_ok=True)
        print(f"✅ Output directory is ready at: '{config.OUTPUT_DIR}/'")
    except OSError as e:
        print(f"❌ Error creating output directory '{config.OUTPUT_DIR}': {e}")
        exit(1)

def is_valid_repo(repo_path: str) -> bool:
    """
    Checks if the provided path is a valid Git repository by looking for a .git directory.

    Args:
        repo_path: The path to check.

    Returns:
        True if it's a valid repo, False otherwise.
    """
    if not os.path.isdir(repo_path):
        print(f"❌ Error: The provided path is not a valid directory.")
        print(f"   Path: '{repo_path}'")
        return False

    git_dir_path = os.path.join(repo_path, '.git')
    if not os.path.isdir(git_dir_path):
        print(f"❌ Error: The provided path is not a valid Git repository.")
        print(f"   Path: '{repo_path}'")
        print(f"   A '.git' directory was not found. Analysis requires a Git repository.")
        return False
        
    return True

def redact_and_log_secret(issue: dict) -> str:
    """
    Redacts a potential secret from an issue's code line and logs it.
    This is a simple implementation for demonstration.

    Args:
        issue: The issue dictionary from Bandit.

    Returns:
        The line of code with the secret redacted.
    """
    line_with_secret = issue.get("code", "")
    redacted_line = "POTENTIAL_SECRET_REDACTED"
    
    # Log the original finding for local review
    log_message = (
        f"REDACTED POTENTIAL SECRET:\n"
        f"  File: {issue.get('filename')}\n"
        f"  Line: {issue.get('line_number')}\n"
        f"  Test ID: {issue.get('test_id')}\n"
        f"  Original Line: {line_with_secret.strip()}\n"
        f"----------------------------------------\n"
    )

    with open(config.SECRETS_LOG_PATH, "a", encoding='utf-8') as f:
        f.write(log_message)
    
    return redacted_line
