import asyncio
import os
import sys

# Add current directory to path so we can import app
sys.path.append(os.getcwd())

# Load env vars manually for this script since uvicorn isn't doing it
from dotenv import load_dotenv
load_dotenv()

from app.agents.runner import OpenAIAgent
from app.core.config import settings

async def main():
    print(f"Checking API Key: {'Present' if settings.OPENAI_API_KEY else 'MISSING'}")
    
    try:
        agent = OpenAIAgent("test_user")
        print("Agent initialized.")
        result = await agent.run("Hello")
        print("Agent run successful.")
        print(result.content)
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
