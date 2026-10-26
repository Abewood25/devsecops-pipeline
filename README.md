
# DevSecOps Security Pipeline

## Project Overview

This project demonstrates the implementation of an automated DevSecOps CI/CD pipeline using Python, FastAPI, GitHub Actions, and multiple security scanning tools.

The goal is to integrate security testing directly into the software development lifecycle (SDLC), allowing potential vulnerabilities to be identified before code is released.

## Technologies Used

- Python 3.12
- FastAPI
- GitHub Actions
- Pytest
- Bandit (Static Application Security Testing)
- pip-audit (Dependency Vulnerability Scanning)
- GitHub CodeQL (Static Code Analysis)
- Git and GitHub

## Security Features

### 1. Automated Testing
Pytest runs automatically when changes are pushed to the main branch, helping identify application defects.

### 2. Static Application Security Testing
Bandit scans Python source code for potential security weaknesses.

### 3. Dependency Vulnerability Scanning
pip-audit checks Python dependencies against known security vulnerability advisories.

### 4. CodeQL Security Analysis
GitHub CodeQL performs automated security analysis of Python source code.

### 5. Automated CI/CD
GitHub Actions executes automated tests and security scans whenever changes are pushed to the main branch.

## Vulnerability Remediation Example

During development, pip-audit identified two vulnerable Python dependencies:

- certifi
- opentelemetry-api

The affected dependency requirements were updated to versions meeting the reported fixes.

The GitHub Actions workflow was rerun successfully after remediation.

This demonstrates a practical security workflow:

Detection -> Investigation -> Remediation -> Verification

## Project Structure

    devsecops-pipeline/
    |-- .github/
    |   |-- workflows/
    |       |-- ci.yml
    |       |-- codeql.yml
    |-- app/
    |-- tests/
    |-- requirements.txt
    |-- .gitignore
    |-- README.md

## Running Locally

Create a virtual environment:

    python -m venv .venv

Activate it on Windows PowerShell:

    .venv\Scripts\Activate.ps1

Install dependencies:

    python -m pip install -r requirements.txt

Run automated tests:

    python -m pytest

Run the FastAPI application:

    uvicorn app.main:app --reload

## Results

- Automated CI pipeline successfully executed
- Pytest automated testing passed
- Bandit security scanning passed
- Dependency vulnerability scanning passed after remediation
- CodeQL analysis completed successfully
- Zero open CodeQL code scanning alerts reported on the main branch at the time of verification

## Skills Demonstrated

- DevSecOps practices
- CI/CD pipeline automation
- Secure software development
- Python application testing
- Static application security testing
- Software supply-chain security
- Vulnerability detection and remediation
- GitHub Actions workflow troubleshooting

## Future Improvements

- Container image security scanning
- Secret detection
- Branch protection and pull request security checks
- Automated security reporting
