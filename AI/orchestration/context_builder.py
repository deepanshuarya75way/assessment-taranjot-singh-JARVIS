"""
Context Builder

Responsible for preparing the prompt sent to Gemini.

Version 1:
    - Load system prompt
    - Include current user prompt

Future versions:
    - Conversation history
    - Long-term memory
    - RAG
    - User profile
"""

from pathlib import Path


class ContextBuilder:

    def __init__(self):

        self.prompt_path = Path("PROMPTS/master.txt")

    def _load_system_prompt(self) -> str:
        """
        Loads the master system prompt.
        """

        try:

            return self.prompt_path.read_text(encoding="utf-8")

        except FileNotFoundError:

            return ""

    def build_context(self, user_prompt: str) -> str:
        """
        Builds the complete prompt that will
        be sent to Gemini.
        """

        system_prompt = self._load_system_prompt()

        context = f"""
{system_prompt}

----------------------------
USER MESSAGE
----------------------------

{user_prompt}
"""

        return context.strip()