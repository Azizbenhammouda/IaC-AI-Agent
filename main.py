from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools.terminal import run_terraform_command
from tools.filesystem import write_tf_file
from tools.filesystem import read_tf_file
from tools.security_tools import run_security_check

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile"
)

tools = [run_terraform_command, write_tf_file, run_security_check]

agent = create_agent(
    model=llm,
    tools=tools,
)

response = agent.invoke({
    "messages": [{
        "role": "user",
        "content": (
            "Create a secure AWS S3 bucket using Terraform. "
            "Write the code, validate it, and fix any issues including security issues."
        )
    }]
})

print("\nFINAL OUTPUT:\n", response["messages"][-1].content)