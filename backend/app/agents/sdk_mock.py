# Mock for missing OpenAI Agents SDK
class Agent:
    def __init__(self, name, instructions, tools):
        self.name = name
        self.instructions = instructions
        self.tools = tools

    async def run(self, message):
        # Mock response
        return MockResult(content=f"Echo: {message}", tool_calls=[])

class AgentRunner:
    def __init__(self):
        pass

class MockResult:
    def __init__(self, content, tool_calls):
        self.content = content
        self.tool_calls = tool_calls
