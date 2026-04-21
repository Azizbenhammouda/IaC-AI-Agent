import subprocess
from langchain.tools import tool

@tool
def run_security_check(directory: str):
    """
    Runs Checkov security scan on the terraform directory.
    Use this to find misconfigurations like open ports or unencrypted buckets.
    """
    # We run checkov on the current directory
    command = f"checkov -d {directory} --quiet --compact"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        return "Security Check Passed: No vulnerabilities found."
    else:
        # We return the failed security checks so the AI can fix them
        return f"Security Vulnerabilities Found:\n{result.stdout}"