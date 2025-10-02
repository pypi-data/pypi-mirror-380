# Copyright (c) Microsoft. All rights reserved.

import asyncio

from agent_framework import HostedCodeInterpreterTool, TextContent, TextReasoningContent, UsageContent
from agent_framework.openai import OpenAIResponsesClient

"""
OpenAI Responses Client Reasoning Example

This sample demonstrates advanced reasoning capabilities using OpenAI's o1 models,
showing step-by-step reasoning process visualization and complex problem-solving.
"""


async def reasoning_example() -> None:
    """Example of reasoning response (get results as they are generated)."""
    print("=== Reasoning Example ===")

    agent = OpenAIResponsesClient(model_id="gpt-5").create_agent(
        name="MathHelper",
        instructions="You are a personal math tutor. When asked a math question, "
        "write and run code using the python tool to answer the question.",
        tools=HostedCodeInterpreterTool(),
        reasoning={"effort": "high", "summary": "detailed"},
    )

    query = "I need to solve the equation 3x + 11 = 14. Can you help me?"
    print(f"User: {query}")
    print(f"{agent.name}: ", end="", flush=True)
    usage = None
    async for chunk in agent.run_stream(query):
        if chunk.contents:
            for content in chunk.contents:
                if isinstance(content, TextReasoningContent):
                    print(f"\033[97m{content.text}\033[0m", end="", flush=True)
                elif isinstance(content, TextContent):
                    print(content.text, end="", flush=True)
                elif isinstance(content, UsageContent):
                    usage = content
    print("\n")
    if usage:
        print(f"Usage: {usage.details}")


async def main() -> None:
    print("=== Basic OpenAI Responses Reasoning Agent Example ===")

    await reasoning_example()


if __name__ == "__main__":
    asyncio.run(main())
