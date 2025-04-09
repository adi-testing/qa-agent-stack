import os
import requests

FAILURE_ANALYSIS_REPORT_PATH = "results/failure_analysis_report.txt"
BUG_REPORT_PATH = "results/bug_report.txt"
PROMPT_PATH = "prompts/bug_reporter_prompt.txt"

def read_prompt_template(file_path):
    # Reads the prompt template from a file.
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt template not found at: {file_path}")
    
    with open(file_path, "r") as f:
        return f.read()

def read_failure_analysis_report(file_path):
    # Reads the failure analysis report from a file.
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Failure analysis report not found at: {file_path}")

    with open(file_path, "r") as f:
        return f.read()

def generate_bug_report_with_llm(failure_analysis, api_url="http://127.0.0.1:1234"):
    # Generates a bug report using the LLM based on the failure analysis report.

    # Read the prompt template
    prompt_template = read_prompt_template(PROMPT_PATH)

    # Format the prompt with the failure analysis report
    prompt = prompt_template.format(failure_analysis=failure_analysis)

    payload = {
        "model": "mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "top_p": 0.9,
        "max_tokens": 1024
    }

    print("🧠 Sending failure analysis to LLM for bug report generation...")
    response = requests.post(f"{api_url}/v1/chat/completions", json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"❌ API error: {response.status_code}")
        print(response.text)
        return None

def save_bug_report(content, output_path):
    # Saves the bug report to a file.

    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the directory exists
    with open(output_path, "w") as f:
        f.write(content)
    print(f"📄 Bug report saved to: {output_path}")

def main():
    # Main function to read the failure analysis report, generate a bug report, and save it.
    DEFAULT_API_URL = "http://127.0.0.1:1234"

    try:
        # Read the failure analysis report
        failure_analysis = read_failure_analysis_report(FAILURE_ANALYSIS_REPORT_PATH)
        print("🔍 Failure Analysis Report:\n", failure_analysis)

        # Generate the bug report using the LLM
        bug_report = generate_bug_report_with_llm(failure_analysis, api_url=DEFAULT_API_URL)
        if bug_report:
            print("\n🛠️ Generated Bug Report:\n")
            print(bug_report)

            # Save the bug report to a file
            save_bug_report(bug_report, BUG_REPORT_PATH)
    except FileNotFoundError as e:
        print(f"❌ {e}")

if __name__ == "__main__":
     main()
