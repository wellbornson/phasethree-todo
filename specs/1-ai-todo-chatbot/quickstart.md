# Quickstart Guide

## Prerequisites
*   Node.js 18+
*   Python 3.10+
*   Neon Database URL

## Backend Setup

1.  Navigate to `backend/`:
    ```bash
    cd backend
    ```
2.  Create virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```
3.  Install dependencies:
    ```bash
    pip install fastapi uvicorn sqlmodel openai-agents-sdk mcp better-auth
    ```
4.  Set environment variables (`.env`):
    ```ini
    DATABASE_URL=postgresql://user:pass@ep-xyz.region.neon.tech/neondb
    OPENAI_API_KEY=sk-...
    ```
5.  Run server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Frontend Setup

1.  Navigate to `frontend/`:
    ```bash
    cd frontend
    ```
2.  Install packages:
    ```bash
    npm install @openai/chatkit
    ```
3.  Set environment variables (`.env.local`):
    ```ini
    NEXT_PUBLIC_OPENAI_DOMAIN_KEY=...
    ```
4.  Run development server:
    ```bash
    npm run dev
    ```

## Verification
*   Open frontend at `http://localhost:5173`.
*   Send a message: "Add a task to buy milk".
*   Check database to see the new task.
