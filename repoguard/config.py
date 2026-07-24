import os

#OP Dir
OUTPUT_DIR = "outputs"

#Layer 1: Repomix
REPOMIX_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "document1.md")

#Layer 2: Bandit
BANDIT_SIMPLIFIED_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "document2.json")
BANDIT_MINIFIED_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "document2.min.json")
SECRETS_LOG_PATH = os.path.join(OUTPUT_DIR, "secrets_redacted.log")

#Layer 3: Gemini
LLM_ANALYSIS_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "llm_analysis.md")

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

