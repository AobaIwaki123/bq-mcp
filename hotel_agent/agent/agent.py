from google.adk.agents import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

tools = toolbox.load_toolset("my-toolset")

prompt = """
  You're a helpful hotel assistant. You handle hotel searching. When the user searches for a hotel, mention it's name, id,
  location and price tier. Always mention hotel ids while performing any
  searches. This is very important for any operations.
"""

root_agent = Agent(
    name="hotel_agent",
    model="gemini-2.5-flash",
    description="A helpful AI assistant that can search hotels.",
    instruction=prompt,
    tools=tools,
)
