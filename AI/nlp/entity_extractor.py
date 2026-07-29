from AI.preprocessing.models.intent import Intent


class EntityExtractor:
    """Extracts entities required by each intent."""

    def extract(self, intent, doc):
        """
        Dispatch entity extraction based on the detected intent.
        """

        if intent == Intent.CREATE_NOTE:
            result = self._extract_note(doc)
            return result

        if intent == Intent.UPDATE_NOTE:
            result = self._extract_note(doc)
            return result

        if intent == Intent.CREATE_REMINDER:
            result = self._extract_reminder(doc)
            return result
        
        if intent == Intent.READ_NOTE:
            result = self._extract_note_title(doc)
            return result

        if intent == Intent.LIST_NOTES:
            result = {
                "entity_type": "notes",
                "parameters": {}
            }
            return result

        if intent == Intent.DELETE_NOTE:
            result = self._extract_note_title(doc)
            return result

        return None

    def _extract_note(self, doc):
        """
        Extract the title and content for create/update note intents.
        Supports:
        - Create a note called Shopping with content Buy milk
        - Update note Shopping with content Buy eggs
        - Edit note Shopping with content Buy bread
        - Change note Shopping with content Buy fruits
        """

        text = doc.text.strip()

        is_update = text.lower().startswith(("update", "edit", "change"))

        title = ""
        content = ""

        if is_update and " to " in text:
            before, content = text.split(" to ", 1)
            content = content.strip()

            tokens = before.split()
            try:
                note_index = tokens.index("note")
                title = " ".join(tokens[note_index + 1:]).strip()
            except ValueError:
                title = ""

            if not title:
                return None

            return {
                "entity_type": "notes",
                "parameters": {
                    "title": title,
                    "content": content,
                },
            }

        if "with content" in text:
            before, content = text.split("with content", 1)
            content = content.strip()
        else:
            before = text

        separators = ["called", "named", "titled"]

        after = None
        for separator in separators:
            if separator in before:
                after = before.split(separator, 1)[1].strip()
                break

        if after is None:
            tokens = before.split()
            try:
                note_index = tokens.index("note")
                after = " ".join(tokens[note_index + 1:]).strip()
            except ValueError:
                after = ""

        title = after.strip()

        if not title:
            return None

        return {
            "entity_type": "notes",
            "parameters": {
                "title": title,
                "content": content,
            },
        }

    def _extract_reminder(self, doc):
        """
        Placeholder for reminder extraction.
        """

        return {
            "entity_type": "reminders",
            "parameters": {},
        }

    def _extract_note_title(self, doc):
        """
        Extract only the note title for delete operations.
        """

        text = doc.text

        title = ""

        separators = ["called", "named", "titled", "note"]

        after = ""

        for separator in separators:
            if separator in text:
                after = text.split(separator, 1)[1]
                break

        title = after.strip()

        if not title:
            return None

        return {
            "entity_type": "notes",
            "parameters": {
                "title": title,
            },
        }