import os
import json
import requests
from . import config


GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-latest:generateContent"

def get_api_key():
    return os.getenv("GEMINI_API_KEY")

def construct_prompt(repo_summary: str, bandit_report: str) -> str:

    return f"""
I will provide you with a comprehensive summary of a code repository (file structure and key file contents)
and a static analysis security report from the Bandit tool.

Your task is to perform a holistic review based *only* on the information provided and identify potential issues in the python files. Please structure your response in Markdown.

Based on the provided information, please analyze and report on the following:

1.  **High-Level Summary:** Provide a brief, one-paragraph summary of the repository's likely purpose and overall structure.
2.  **Vulnerability Hotspots:** Based on file names, dependencies, and the Bandit report, identify specific files(python) or code sections (python) that are most likely to contain security vulnerabilities (e.g., `auth.py`, `api/payment_processing.py`, files with many Bandit findings). Explain your reasoning.
3.  **Potential Static and Dynamic Vulnerabilities:** Suggest potential vulnerabilities that the static analyzer might have missed. Consider the code's described structure and dependencies to infer possible dynamic issues like race conditions, insecure object deserialization, injection flaws beyond simple SQLi, or business logic flaws.
4.  **Code Workflow and Architectural Issues:** Analyze the repository structure and identify any potential architectural flaws, poor coding practices, or workflow issues that could lead to security risks or maintenance problems (e.g., monolithic files, lack of tests, secrets in configuration files).
5.  **Actionable Recommendations:** Provide a short, bulleted list of the top 3-5 most important actions the development team should take to improve the repository's security posture.

---
Here is the repository summary:
---

**REPOSITORY SUMMARY (from Repomix)**

{repo_summary}


---
Here is the static analysis report:
---

**STATIC ANALYSIS REPORT (from Bandit)**

{bandit_report}
"""

def analyze_with_gemini():

    print("\n[Layer 3/3] 🧠 Starting AI Analysis with Gemini...")

    api_key = get_api_key()
    if not api_key:
        print("❌ Error: GEMINI_API_KEY environment variable not set.")
        print("   Skipping Layer 3 analysis. Please set the key and run again.")
        return

    # --- 1. Read the input files ---
    try:
        with open(config.REPOMIX_OUTPUT_PATH, 'r', encoding='utf-8') as f:
            repo_summary = f.read()
        
        with open(config.BANDIT_SIMPLIFIED_OUTPUT_PATH, 'r', encoding='utf-8') as f:
            # Load and re-dump the JSON to ensure it's nicely formatted for the prompt
            bandit_json = json.load(f)
            bandit_report = json.dumps(bandit_json, indent=2)

    except FileNotFoundError as e:
        print(f"❌ Error: Could not find input file for LLM analysis: {e.filename}")
        print("   Please ensure Layer 1 and Layer 2 completed successfully.")
        return

    # --- 2. Construct the prompt and API payload ---
    prompt = construct_prompt(repo_summary, bandit_report)
    
    headers = {
        'Content-Type': 'application/json',
    }
    
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    # --- 3. Call the Gemini API ---
    try:
        print("   Sending analysis data to Gemini. This may take a moment...")
        response = requests.post(f"{GEMINI_API_URL}?key={api_key}", headers=headers, json=payload, timeout=300)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)

        response_json = response.json()
        
        # --- 4. Extract and save the response ---
        # The response structure can vary slightly, so we add robust checking.
        if "candidates" in response_json and response_json["candidates"]:
            first_candidate = response_json["candidates"][0]
            if "content" in first_candidate and "parts" in first_candidate["content"] and first_candidate["content"]["parts"]:
                llm_response_text = first_candidate["content"]["parts"][0]["text"]
                
                with open(config.LLM_ANALYSIS_OUTPUT_PATH, 'w', encoding='utf-8') as f:
                    f.write(llm_response_text)
                
                print(f"✅ Success! Gemini analysis saved to: {config.LLM_ANALYSIS_OUTPUT_PATH}")
            else:
                 print("❌ Error: Received an unexpected response format from Gemini (missing content part).")
                 print(f"   Full Response: {response_json}")
        else:
            print("❌ Error: Received an empty or invalid response from Gemini.")
            print(f"   Full Response: {response_json}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: A network error occurred while contacting the Gemini API: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred during Gemini analysis: {e}")
