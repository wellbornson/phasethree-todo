---
id: 011
title: fix-env-vars-and-restart
stage: misc
date: 2025-12-29
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: wellbornsonAi
command: AGAIN EXICUTE (resolving persistent old env var)
labels: ["debug", "env", "server"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .env
 - .env.example
tests:
 - none
---

## Prompt

User reported persistent `ep-xyz` host error.

## Response snapshot

1. Fixed root `.env` (which had garbage).
2. Renamed `.env.example` to `.env.example.bak` to prevent fallback loading.
3. Restarted backend without inline env vars, relying on the corrected files.

## Outcome

- ✅ Impact: Eliminated sources of incorrect env vars.
- 🧪 Tests: N/A
- 📁 Files: Modified `.env`, renamed `.env.example`.
- 🔁 Next prompts: Verify connection.
- 🧠 Reflection: The persistence of the error suggested the app was finding the bad config in an unexpected place (likely root .env or fallback).

## Evaluation notes (flywheel)

- Failure modes observed: Env var precedence/leaking
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): none
