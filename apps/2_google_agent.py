from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()
memory = MemorySaver()

agent =  create_agent(
    model = llm,
    tools = [search.run],
    checkpointer = memory,
    system_prompt = "you are a agent and can search for any question on google."
)

while True:
    query = input("user:")
    if query.lower() == "quit":
        print("bye bye 🐖")
        break

    response = agent.invoke(
                {"messages":[{"role" : "user", "content": query}]},
                {"configurable":{"thread_id":"1"}} 
            )
    print(response["messages"][-1].content)