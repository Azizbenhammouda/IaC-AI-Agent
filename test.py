from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile"
)

response = llm.invoke("Explain what a firewall does in one sentence")
print(response.content)