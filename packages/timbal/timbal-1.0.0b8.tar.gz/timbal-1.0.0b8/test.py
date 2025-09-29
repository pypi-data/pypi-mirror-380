from dotenv import load_dotenv
from timbal import Agent
from timbal.tools import Bash, WebSearch

load_dotenv()


def get_datetime():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


agent = Agent(
    name="test_web_search",
    # model="anthropic/claude-sonnet-4-0",
    model="openai/gpt-4.1-mini",
    # model="openai/gpt-5-mini",
    tools=[
        WebSearch(), 
        # Bash("*", background_mode="auto"),
        # get_datetime,
    ],
    model_params={
        # "max_tokens": 10000,
        # "thinking": {
        #     "effort": "low",
        #     "summary": "auto"
        # }
    }
)

async def main():
    # await agent(prompt="search in linkedin who's the CEO of Timbal AI").collect()
    # await agent(prompt="What time is it?").collect()
    # await agent(prompt="Thanks!").collect()
    # await agent(prompt="hello").collect()
    # await agent(
    #     prompt="Reason step by step: A person is facing north. They turn 90 degrees right, then 180 degrees left. In what direction are they facing now?",
    #     thinking={
    #         "effort": "low",
    #         "summary": "auto"
    #         # "type": "enabled",
    #         # "budget_tokens": 1024
    #     }
    # ).collect()
    # await agent(prompt="Cool. Thanks!").collect()
    while True:
        prompt = input("User: ")
        if prompt == "q":
            break
        await agent(prompt=prompt).collect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
