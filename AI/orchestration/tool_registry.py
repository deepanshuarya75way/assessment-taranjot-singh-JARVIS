"""
Tool Registry

The Tool Registry acts as the bridge between the
Orchestrator and the Service Layer.

It maps:

    intent

to the actual Python function that performs the work.

The Orchestrator never imports Notes, Reminders,
or Memories directly.
"""
from AI.preprocessing.models.intent import Intent

from SERVICES.notes_service import (
    create_new_note,
    fetch_note,
    edit_note,
    remove_note,
    fetch_all_notes,
)

from SERVICES.reminders_service import (
    create_new_reminder,
    remove_reminder,
    fetch_all_reminders,
)

from SERVICES.memories_service import (
    create_new_memory,
    fetch_memory,
)


class ToolRegistry:
    """Registry that maps detected intents to service functions."""

    def __init__(self):

        # Intent -> Service Function mapping
        self.tools = {
            Intent.CREATE_NOTE: create_new_note,
            Intent.READ_NOTE: fetch_note,
            Intent.UPDATE_NOTE: edit_note,
            Intent.DELETE_NOTE: remove_note,
            Intent.LIST_NOTES: fetch_all_notes,

            Intent.CREATE_REMINDER: create_new_reminder,
            Intent.DELETE_REMINDER: remove_reminder,
            Intent.LIST_REMINDERS: fetch_all_reminders,

            Intent.CREATE_MEMORY: create_new_memory,
            Intent.READ_MEMORY: fetch_memory,
}

    def get_tool(self, intent: Intent):
        """Return the function associated with the detected intent."""
        if not intent:
            return None

        return self.tools.get(intent)

    def has_tool(self, intent: Intent) -> bool:
        return self.get_tool(intent) is not None

    def list_intents(self):
        """
        Returns all registered intents.
        """
        return [intent.name for intent in self.tools.keys()]

    def register_tool(self, intent: Intent, tool):
        """Register a new tool at runtime."""
        self.tools[intent] = tool