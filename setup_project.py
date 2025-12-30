import os
import sys

# Add backend directory to path so imports work
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

# Script to setup the project
def setup():
    print("Setting up AI Todo Chatbot Project...")
    
    # 1. Create .env if not exists
    if not os.path.exists(".env"):
        print("Creating .env from .env.example...")
        with open(".env.example", "r") as src, open(".env", "w") as dst:
            dst.write(src.read())
        print("Please edit .env with your credentials.")

    print("\nBackend Setup:")
    print("1. cd backend")
    print("2. python -m venv venv")
    print("3. source venv/bin/activate (or venv\\Scripts\\activate)")
    print("4. pip install -r requirements.txt")
    
    print("\nFrontend Setup:")
    print("1. cd frontend")
    print("2. npm install")
    
    print("\nTo run:")
    print("Backend: uvicorn app.main:app --reload")
    print("Frontend: npm run dev")

if __name__ == "__main__":
    setup()

