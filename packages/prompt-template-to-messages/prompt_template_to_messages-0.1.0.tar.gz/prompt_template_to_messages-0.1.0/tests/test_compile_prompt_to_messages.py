from __future__ import annotations

from prompt_template_to_messages import compile_prompt_to_messages


def test_simple_text_scope() -> None:
    result = compile_prompt_to_messages("Hello {{ name }}!", scope={"name": "World"})
    assert result == [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Hello World!"},
            ],
        }
    ]


def test_image_only_message_with_scope_variable() -> None:
    template = """{% call _pt2m_message('user') -%}\n{{ _pt2m_resolve_image(hero_image, detail='high') }}\n{%- endcall %}"""
    scope = {"hero_image": "https://cdn.example/hero.png"}

    result = compile_prompt_to_messages(template, scope=scope)

    assert result == [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cdn.example/hero.png",
                        "detail": "high",
                    },
                }
            ],
        }
    ]


def test_text_image_then_text() -> None:
    template = "Hello {{ _pt2m_resolve_image('cat.png', alt='A cat') }} there"
    result = compile_prompt_to_messages(template)
    assert result == [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Hello "},
                {
                    "type": "image_url",
                    "image_url": {"url": "cat.png"},
                },
                {"type": "text", "text": " there"},
            ],
        }
    ]


def test_custom_image_translator() -> None:
    template = "{{ _pt2m_resolve_image('dog.png') }}"

    def image_to_url(tag, context):
        return {
            "type": "image_url",
            "image_url": {
                "url": f"https://cdn.example/{tag.attrs['ref']}",
                "detail": "high",
            },
        }

    result = compile_prompt_to_messages(template, translators=[("image", image_to_url)])
    assert result == [
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://cdn.example/dog.png",
                        "detail": "high",
                    },
                }
            ],
        }
    ]


def test_complex_role_logic_with_jinja_call_blocks() -> None:
    template = """
{% call _pt2m_message('system') -%}
You are a helpful assistant.
{%- endcall %}
{% call _pt2m_message('user') -%}
Describe this image: {{ _pt2m_resolve_image(item.ref) }}
{%- endcall %}
"""

    scope = {"item": {"ref": "scene.png"}}
    result = compile_prompt_to_messages(template, scope=scope)
    assert result == [
        {
            "role": "system",
            "content": [
                {"type": "text", "text": "You are a helpful assistant."},
            ],
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image: "},
                {
                    "type": "image_url",
                    "image_url": {"url": "scene.png"},
                },
            ],
        },
    ]


def test_custom_multi_modal_translator_combined_scope() -> None:
    template = """{% call _pt2m_message('assistant') %}
Here is the asset: {{ _pt2m_resolve_image(asset_ref, detail='medium', caption=asset_caption) }}
Here is the custom asset: {{ resolve_multi_modal(asset_ref, detail='medium', caption=asset_caption) }}
{% endcall %}"""

    scope = {
        "asset_ref": "banner-42",
        "asset_caption": "Promo banner",
        "resolve_multi_modal": lambda ref, detail, caption: (
            f'<multi-modal ref="{ref}" detail="{detail}" caption="{caption}" />'
        ),
    }

    def multi_modal_translator(tag, context):
        return {
            "type": "multi-modal",
            "multi_modal": {
                "ref": tag.attrs.get("ref"),
                "detail": tag.attrs.get("detail"),
                "caption": tag.attrs.get("caption"),
            },
        }

    result = compile_prompt_to_messages(
        template,
        scope=scope,
        translators=[("multi-modal", multi_modal_translator)],
    )
    print(result)
    assert result == [
        {
            "role": "assistant",
            "content": [
                {"type": "text", "text": "\nHere is the asset: "},
                {"type": "image_url", "image_url": {"url": "banner-42", "detail": "medium"}},
                {"type": "text", "text": "\nHere is the custom asset: "},
                {
                    "type": "multi-modal",
                    "multi_modal": {
                        "ref": "banner-42",
                        "detail": "medium",
                        "caption": "Promo banner",
                    },
                },
            ],
        }
    ]
