import argparse
import os
from .utils import setup_output_directory, is_valid_repo
from .repomix_runner import run_repomix
from .static_analysis import run_static_analysis
# Make sure to import the new function
from .llm_analyzer import analyze_with_gemini

def main():
    """
    Parses command-line arguments and orchestrates the analysis workflow.
    """
    parser = argparse.ArgumentParser(
        description="RepoGuard: A multi-layer repository analysis tool."
    )
    
    # Main command parser
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # 'analyze' command
    analyze_parser = subparsers.add_parser(
        "analyze", help="Run a full analysis on a repository."
    )
    analyze_parser.add_argument(
        "repo_path", type=str, help="The file path to the local Git repository."
    )
    
    # --- FIX: Add the definition for the new flag ---
    # This line tells argparse to recognize --ai-analysis.
    analyze_parser.add_argument(
        "--ai-analysis",
        action="store_true", # Makes it a flag that doesn't need a value (e.g., --ai-analysis True)
        help="Enable Layer 3 analysis with the Gemini LLM. Requires GEMINI_API_KEY environment variable."
    )

    args = parser.parse_args()

    # --- Workflow Orchestration ---
    if args.command == "analyze":
        repo_path = os.path.abspath(args.repo_path)

        if not is_valid_repo(repo_path):
            return

        setup_output_directory()

        # --- Layer 1 ---
        if not run_repomix(repo_path):
            print("\nSkipping further analysis due to Repomix failure.")
            return

        # --- Layer 2 ---
        if not run_static_analysis(repo_path):
            print("\nSkipping further analysis due to Bandit failure.")
            return
            
        # --- Layer 3: Run only if the flag is present ---
        # This `if` statement checks if the user included --ai-analysis
        if args.ai_analysis:
            analyze_with_gemini()
        
        print("\n🎉 Analysis complete!")

if __name__ == "__main__":
    main()
