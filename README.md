# AI-Driven Automated Software Tester

A lightweight AI agent system that automates software testing. This tool reads your Python code, generates `pytest` unit tests using the LM Studio API, and saves them for execution. It is designed to simplify and accelerate the testing process.

---

## Features
- Automatically generates `pytest` unit tests for your Python code.
- Covers normal cases, edge cases, and invalid inputs.
- Uses LM Studio API for AI-driven test generation.

---

## Setup Instructions

### 1. General Setup
Ensure Python 3.8+ is installed on your system. Verify by running:
```bash
python3 --version
```
### 2. Clone This Repository
```bash
git clone https://github.com/<your-username>/<your-repository>.git    
cd <your-repository>
```
### 3. Setting Up and Connecting the AI Model
- Download and install LM Studio from LM Studio's official website.
- Start the LM Studio server locally.
- Configure the server to run on http://127.0.0.1:1234.
- Load the desired AI model (e.g., mistral-7b-instruct).
- Ensure the server is running and accessible by testing the endpoint:
```bash
curl http://127.0.0.1:1234/v1/chat/completions
```

### 4. Setting Up the Virtual Environment
Create a virtual environment:
```bash
python3 -m venv venv
```
Activate the virtual environment:
On macOS/Linux:
```bash
source venv/bin/activate
```
On Windows:
```bash
.\venv\Scripts\activate
```
### 5. Running the Project
Ensure the LM Studio server is running.
Run the test generator script:
```bash
python agents/test_generator.py
```
Generated test cases will be saved in:
```bash
tests/generated_tests.py
```
