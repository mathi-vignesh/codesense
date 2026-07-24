# repoguard/gemini_summarizer.py
# New Layer 1: Uses the Gemini CLI to summarize the repository.

import subprocess
import os
from . import config

def generate_summary_with_gemini_cli(repo_path: str) -> bool:
    """
    Gathers all source code from the repository and uses the Gemini CLI
    to generate an LLM-compatible summary.

    Args:
        repo_path: The absolute path to the Git repository.

    Returns:
        True if the summary was generated successfully, False otherwise.
    """
    print("\n[Layer 1/2] 🚀 Starting Repository Summarization with Gemini CLI...")

    try:
        source_code_content = _gather_source_code(repo_path)
        if not source_code_content:
            print("   No source code files found to summarize. Skipping.")
            # Create an empty summary file to allow the process to continue.
            with open(config.SUMMARY_OUTPUT_PATH, "w", encoding='utf-8') as f:
                f.write("# Repository Summary\n\nNo summarizable files were found.")
            return True
        
        # Check for large files which might exceed token limits
        if len(source_code_content) > 500000: # 500k char limit as a safeguard
             print("   Warning: Repository is very large and may exceed the prompt token limit for the CLI.")

        prompt = (
            "You are a code analysis tool. Your task is to create a concise, "
            "LLM-compatible markdown summary of the following codebase. "
            "Include the file structure and a brief description of each file's purpose. "
            "Do not include the full code content in your summary. Here is the codebase:\n\n"
            f"{source_code_content}"
        )

        # Using the gemini CLI to generate the content
        command = ["gemini", "generate", "--prompt", prompt]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )

        with open(config.SUMMARY_OUTPUT_PATH, "w", encoding='utf-8') as f:
            f.write(result.stdout)
            
        print(f"✅ Success! Gemini summary saved to: {config.SUMMARY_OUTPUT_PATH}")
        return True

    except FileNotFoundError:
        print("❌ Error: 'gemini' command not found.")
        print("   Please ensure the Gemini CLI is installed and configured. See the README for instructions.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Gemini CLI for summarization. Return code: {e.returncode}")
        print(f"   Stderr: {e.stderr.strip()}")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred during summarization: {e}")
        return False

def _gather_source_code(repo_path: str) -> str:
    """Walks through the repo and concatenates the content of relevant files."""
    combined_content = ""
    # Define file types to include and directories to exclude
    include_extensions = {'.py', '.js', '.html', '.css', '.md', '.txt', '.json', '.toml', '.yaml', '.sh'}
    exclude_dirs = {'__pycache__', '.git', '.venv', 'venv', 'node_modules', 'dist', 'build'}

    for root, dirs, files in os.walk(repo_path):
        # Modify the list of directories in-place to prevent os.walk from descending into them
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in include_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        relative_path = os.path.relpath(file_path, repo_path)
                        combined_content += f"\n--- File: {relative_path} ---\n"
                        combined_content += content
                except Exception:
                    # Ignore files that can't be read
                    continue
    return combined_content
