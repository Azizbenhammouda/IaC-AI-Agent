from langchain.tools import tool

@tool
def write_tf_file(filename:str,content:str):
  """
    Creates or overwrites a Terraform file (.tf) with the provided content.
    Input should be the filename (e.g., 'main.tf') and the file content.
    """
  with open(filename, "w") as f:
        f.write(content)
  return f"Successfully wrote {filename}"

@tool
def read_tf_file(filename:str):
    """
    Reads the content of a Terraform file.
    Use this to inspect code before modifying it.
    """
    try:
        with open(filename,"r") as f:
            return f.read()
    except FileNotFoundError:
        return "file not found"
    
