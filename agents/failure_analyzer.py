import subprocess
import requests
import re
import os

PROMPT_PATH = "prompts/failure_analysis_prompt.txt"

def run_tests_and_capture_failures(test_dir="tests"):
    """
    Run pytest and return the raw failure messages.
    """
    print("▶️ Running pytest...")
    result = subprocess.run(
        ["pytest", test_dir, "--tb=short", "--maxfail=5"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✅ All tests passed!")
        return None

    output = result.stdout
    print("❌ Some tests failed. Capturing failure info...")
    return output


def extract_failures(pytest_output):
    """
    Extract failing test messages from pytest output.
    """
    match = re.search(r"=+ FAILURES =+(.*?)(=+ short test summary info =+)", pytest_output, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return pytest_output  # fallback


def load_prompt(template_path, failures):
    """
    Load and fill the prompt template.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Prompt template not found at: {template_path}")

    with open(template_path, "r") as f:
        template = f.read()

    return template.format(failures=failures)


def analyze_failures_with_llm(failure_text, api_url="http://127.0.0.1:1234"):
    """
    Ask the LLM to explain and suggest fixes for test failures.

    Args:
        failure_text (str): The extracted failure details from pytest output.
        api_url (str): The base URL of the LM Studio API.

    Returns:
        str: The analysis and suggested fixes from the LLM.
    """
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


if __name__ == "__main__":
    # Default API URL for consistency with test_generator.py
    DEFAULT_API_URL = "http://127.0.0.1:1234"

    pytest_output = run_tests_and_capture_failures()

    if pytest_output:
        failure_details = extract_failures(pytest_output)
        print("🔍 Extracted Failures:\n", failure_details)

        analysis = analyze_failures_with_llm(failure_details, api_url=DEFAULT_API_URL)
        if analysis:
            print("\n🛠️ Suggested Fixes:\n")
            print(analysis)
    else:
        print("🎉 No failures to analyze.")
