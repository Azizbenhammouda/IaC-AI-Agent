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
def print_banner():
    banner = """
██╗ █████╗  ██████╗     █████╗ ██╗
██║██╔══██╗██╔════╝    ██╔══██╗██║
██║███████║██║         ███████║██║
██║██╔══██║██║         ██╔══██║██║
██║██║  ██║╚██████╗    ██║  ██║██║
╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝  ╚═╝╚═╝
               
    """
    print("\033[94m" + banner + "\033[0m")          
    print("  Infrastructure as Code — AI Agent")
    print("\033[92m  v1.0.0  ✦  powered by LangChain + Groq\033[0m")  
    print("  " + "─" * 40 + "\n")

def run_cli():
    print_banner()
    print(" Terraform AI Agent")
    print("=" * 40)
    print("Type your infrastructure request below.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print("\n Agent is working...\n")

        try:
            response = agent.invoke({
                "messages": [{
                    "role": "user",
                    "content": user_input
                }]
            })
            print("\n Agent:\n")
            print(response["messages"][-1].content)
            print("\n" + "=" * 40 + "\n")

        except Exception as e:
            print(f"\n Error: {str(e)}\n")

if __name__ == "__main__":
    run_cli()
