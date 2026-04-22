import subprocess
from langchain.tools import tool

@tool
def run_terraform_command(command: str):
  """
    Executes a terraform command in the terminal.
    Use this to run 'terraform validate', 'terraform plan', etc.
    Input should be the full command string (e.g., 'terraform validate').
    """
  try:
    result=subprocess.run(command, shell=True, capture_output=True, text=True) #risk here
    if result.returncode == 0:
            return f"Success:\n{result.stdout}"
    else:
            return f"Error:\n{result.stderr}"
  except Exception as e:
        return f"Execution failed: {str(e)}"

