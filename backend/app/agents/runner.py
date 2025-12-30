import json
import inspect
import asyncio
from typing import List, Optional, Any
from openai import AsyncOpenAI
from app.core.config import settings
from app.tools.mcp_server import mcp_server
from app.agents.prompts import SYSTEM_PROMPT

class AgentResult:
    def __init__(self, content: str, tool_calls: List[dict] = None):
        self.content = content
        self.tool_calls = tool_calls or []

class OpenAIAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.tools = mcp_server.get_tools()
        self.tool_map = {func.__name__: func for func in self.tools}
        self.tool_schemas = self._generate_tool_schemas()

    def _generate_tool_schemas(self) -> List[dict]:
        schemas = []
        for func in self.tools:
            sig = inspect.signature(func)
            parameters = {"type": "object", "properties": {}, "required": []}
            for name, param in sig.parameters.items():
                if name == "user_id": continue
                p_type = "string"
                if param.annotation == int: p_type = "integer"
                parameters["properties"][name] = {"type": p_type}
                if param.default == inspect.Parameter.empty: parameters["required"].append(name)
            schemas.append({"type": "function", "function": {"name": func.__name__, "description": inspect.getdoc(func), "parameters": parameters}})
        return schemas

    async def run(self, message: str, history: List[Any] = None) -> AgentResult:
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        if history:
            for msg in history: messages.append({"role": msg.role, "content": msg.content})
        messages.append({"role": "user", "content": message})

        all_tools = []
        try:
            for _ in range(3): # Max 3 turns for speed
                response = await asyncio.wait_for(
                    self.client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=self.tool_schemas, tool_choice="auto"),
                    timeout=5.0 # Total 5s timeout for LLM
                )
                msg = response.choices[0].message
                if not msg.tool_calls:
                    return AgentResult(content=msg.content or "✅ Done!", tool_calls=all_tools)

                messages.append(msg.model_dump(exclude_none=True))
                for tc in msg.tool_calls:
                    name, args = tc.function.name, json.loads(tc.function.arguments)
                    all_tools.append({"name": name, "args": args})
                    res = self.tool_map[name](user_id=self.user_id, **args)
                    messages.append({"tool_call_id": tc.id, "role": "tool", "name": name, "content": json.dumps(res)})
            return AgentResult(content="✅ **Done!** I've updated your list.", tool_calls=all_tools)
        except asyncio.TimeoutError:
            return AgentResult(content="I'm still working on it, Zahid! 🚀", tool_calls=all_tools)
        except Exception as e:
            return AgentResult(content=f"Sorry Zahid, I hit a snag: {str(e)}", tool_calls=all_tools)

def get_agent(user_id: str):
    return OpenAIAgent(user_id)
