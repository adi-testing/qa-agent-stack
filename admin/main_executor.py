import subprocess

# Paths to the scripts
SCRIPTS = [
    "agents/test_generator.py",
    "agents/test_runner.py",
    "agents/failure_analyzer.py",
    "agents/bug_reporter.py",
    "agents/test_cases_generator.py"
]

def execute_script(script_path):
    """
    Executes a Python script using subprocess.
    """

    print(f"Executing {script_path}...")
    result = subprocess.run(["python", script_path], check=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error executing {script_path}:\n{result.stderr}")
        raise RuntimeError(f"Script {script_path} failed with error: {result.stderr}")
    
    print(f"✅ Successfully executed: {script_path}")
    print(result.stdout)

def main():
    """
    Main function to execute all scripts in the specified order.
    """
    try:
        for script in SCRIPTS:
            execute_script(script)
        print("All scripts executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
