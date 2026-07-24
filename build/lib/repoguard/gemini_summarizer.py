# repoguard/gemini_summarizer.py
# New Layer 1: Uses the Gemini CLI to summarize the repository.

import subprocess
import os
import sys
from . import config

def generate_summary_with_gemini_cli(repo_path: str) -> bool:
    """
    Gathers all source code from the repository and uses the Gemini CLI
    to generate an LLM-compatible summary.
    """
    print("\n[Layer 1/2] 🚀 Starting Repository Summarization with Gemini CLI...")

    try:
        # This logic is self-contained and robust. It finds the gemini.exe
        # that was installed alongside the python.exe running this script.
        python_executable_dir = os.path.dirname(sys.executable)
        gemini_executable_path = os.path.join(python_executable_dir, 'gemini.exe' if sys.platform == "win32" else 'gemini')

        if not os.path.exists(gemini_executable_path):
            print(f"❌ Error: Gemini executable not found in the current virtual environment.")
            print(f"   Expected at: {gemini_executable_path}")
            print("   Please run 'pip install google-generativeai' in your active venv.")
            return False

        source_code_content = _gather_source_code(repo_path)
        if not source_code_content:
            print("   No source code files found to summarize. Skipping.")
            with open(config.SUMMARY_OUTPUT_PATH, "w", encoding='utf-8') as f:
                f.write("# Repository Summary\n\nNo summarizable files were found.")
            return True
        
        if len(source_code_content) > 500000:
             print("   Warning: Repository is very large and may exceed the prompt token limit.")
             print("   Processing large repository. This may take several minutes...")

        prompt = (
            "Summarise the following source code files. Explain their workflow, what the project is, "
            "and format the entire summary into an LLM-compatible format. "
            "Here is the codebase:\n\n"
            f"{source_code_content}"
        )

        command = [gemini_executable_path, "generate"]

        result = subprocess.run(
            command, input=prompt, capture_output=True, text=True, check=True, encoding='utf-8', timeout=300
        )

        with open(config.SUMMARY_OUTPUT_PATH, "w", encoding='utf-8') as f:
            f.write(result.stdout)
            
        print(f"✅ Success! Gemini summary saved to: {config.SUMMARY_OUTPUT_PATH}")
        return True

    except subprocess.TimeoutExpired:
        print("❌ Error: The Gemini summarization process timed out after 5 minutes.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Gemini CLI for summarization. Return code: {e.returncode}")
        if "token limit" in e.stderr.lower():
             print("   Hint: The repository content is too large and exceeds the model's token limit.")
        print(f"   Stderr: {e.stderr.strip()}")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred during summarization: {e}")
        return False

def _gather_source_code(repo_path: str) -> str:
    """Walks through the repo and concatenates the content of relevant files."""
    combined_content = ""
    include_extensions = {'.py', '.js', '.html', '.css', '.md', '.txt', '.json', '.toml', '.yaml', '.sh'}
    exclude_dirs = {'__pycache__', '.git', '.venv', 'venv', 'node_modules', 'dist', 'build'}

    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if any(file.endswith(ext) for ext in include_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        relative_path = os.path.relpath(file_path, repo_path)
                        combined_content += f"\n--- File: {relative_path} ---\n{content}"
                except Exception:
                    continue
    return combined_content
