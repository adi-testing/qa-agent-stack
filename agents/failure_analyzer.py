import requests
import os
import re

PROMPT_PATH = "prompts/failure_analysis_prompt.txt"
FAILURE_OUTPUT_PATH = "results/failure_output.txt"
ANALYSIS_REPORT_PATH = "results/failure_analysis_report.txt"  # Path to save the analysis report

def load_prompt(template_path, failures):
    # Load and fill the prompt template.

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Prompt template not found at: {template_path}")

    with open(template_path, "r") as f:
        template = f.read()

    return template.format(failures=failures)

def analyze_failures_with_llm(failure_text, api_url="http://127.0.0.1:1234"):
    # Ask the LLM to explain and suggest fixes for test failures.

    prompt = load_prompt(PROMPT_PATH, failure_text)

    payload = {
        "model": "mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "top_p": 0.9,
        "max_tokens": 1024
    }

    print("🧠 Sending failure details to LLM for analysis...")
    response = requests.post(f"{api_url}/v1/chat/completions", json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"❌ API error: {response.status_code}")
        print(response.text)
        return None

def extract_failures_from_file(file_path):
    # Extract failing test messages from a saved file.

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Failure output file not found at: {file_path}")

    with open(file_path, "r") as f:
        pytest_output = f.read()

    match = re.search(r"=+ FAILURES =+(.*?)(=+ short test summary info =+)", pytest_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return pytest_output  # fallback

def save_analysis_report(content, output_path):
    # Save the failure analysis report to a file.

    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the directory exists
    with open(output_path, "w") as f:
        f.write(content)
    print(f"📄 Failure analysis report saved to: {output_path}")

def main():
    # Main function to orchestrate the failure analysis process.
    
    # Default API URL for consistency with test_generator.py
    DEFAULT_API_URL = "http://127.0.0.1:1234"

    try:
        # Extract failure details from the failure output file
        failure_details = extract_failures_from_file(FAILURE_OUTPUT_PATH)
        print("🔍 Extracted Failures:\n", failure_details)

        # Analyze the failures using the LLM
        analysis = analyze_failures_with_llm(failure_details, api_url=DEFAULT_API_URL)
        if analysis:
            print("\n🛠️ Suggested Fixes:\n")
            print(analysis)

            # Save the analysis report to a file
            save_analysis_report(analysis, ANALYSIS_REPORT_PATH)
    except FileNotFoundError as e:
        print(f"❌ {e}")

if __name__ == "__main__":
    main()