from llm import gemini_llm
from langchain.agents import create_agent

agent = create_agent(
    model=gemini_llm,
    system_prompt = "You are a helpful assistant",
    # tools = [live_cricket_score]
)

response = agent.invoke({
    "messages":[{"role": "user", "content": "What is a cat"}]
})

print(response)