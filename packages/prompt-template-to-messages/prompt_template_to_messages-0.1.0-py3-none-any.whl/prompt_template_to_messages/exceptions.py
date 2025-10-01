"""Custom exceptions for prompt_template_to_messages."""


class PromptTemplateToMessagesError(RuntimeError):
    """Raised when a prompt template cannot be compiled into messages."""
