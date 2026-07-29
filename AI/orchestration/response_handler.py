"""
Response Handler

Responsible for formatting every response returned
by the Orchestrator.

Having a dedicated handler keeps the Orchestrator
focused only on coordination.
"""


class ResponseHandler:
    """Formats responses returned by the orchestrator."""

    def _build_response(self, success, source, response, data=None):
        """Create a standardized response dictionary."""
        return {
            "success": success,
            "source": source,
            "response": response,
            "data": data,
        }

    def handle_service_response(self, response):
        """
        Formats responses coming from the
        Service Layer.
        """

        if isinstance(response, dict):
            return self._build_response(
                success=response.get("success", True),
                source="service",
                response=response.get(
                    "message",
                    "Operation completed successfully."
                ),
                data=response.get("data"),
            )

        return self._build_response(
            success=True,
            source="service",
            response=str(response),
        )

    def handle_llm_response(self, response):
        """
        Formats responses coming from Gemini.
        """

        return self._build_response(
            success=True,
            source="gemini",
            response=response,
        )

    def handle_error(self, message):
        """
        Formats error responses.
        """

        return self._build_response(
            success=False,
            source="system",
            response=message,
        )