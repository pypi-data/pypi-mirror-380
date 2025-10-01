from dotenv import load_dotenv
from timbal import Agent
from timbal.tools import WebSearch

load_dotenv()


agent = Agent(
    name="eve",
    model="openai/gpt-4o-mini",
    tools=[WebSearch()],
    model_params={
        "max_tokens": 2048,
    }
)
   

async def main():
    while True:
        prompt = input("User: ")
        if prompt == "q":
            break
        await agent(prompt=prompt).collect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
