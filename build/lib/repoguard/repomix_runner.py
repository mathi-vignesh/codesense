import subprocess
import os
import platform
from . import config

def run_repomix(repo_path: str):

    print("\n[Layer 1/2] 🚀 Starting Repository Summarization with Repomix...")

    git_dir_path = os.path.join(repo_path, '.git')
    if not os.path.isdir(git_dir_path):
        print(f"❌ Error: The provided path is not a valid Git repository.")
        print(f"   Path: '{repo_path}'")
        print(f"   A '.git' directory was not found. Repomix requires a Git repository to analyze.")
        return False
    
    npx_path = "C:\\Program Files\\nodejs\\npx.cmd"
    if not os.path.exists(npx_path):
        print(f"❌ CRITICAL ERROR: The command 'npx.cmd' was not found at the hardcoded path:")
        print(f"   '{npx_path}'")
        print("   Please verify your Node.js installation directory and update the path in this script if needed.")
        return False


    #absolute path to the output file
    output_file_path = os.path.abspath(config.REPOMIX_OUTPUT_PATH)
    
    #Fixed SYNTAX: The error shows 'markdown' is seen as a path.
    #The correct syntax is just using '--stdout' which defaults to md.
    repomix_command = f'"{npx_path}" repomix --stdout'
    
    command_str = f'cd /d "{repo_path}" && {repomix_command} > "{output_file_path}"'

    try:
        result = subprocess.run(
            command_str,
            capture_output=True, # Still capture stderr for error reporting
            text=True,
            encoding='utf-8',
            shell=True
        )

        if result.returncode != 0:
            print(f"❌ Error running Repomix. Return code: {result.returncode}")
            if 'Need to install the following packages' in result.stderr:
                print("\n   >>> ACTION REQUIRED <<<")
                print("   This is a normal first-time setup for Repomix.")
                print("   Please run the command again and type 'y' when prompted.")
            else:
                stderr_output = result.stderr.strip() if result.stderr else "(No error message was produced)"
                print(f"   Stderr: {stderr_output}")
            return False

        print(f"✅ Success! Repomix summary saved to: {output_file_path}")
        return True
        
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

