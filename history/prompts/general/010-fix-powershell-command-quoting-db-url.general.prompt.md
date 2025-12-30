---
id: 010
title: fix-powershell-command-quoting-db-url
stage: misc
date: 2025-12-29
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: wellbornsonAi
command: (from logs) CommandNotFoundException for the connection string assignment
labels: ["debug", "powershell", "env"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - backend/.env
tests:
 - none
---

## Prompt

(User provided logs showing `The term 'postgresql://...' is not recognized` and subsequently `OperationalError: could not translate host name "ep-xyz..."` because the previous command failed to set the env var correctly in PowerShell.)

## Response snapshot

Corrected the PowerShell command syntax by ensuring the `DATABASE_URL` string is properly quoted.

## Outcome

- ✅ Impact: The environment variable should now be set correctly in the shell session.
- 🧪 Tests: N/A
- 📁 Files: Re-verified `backend/.env` content.
- 🔁 Next prompts: Check server startup.
- 🧠 Reflection: PowerShell parsed the unquoted URL as a command due to special characters. Quoting it fixes this.

## Evaluation notes (flywheel)

- Failure modes observed: Shell syntax error
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): none
