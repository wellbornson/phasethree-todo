import requests
import sys

BASE_URL = "http://localhost:8000/api/test_user/chat"

def chat(message, conversation_id=None):
    payload = {"message": message}
    if conversation_id:
        payload["conversation_id"] = conversation_id
    
    try:
        response = requests.post(BASE_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
        if hasattr(e, 'response') and e.response:
            print(e.response.text)
        sys.exit(1)

def main():
    print("1. Adding a dummy task...")
    chat("Add a task to debug the agent")
    
    print("\n2. Asking 'How many tasks?'...")
    resp = chat("How many tasks do I have?")
    print(f"Response: {resp['response']}")
    
    if any(char.isdigit() for char in resp['response']):
         print("\nSUCCESS: Agent seemingly found tasks.")
    else:
         print("\nWARNING: Agent might not have found tasks (check debug output).")

if __name__ == "__main__":
    main()

