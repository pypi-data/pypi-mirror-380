from datetime import datetime

import httpx
from dotenv import load_dotenv
from timbal import Agent, Workflow
from timbal.state import get_run_context
from timbal.tools import Bash, WebSearch, Write

load_dotenv()


def get_datetime() -> str:
    return datetime.now().isoformat()


async def fetch_content(url: str) -> str:
    async with httpx.AsyncClient(follow_redirects=True) as client:
        res = await client.get(url)
        res.raise_for_status()
        return res.text


agent = Agent(
    name="demo_agent",
    model="openai/gpt-5-mini",
    tools=[get_datetime, WebSearch()]
)
    

workflow = (Workflow(name="demo_workflow")
    .step(fetch_content)
    .step(Write(), path="./content.txt", content=lambda: get_run_context().step_span("fetch_content").output) 
)


async def main():
    await workflow(url="https://timbal.ai").collect()
    # await agent(prompt="What time is it?").collect()
    # await agent(prompt="What's the weather like in Barcelona?").collect()
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
    # while True:
    #     prompt = input("User: ")
    #     if prompt == "q":
    #         break
    #     await agent(prompt=prompt).collect()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
