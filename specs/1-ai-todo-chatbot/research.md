# Research & Technical Decisions

**Feature**: AI-Powered Todo Chatbot
**Date**: 2025-12-29

## Key Decisions

### 1. Official MCP SDK
*   **Decision**: Use `mcp` (or `mcp-server-py` depending on exact PyPI availability at install time) as the official SDK.
*   **Rationale**: The user explicitly requested the "Official MCP SDK". The standard Python SDK for MCP is usually provided under the `mcp` package.
*   **Alternatives Considered**: Custom implementation of MCP spec (Rejected: reinventing the wheel).

### 2. OpenAI Agents SDK Integration
*   **Decision**: Use `openai-agents-sdk` to manage the agent loop.
*   **Rationale**: Provides a structured way to handle tool calling, history management, and LLM interaction, aligning with the "Standardized AI Interaction" principle.
*   **Alternatives Considered**: Raw `openai` client (Rejected: Agents SDK offers higher-level abstractions for state management and tool binding).

### 3. Database & ORM
*   **Decision**: Neon Serverless PostgreSQL with `sqlmodel`.
*   **Rationale**: `sqlmodel` combines Pydantic validation with SQLAlchemy ORM, perfect for FastAPI. Neon provides a scalable, serverless backend that fits the "Stateless" principle.

### 4. Auth Provider
*   **Decision**: Better Auth.
*   **Rationale**: Explicitly requested by user.
*   **Implications**: Need to ensure Python integration/verification of Better Auth tokens (likely JWT based).

## Resolved Clarifications

*   **Package Naming**: Assumed `official-mcp-sdk` refers to the standard `mcp` library in Python. Will verify during installation.
*   **Stateless Flow**: Confirmed flow: Request -> Fetch DB History -> Rehydrate Agent -> Run Agent -> Store Result -> Response.
