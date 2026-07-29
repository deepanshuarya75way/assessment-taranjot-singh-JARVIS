"""
Orchestrator

The central coordinator of JARVIS.

Responsibilities
----------------
1. Analyze the request.
2. Decide whether Gemini is required.
3. Route service requests.
4. Build LLM context.
5. Delegate response formatting.
"""

from AI.preprocessing.request_analyzer import RequestAnalyzer
from AI.orchestration.context_builder import ContextBuilder
from AI.orchestration.tool_registry import ToolRegistry
from AI.orchestration.response_handler import ResponseHandler
from AI.preprocessing.models.intent import Intent

from AI.clients.gemini_client import GeminiClient
from AI.config.gemini_config import GeminiConfig


class Orchestrator:
    """Coordinates the complete AI workflow."""

    def __init__(self):
        self.request_analyzer = RequestAnalyzer()
        self.context_builder = ContextBuilder()
        self.tool_registry = ToolRegistry()
        self.response_handler = ResponseHandler()

        self.gemini = GeminiClient(
            GeminiConfig()
        )

    def process(self, user_prompt):
        """
        Main entry point of JARVIS.
        """

        analysis = self.request_analyzer.analyze(user_prompt)

        if analysis.needs_llm:
            return self._execute_llm(user_prompt)

        return self._execute_tool(analysis)

    def _execute_tool(self, analysis):
        """
        Execute a local tool or service.
        """

        if analysis.intent is None:
            return self.response_handler.handle_error(
                "No intent detected."
            )

        tool = self.tool_registry.get_tool(
            analysis.intent
        )

        if tool is None:
            return self.response_handler.handle_error(
                "No matching tool found."
            )

        entities = analysis.entities

        if not entities:
            return self.response_handler.handle_error(
                "Unable to extract required information."
            )

        parameters = entities.get("parameters", {})

        # Tools that do not require parameters.
        parameterless_intents = {
            Intent.LIST_NOTES,
        }

        if (
            analysis.intent not in parameterless_intents
            and not parameters
        ):
            return self.response_handler.handle_error(
                "No parameters extracted from the request."
            )

        try:
            # Version 1
            # Hardcoded until authentication is added.
            user_id = 1

            result = tool(
                user_id=user_id,
                **parameters
            )

            return self.response_handler.handle_service_response(
                result
            )

        except ValueError as error:
            return self.response_handler.handle_error(
                str(error)
            )
        except Exception as error:
            print(f"[Orchestrator] Unexpected Error: {error}")

            return self.response_handler.handle_error(
                "An unexpected error occurred while processing your request."
            )
        

    def _execute_llm(self, user_prompt):
        """
        Generate a response using Gemini.
        """

        try:
            context = self.context_builder.build_context(
                user_prompt
            )

            response = self.gemini.generate(
                context
            )

            return self.response_handler.handle_llm_response(
                response
            )

        except ValueError as error:
            return self.response_handler.handle_error(
                str(error)
            )

        except Exception as error:
            print(f"[Gemini] Unexpected Error: {error}")

            return self.response_handler.handle_error(
                "An unexpected error occurred while generating the response."
            )