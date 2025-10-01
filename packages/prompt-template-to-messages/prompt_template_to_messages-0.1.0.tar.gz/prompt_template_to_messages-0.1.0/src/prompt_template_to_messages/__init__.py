"""Public API for prompt_template_to_messages."""

from __future__ import annotations

from .constants import PT2M_PREFIX
from .exceptions import PromptTemplateToMessagesError
from .parsing import compile_prompt_to_messages
from .scope import DEFAULT_SCOPE, scope_pt2m_embed, scope_pt2m_message, scope_pt2m_resolve_image
from .translators import (
    BaseTranslator,
    FunctionTranslator,
    PlainTextTranslator,
    PT2MImageTranslator,
    PT2MMessageTranslator,
    TranslationContext,
    prepare_translators,
)

__all__ = [
    "PT2M_PREFIX",
    "PromptTemplateToMessagesError",
    "compile_prompt_to_messages",
    "DEFAULT_SCOPE",
    "scope_pt2m_message",
    "scope_pt2m_resolve_image",
    "scope_pt2m_embed",
    "BaseTranslator",
    "FunctionTranslator",
    "PlainTextTranslator",
    "PT2MImageTranslator",
    "PT2MMessageTranslator",
    "TranslationContext",
    "prepare_translators",
]
