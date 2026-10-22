
from llm import gemini_llm
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from tools import live_cricket_score, live_football_score

memory = InMemorySaver()

agent = create_agent(
    model=gemini_llm,
    tools=[live_cricket_score, live_football_score],
    system_prompt="You are a helpful assistant",
    checkpointer=memory
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is a cat?"
            }
        ]
    },
    config={
        "configurable": {
            "thread_id": "1"
        }
    }
)

print(response)
