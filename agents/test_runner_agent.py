import subprocess
import os

FAILURE_OUTPUT_PATH = "results/failure_output.txt"

def save_to_file(content, file_path):
    ''' Saves the given content to a file.
    Args:
        content (str): The content to save.
        file_path (str): The path to the file where the content will be saved.     
    '''
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  
    with open(file_path, "w") as f:
        f.write(content)
    print(f"📄 Output saved to: {file_path}")

def run_tests_and_save_failures(test_dir="tests"):
    ''' Run pytest and save the raw failure messages to a file.
    Args:
        test_dir (str): The directory containing the tests. Defaults to "tests".
    '''
    print("▶️ Running pytest...")
    result = subprocess.run(
        ["pytest", test_dir, "--tb=short", "--maxfail=5"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("✅ All tests passed!")
        save_to_file("All tests passed!", FAILURE_OUTPUT_PATH)
        return
    output = result.stdout
    print("❌ Some tests failed. Saving failure info...")
    save_to_file(output, FAILURE_OUTPUT_PATH)

if __name__ == "__main__":
    run_tests_and_save_failures()