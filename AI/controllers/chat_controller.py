from AI.orchestration.orchestrator import Orchestrator


class ChatController:
    """
    Coordinates chat requests between the UI and the AI pipeline.
    """

    def __init__(self):
        self.orchestrator = Orchestrator()

    def process_prompt(self, prompt):
        """
        Process a user prompt through the AI pipeline.

        Args:
            prompt (str): User input.

        Returns:
            dict: Response dictionary.
        """

        if not prompt or not prompt.strip():
            return {
                "success": False,
                "source": "system",
                "response": "Please enter a message."
            }

        try:
            result = self.orchestrator.process(prompt)
            return result
        except Exception as error:
            return {
                "success": False,
                "source": "system",
                "response": "Something went wrong while processing your request.",
                "error": str(error)
            }