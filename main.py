import subprocess
from agents import test_generator

def run_tests():
    result = subprocess.run(["pytest", "tests/generated_tests.py"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    print("=== Generating Tests ===")
    test_generator.run()
    
    print("\n=== Running Tests ===")
    run_tests()
