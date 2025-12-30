---
id: 015
title: provide-server-commands
stage: general
date: 2025-12-29
surface: agent
model: gemini
feature: none
branch: 1-ai-todo-chatbot
user: wellbornsonAi
command: give me commands for both servers i will execute my self
labels: ["cli", "instructions", "server"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - none
tests:
 - none
---

## Prompt

give me commands for both servers i will execute my self

## Response snapshot

Provided the manual shell commands for starting the FastAPI backend and Vite frontend.

## Outcome

- ✅ Impact: User can now manually manage server lifecycle.
- 🧪 Tests: None.
- 📁 Files: None modified.
- 🔁 Next prompts: User reports issues or continues development.
- 🧠 Reflection: User preferred manual control over the automated background process I initiated previously.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null
