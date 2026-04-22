import subprocess
from langchain.tools import tool
import json

@tool
def run_security_check(directory: str):
    """
    Runs Checkov security scan on a Terraform directory.
    Returns structured security findings.
    """

    try:
        result = subprocess.run(
            ["checkov", "-d", directory, "--output", "json"],
            capture_output=True,
            text=True
        )

        if not result.stdout:
            return f"Error: No output from Checkov.\n{result.stderr}"

        output = json.loads(result.stdout)

        return output

    except json.JSONDecodeError:
        return f"Failed to parse Checkov output:\n{result.stdout}"

    except Exception as e:
        return f"Scan failed: {str(e)}"