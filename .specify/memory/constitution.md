<!-- Sync Impact Report
Version Change: 0.0.0 -> 1.0.0 (Initial Ratification)
Modified Principles: Established core values (Reliability, Politeness, Efficiency, Completeness, MCP Standardization)
Added Sections: Technology Stack & Architecture, Delivery & Automation
Templates Requiring Updates: ✅ None (Initial Setup)
Follow-up TODOs: None
-->

# Phase III AI-Powered Todo Chatbot Constitution

## Core Principles

### I. Reliability & Stateless Architecture
The system MUST be designed with a stateless architecture to ensure scalability, resilience, and horizontal scaling. Components should not rely on local memory for state persistence across requests; all state must be persisted to the database (Neon Serverless PostgreSQL). This ensures the system is resilient to restarts and capable of seamless scaling.

### II. Politeness & User Experience
Agent interactions MUST be friendly, confirmatory, and handle errors gracefully. The system should embody a helpful and warm persona. User intent should be confirmed (e.g., "I've added that task for you"), and ambiguities should be resolved proactively or by chaining tool calls, ensuring a smooth conversational flow.

### III. Efficiency & Sophistication
Implementation MUST prioritize efficiency, speed, and cleanliness. Code should be sophisticated yet minimal ("refined logic"), avoiding unnecessary boilerplate. Solutions should be idiomatic to the chosen technology stack (Python/FastAPI/React) and optimized for performance.

### IV. Completeness & Functional Integrity
The solution MUST cover all specified requirements: basic task operations (CRUD), database models (Task, Conversation, Message), and specific MCP tool definitions. Agent behaviors must include natural language processing for task operations, history fetching, and error handling. No feature should be left partially implemented; "working" means fully functional from the user's perspective.

### V. Standardized AI Interaction (MCP & Agents SDK)
The project MUST utilize the Official Model Context Protocol (MCP) SDK for defining tools and the OpenAI Agents SDK for agent logic. This ensures a standardized, modular approach to AI-application interaction. Tools (add_task, list_tasks, etc.) are the primary interface for the agent to interact with the database.

## Technology Stack & Architecture

**Stack:**
*   **Frontend:** OpenAI ChatKit (React/Vite)
*   **Backend:** Python FastAPI, OpenAI Agents SDK, Official MCP SDK
*   **Database:** Neon Serverless PostgreSQL (SQLModel ORM)
*   **Auth:** Better Auth

**Architecture:**
*   **Flow:** ChatKit UI -> FastAPI (`/api/{user_id}/chat`) -> Agents SDK -> MCP Server -> Neon DB.
*   The API endpoint MUST be stateless, persisting conversation history and messages to the DB.

## Delivery & Automation

**Deliverables:**
*   Complete GitHub repository structure: `/frontend`, `/backend`, `/specs`.
*   Database migrations via SQLModel.
*   Comprehensive `README.md` with setup instructions, environment variable configuration, and usage guide.

**Automation:**
*   All setup and installation steps (e.g., `pip install`, `npm install`) MUST be automated via scripts or clearly provided as executable commands. The user should not be required to perform manual coding.

## Governance

This Constitution supersedes all other project documentation. Any deviation from these principles requires a formal amendment to this document.
*   **Amendments:** Must be documented with a clear rationale and version bump.
*   **Compliance:** All specifications (`/specs`), plans, and code changes must be verified against these principles.
*   **Version Control:** Semantic versioning (MAJOR.MINOR.PATCH) applies to this governance document.

**Version**: 1.0.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29