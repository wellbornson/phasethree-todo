---
id: 009
title: force-db-url-env-var
stage: misc
date: 2025-12-29
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: wellbornsonAi
command: (logs show it still using old URL ep-xyz...)
labels: ["debug", "env", "database"]
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

(Logs showed `could not translate host name "ep-xyz.region.neon.tech"`, implying the old .env value was still being picked up despite the file change.)

## Response snapshot

Forced the `DATABASE_URL` directly in the start command to bypass potential caching or file reading issues.

## Outcome

- ✅ Impact: Server started with the correct URL forced in the shell.
- 🧪 Tests: N/A
- 📁 Files: No files modified.
- 🔁 Next prompts: Verify connection.
- 🧠 Reflection: The application might be caching the .env or reading from a different location. Forcing the env var proves if the URL itself works.

## Evaluation notes (flywheel)

- Failure modes observed: Stale environment variables
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): none
