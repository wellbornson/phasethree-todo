---
description: "Task list for AI-Powered Todo Chatbot feature implementation"
---

# Tasks: AI-Powered Todo Chatbot

**Input**: Design documents from `/specs/1-ai-todo-chatbot/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: Integrated into development flow as validation steps (manual verification per spec).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: [US1] Basic Task Mgmt, [US2] Context/Persistence, [US3] Complex Commands
- File paths are relative to repo root

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize project structure, install dependencies, and configure environment.

- [x] T001 Create project structure: backend/app, frontend/src, specs/contracts
- [x] T002 Initialize Python backend: pyproject.toml with dependencies (fastapi, uvicorn, sqlmodel, openai-agents-sdk, mcp, better-auth)
- [x] T003 [P] Initialize React frontend: package.json with dependencies (@openai/chatkit, vite, react)
- [x] T004 [P] Configure environment variables: .env.example (DATABASE_URL, OPENAI_API_KEY, NEXT_PUBLIC_OPENAI_DOMAIN_KEY)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required before any user story can be implemented.

- [x] T005 Setup Database: Create `backend/app/core/db.py` (engine, session) and `backend/alembic/` (migration config)
- [x] T006 [P] Create Base Entities: `backend/app/models/base.py` (SQLModel base classes)
- [x] T007 [P] Setup Auth: `backend/app/core/auth.py` (Better Auth integration stub/config)
- [x] T008 [P] Setup Agent Runner: `backend/app/agents/runner.py` (OpenAI Agent instantiation logic)
- [x] T009 [P] Setup MCP Server: `backend/app/tools/mcp_server.py` (Basic MCP server instance)
- [x] T010 Setup FastAPI App: `backend/app/main.py` (FastAPI app, CORS, include routers)

**Checkpoint**: Backend server starts, DB connects, frontend builds.

---

## Phase 3: User Story 1 - Basic Task Management (Priority: P1) 🎯 MVP

**Goal**: Users can perform CRUD operations on tasks using natural language.

**Independent Test**: Send messages like "Add task X", "List tasks", "Complete X" and verify DB state.

### Implementation for User Story 1

- [x] T011 [US1] Create Task Model: `backend/app/models/task.py` (Task entity)
- [x] T012 [P] [US1] Implement `add_task` Tool: `backend/app/tools/tasks.py` (MCP tool definition)
- [x] T013 [P] [US1] Implement `list_tasks` Tool: `backend/app/tools/tasks.py` (MCP tool definition)
- [x] T014 [P] [US1] Implement `complete_task` Tool: `backend/app/tools/tasks.py` (MCP tool definition)
- [x] T015 [P] [US1] Implement `delete_task` Tool: `backend/app/tools/tasks.py` (MCP tool definition)
- [x] T016 [US1] Bind Tools to Agent: Update `backend/app/agents/runner.py` to register task tools
- [x] T017 [US1] Implement Chat Endpoint: `backend/app/api/chat.py` (Handle POST /api/{user_id}/chat, invoke agent)
- [x] T018 [US1] Connect Frontend: `frontend/src/App.tsx` (ChatKit setup, API call to backend)

**Checkpoint**: Basic "Add/List/Complete/Delete" flow works via UI.

---

## Phase 4: User Story 2 - Conversational Context & Persistence (Priority: P1)

**Goal**: System remembers conversation history across sessions.

**Independent Test**: Refresh browser, see previous chat history.

### Implementation for User Story 2

- [x] T019 [US2] Create Conversation/Message Models: `backend/app/models/chat.py` (Conversation, Message entities)
- [x] T020 [US2] Implement History Service: `backend/app/services/history.py` (Fetch/Store messages in DB)
- [x] T021 [US2] Update Chat Endpoint: `backend/app/api/chat.py` (Load history before agent run, save new messages after)
- [x] T022 [US2] Update Frontend: `frontend/src/components/Chat.tsx` (Pass conversation_id, render history on load)

**Checkpoint**: Conversation history persists and reloads correctly.

---

## Phase 5: User Story 3 - Complex Command Chaining (Priority: P2)

**Goal**: Agent handles ambiguous or multi-step requests.

**Independent Test**: "Delete the meeting task" -> Agent lists tasks -> User confirms -> Agent deletes.

### Implementation for User Story 3

- [x] T023 [US3] Implement `update_task` Tool: `backend/app/tools/tasks.py` (MCP tool for updates)
- [ ] T024 [US3] Refine Agent Instructions: `backend/app/agents/prompts.py` (System prompt for chaining/confirmation behavior)
- [x] T025 [P] [US3] Add Error Handling: `backend/app/tools/tasks.py` (Graceful returns for "Not Found" etc.)
- [ ] T026 [US3] Frontend Tool Feedback: `frontend/src/components/ToolCall.tsx` (Visual indication of tool usage if supported by ChatKit)

**Checkpoint**: Complex flows and updates work smoothly.

---

## Phase 6: Polish & Documentation

**Purpose**: Finalize for delivery.

- [ ] T027 [P] Create Migrations: Run `alembic revision --autogenerate` and apply
- [ ] T028 [P] Write README: `README.md` (Setup, Auth, Env Vars)
- [ ] T029 [P] Verify Quickstart: Run through `specs/1-ai-todo-chatbot/quickstart.md` steps manually

---

## Dependencies & Execution Order

1.  **Phase 1 & 2** (Setup/Foundational) must complete first.
2.  **Phase 3** (US1 - MVP) is the core. Complete this to have a working "Agent".
3.  **Phase 4** (US2 - History) adds the "Chatbot" persistence.
4.  **Phase 5** (US3 - Advanced) adds sophistication.

## Parallel Opportunities

- Frontend (T003, T018, T022) can be worked on alongside Backend once API contract is stable.
- Individual MCP tools (T012-T015) can be implemented in parallel.
- Documentation (T028) can be written anytime after Phase 1.
