import subprocess
import os

FAILURE_OUTPUT_PATH = "results/failure_output.txt"

def run_tests_and_save_failures(test_dir="tests"):
    """
    Run pytest and save the raw failure messages to a file.

    Args:
        test_dir (str): The directory containing the test files.
    """
    print("▶️ Running pytest...")
    result = subprocess.run(
        ["pytest", test_dir, "--tb=short", "--maxfail=5"],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print("✅ All tests passed!")
        # Ensure the results directory exists
        os.makedirs(os.path.dirname(FAILURE_OUTPUT_PATH), exist_ok=True)
        with open(FAILURE_OUTPUT_PATH, "w") as f:
            f.write("All tests passed!")
        return

    output = result.stdout
    print("❌ Some tests failed. Saving failure info...")
    # Ensure the results directory exists
    os.makedirs(os.path.dirname(FAILURE_OUTPUT_PATH), exist_ok=True)
    with open(FAILURE_OUTPUT_PATH, "w") as f:
        f.write(output)

if __name__ == "__main__":
    run_tests_and_save_failures()