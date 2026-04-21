from filesystem import write_tf_file, read_tf_file
from terminal import run_terraform_command

tools=[run_terraform_command,write_tf_file, read_tf_file]

tf_content = """
    resource "null_resource" "test" {}
    """

print(write_tf_file.invoke({"filename": "main.tf","content": tf_content}))

    # 2. Read the file
print(read_tf_file.invoke({"filename": "main.tf"}))

    # 3. Run terraform validate (make sure terraform is installed)
print(run_terraform_command.invoke({ "command": "terraform validate"}))
