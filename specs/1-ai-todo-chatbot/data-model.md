# Data Model

## Entities

### Task
Represents a specific todo item to be completed.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `Integer` | Yes | Primary Key (Auto-increment) |
| `user_id` | `String` | Yes | Owner of the task (from Auth) |
| `title` | `String` | Yes | Short summary of the task |
| `description` | `String` | No | Detailed information |
| `completed` | `Boolean` | Yes | Status (Default: False) |
| `created_at` | `DateTime` | Yes | Timestamp of creation |
| `updated_at` | `DateTime` | Yes | Timestamp of last update |

### Conversation
Groups a sequence of messages between a user and the agent.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `Integer` | Yes | Primary Key |
| `user_id` | `String` | Yes | Owner of the conversation |
| `created_at` | `DateTime` | Yes | Start of conversation |
| `updated_at` | `DateTime` | Yes | Last activity |

### Message
A single turn in the conversation.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | `Integer` | Yes | Primary Key |
| `conversation_id` | `Integer` | Yes | Foreign Key to Conversation |
| `user_id` | `String` | Yes | Owner (Redundant but useful for queries) |
| `role` | `String` | Yes | `user` or `assistant` |
| `content` | `String` | Yes | Text content of the message |
| `created_at` | `DateTime` | Yes | Timestamp |

## Relationships

*   **User (External)** 1 : N **Tasks**
*   **User (External)** 1 : N **Conversations**
*   **Conversation** 1 : N **Messages**
