import os
import sys

print("--- Python Environment Detective ---")
print(f"[*] Python Executable Being Used: \n{sys.executable}\n")

print("[*] Checking the PATH variable seen by this script:")
path_variable = os.environ.get('PATH', 'PATH variable not found!')
path_entries = path_variable.split(os.pathsep)

venv_scripts_found = False
nodejs_found = False
nodejs_path = "C:\\Program Files\\nodejs" #usual Node.js installatin path

for i, entry in enumerate(path_entries):
    print(f"  {i+1}: {entry}")
    if "venv\\Scripts" in entry:
        venv_scripts_found = True
    if nodejs_path in entry.lower(): # Check case-insensitive
        nodejs_found = True

print("\n--- Analysis Results ---")
if venv_scripts_found:
    print("✅ SUCCESS: The venv's Scripts folder is in the PATH.")
else:
    print("❌ FAILURE: The venv's Scripts folder is MISSING from the PATH.")

if nodejs_found:
    print("✅ SUCCESS: The Node.js folder is in the PATH.")
else:
    print(f"❌ FAILURE: The Node.js folder ('{nodejs_path}') is MISSING from the PATH.")
    print("\n   >>> THIS IS THE REASON 'NPX' IS NOT FOUND. <<<")
