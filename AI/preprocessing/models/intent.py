from enum import Enum


class Intent(Enum):
   

    UNKNOWN = "unknown"

    # Conversation
    CHAT = "chat"

    # Notesa
    CREATE_NOTE = "create_note"
    READ_NOTE = "read_note"
    UPDATE_NOTE = "update_note"
    DELETE_NOTE = "delete_note"
    LIST_NOTES = "list_notes"

    # Reminders
    CREATE_REMINDER = "create_reminder"
    READ_REMINDER = "read_reminder"
    UPDATE_REMINDER = "update_reminder"
    DELETE_REMINDER = "delete_reminder"
    LIST_REMINDERS = "list_reminders"

    # Memories
    CREATE_MEMORY = "create_memory"
    READ_MEMORY = "read_memory"
    UPDATE_MEMORY = "update_memory"
    DELETE_MEMORY = "delete_memory"
    LIST_MEMORIES = "list_memories"

    # Conversations
    CREATE_CONVERSATION = "create_conversation"
    LOAD_CONVERSATION = "load_conversation"
    DELETE_CONVERSATION = "delete_conversation"

    # Future Features
    RAG = "rag"
    PDF = "pdf"
    WEB_SEARCH = "web_search"