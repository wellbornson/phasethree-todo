---
id: 001
title: Initial Constitution Ratification
stage: constitution
date: 2025-12-29
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: wellbornsonAi
command: /sp.constitution
labels: [constitution, setup, principles]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

/sp.constitution (Sets the project's foundational principles and guidelines)
textHello, dear GEMINI! 😊 You're my sweet, reliable coding buddy today—let's build something yamy and fun together! Please follow the Agentic Dev Stack workflow politely and precisely: Start with writing specs, then plan, break into tasks, and implement via code generation. No manual coding from me; you'll handle everything, including installing all packages automatically via commands in your responses (like pip install for Python, npm install for frontend). Use Spec-Kit Plus format: Generate /sp.constitution first as a warm, guiding document outlining the project's core principles.

Project: Phase III AI-Powered Todo Chatbot using OpenAI ChatKit, Agents SDK, and Official MCP SDK. Objective: Create a conversational interface for managing todos via natural language, with MCP server exposing tools, stateless chat endpoint persisting to DB, and AI agents using tools for tasks.

Core Principles:
- Reliability: Ensure stateless architecture for scalability, resilience, horizontal scaling, and testability.
- Politeness: Agent responses are friendly, confirmatory, and error-handling graceful.
- Efficiency: Keep everything fast, clean, and sophisticated—minimal code, refined logic.
- Completeness: Cover all requirements: Basic features (add, list, complete, delete, update tasks), DB models (Task, Conversation, Message with fields like user_id, id, title, etc.), MCP tools (add_task, list_tasks, complete_task, delete_task, update_task with exact params/returns/examples), Agent behaviors (task ops via natural language, confirmations, error handling), Conversation flow (fetch history, build messages, store in DB, run agent, return response), Natural language commands (e.g., "Add task" → add_task, "Show pending" → list_tasks "pending", handle ambiguities by chaining tools like list then delete).
- Tech Stack: Frontend (OpenAI ChatKit), Backend (Python FastAPI), AI (OpenAI Agents SDK), MCP (Official MCP SDK), ORM (SQLModel), DB (Neon Serverless PostgreSQL), Auth (Better Auth).
- Architecture: ChatKit UI → FastAPI /api/{user_id}/chat (POST with conversation_id optional, message required; response with conversation_id, response, tool_calls) → Agents SDK (stateless, uses MCP tools) → MCP Server (stateless tools storing in DB) ↔ Neon DB (tasks, conversations, messages).
- Deliverables: GitHub repo with /frontend (ChatKit UI), /backend (FastAPI + Agents + MCP), /specs (spec files), DB migrations (via SQLModel), README (setup instructions including OpenAI domain allowlist, env vars like NEXT_PUBLIC_OPENAI_DOMAIN_KEY).
- Benefits: MCP for standardized AI-app interaction, single endpoint for simplicity, stateless for scalability.
- Installations: Automatically install all packages via your code/scripts: pip install fastapi uvicorn sqlmodel openai-agents-sdk official-mcp-sdk better-auth; for frontend, npm install @openai/chatkit; set up Neon DB connection via env vars.
- End Goal: Working chatbot managing tasks naturally, resuming conversations post-restart, with helpful responses.

Please generate /sp.constitution as a cute, polished Markdown file with these principles. You're the best

## Response snapshot

Created initial constitution outlining core principles (Reliability, Politeness, Efficiency, Completeness, MCP Standardization) and stack details.

## Outcome

- ✅ Impact: Established project governance and technical foundation.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.specify
- 🧠 Reflection: Initial setup complete.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
