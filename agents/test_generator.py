import os
from utils.llm_utils import send_prompt_to_llm  

def read_file(file_path):
    # Reads the content of a file and returns it as a string.

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as f:
        return f.read()

def generate_tests(code, prompt_template, api_url="http://127.0.0.1:1234"):
    # Sends a prompt to the LM Studio API to generate test cases.

    # Format the prompt by inserting the code into the template
    prompt = prompt_template.format(code=code)
    print(f"Formatted Prompt Sent to API:\n{prompt}")  # Debugging: Print the full prompt

    # Use the shared utility function to send the prompt to the LLM
    try:
        generated_text = send_prompt_to_llm(prompt, api_url=api_url)
        if not generated_text:
            raise ValueError("No test cases were generated by the model.")
        return generated_text
    except Exception as e:
        raise Exception(f"An error occurred while generating tests: {e}")

def save_file(content, output_path):
    # Saves the generated test code to a file.

    # Replace placeholder module name and any occurrences of 'src.calculator'
    content = content.replace("from your_module", "from calculator")
    content = content.replace("from src.calculator", "from calculator")

    # Extract the Python code block from the content
    start = content.find("```python")
    end = content.rfind("```")
    if start != -1 and end != -1:
        content = content[start + len("```python"):end].strip()

    # Prepend the required import statements
    import_statements = (
        "import sys\n"
        "import os\n"
        "sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))\n\n"
    )
    content = import_statements + content

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(content)
    print(f"📄 Test file saved to: {output_path}")

def main():
    # Main function to orchestrate reading code, generating tests, and saving them.

    try:
        # Paths to the source code and prompt template
        code_path = 'src/calculator.py'
        prompt_path = 'prompts/test_gen_prompt.txt'
        output_path = 'tests/test_generated_tests.py'

        # Read the source code and prompt template
        code = read_file(code_path)
        prompt_template = read_file(prompt_path)

        # Generate test cases using the LM Studio API
        test_code = generate_tests(code, prompt_template)

        # Save the generated test cases to the output file
        save_file(test_code, output_path)

        print(f"Test cases successfully generated and saved to '{output_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
