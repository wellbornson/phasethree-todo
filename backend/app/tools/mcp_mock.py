# Mock for missing MCP SDK
class Server:
    def __init__(self, name):
        self.name = name
        self.tools = []

    def tool(self):
        def decorator(func):
            self.tools.append(func)
            return func
        return decorator

    def get_tools(self):
        return self.tools
