import asyncio

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_utcp import UTCPClient


async def main():
    # Define a configuration for the UTCP client. This tells it where to find the tool manuals.
    utcp_config = {
        "manual_call_templates": [
            {
                "name": "open_library_api",
                "call_template_type": "http",
                "http_method": "GET",
                "url": "https://openlibrary.org/static/openapi.json",
                "content_type": "application/json",
            },
            # You can add more manuals here
        ]
    }

    # Initialize the Langchain-UTCP client using the configuration
    # This will create and manage an official UtcpClient instance internally.
    client = await UTCPClient.create(config=utcp_config)

    # Load all tools from all configured manuals as LangChain tools
    tools = await client.aload_tools()
    print(f"Loaded {len(tools)} tools.")
    for tool in tools:
        print(f"- {tool.name}")

    # Set up your LangChain agent as usual
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Run the agent
    result = await agent_executor.ainvoke(
        {"input": "Search for books by J.R.R. Tolkien"}
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
