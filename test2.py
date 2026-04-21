from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
import subprocess

# LLM
llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192"
)

# Tool: run Linux commands
def run_command(cmd):
    return subprocess.getoutput(cmd)

tools = [
    Tool(
        name="Terminal",
        func=run_command,
        description="Run Linux commands on the system"
    )
]

# Agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Run it
agent.run("Show me active network connections")