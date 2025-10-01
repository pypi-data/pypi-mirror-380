prompt-template-to-messages
===========================

Turn richly annotated Jinja2 prompts into OpenAI-compatible message payloads without giving up the ergonomics of plain text version control.

Why this project exists
-----------------------
Most prompt repositories still manage prompts as plain text. Diffing, reviewing, and versioning become easy, but multimodal prompts are hard to author and ship. `prompt-template-to-messages` embraces templates: you keep a single text file that mixes roles, function calls, and rich metadata via helper functions, which render into HTML-like tags prefixed with `pt2m-`. Under the hood, we combine Jinja2 for rendering dynamic content and BeautifulSoup-powered parsing to compile the result into the structured `messages` array required by OpenAI-compatible APIs. Welcome to the template era.

Key features
------------
- Author prompts once and render them as OpenAI `messages`.
- Keep prompts in Git-friendly text files while supporting multimodal content.
- Compose translators to customize how tags produce message fragments.
- Strict rendering: Jinja2 runs with `StrictUndefined` so missing variables fail fast.

Install
-------
```
pip install prompt-template-to-messages
```

Quick start
-----------
1. Create a template file `welcome.pt2m.jinja`:

   ```
   {% set user_name = user_name or "friend" %}
   {% call _pt2m_message('system') %}
   You are a concise onboarding assistant.
   {% endcall %}
   {% call _pt2m_message('user') %}
   Hello, {{ user_name }}!
   {{ _pt2m_resolve_image(intro_image_url, alt='Welcome illustration') }}
   {% endcall %}
   ```

2. Render it with Python:

   ```python
   from prompt_template_to_messages import compile_prompt_to_messages

   template_text = open("welcome.pt2m.jinja", "r", encoding="utf-8").read()
   messages = compile_prompt_to_messages(
       template_text,
       scope={"user_name": "Ada", "intro_image_url": "https://example.com/welcome.png"},
   )
   ```

3. Send `messages` to your favorite chat completion client.

Examples
--------
### Image-only broadcast
Use a scope variable to supply an image URL and render a message that contains only `image_url` content:

template
```
{% call _pt2m_message('user') -%}
{{ _pt2m_resolve_image(hero_image, detail='high') }}
{%- endcall %}

```
scope
```python
scope = {"hero_image": "https://cdn.example/hero.png"}
messages = compile_prompt_to_messages(template, scope=scope)
# -> [{'role': 'user', 'content': [{'type': 'image_url', 'image_url': {'url': 'https://cdn.example/hero.png', 'detail': 'high'}}]}]
```

### Custom translator with plain tags
Plain HTML-like tags that appear in the rendered template can be whitelisted by registering translators. The example below mixes `_pt2m_` helpers with a scope function that emits `<multi-modal>` tags:

```python
from prompt_template_to_messages import compile_prompt_to_messages

template = """{% call _pt2m_message('assistant') -%}Gallery incoming: {{ render_multi_modal(featured) }}{%- endcall %}"""

def render_multi_modal(asset):
    return f'<multi-modal ref="{asset["ref"]}" caption="{asset["caption"]}" detail="{asset["detail"]}" />'

def multi_modal_translator(tag, context):
    return {
        "type": "multi-modal",
        "multi_modal": {
            "ref": tag.attrs.get("ref"),
            "caption": tag.attrs.get("caption"),
            "detail": tag.attrs.get("detail"),
        },
    }

scope = {"featured": {"ref": "hero.png", "caption": "Hero", "detail": "medium"}, "render_multi_modal": render_multi_modal}
messages = compile_prompt_to_messages(template, scope=scope, translators=[("multi-modal", multi_modal_translator)])
```

Any translator added through `translators=[...]` is treated as part of the whitelist, so its tag will be parsed even without the `pt2m-` prefix.

CLI usage
---------
This package ships a CLI named `ptm`.

```
ptm render TEMPLATE_PATH --scope scope.json --output messages.json
```

`--scope` accepts a JSON file, and `--output` writes the compiled messages. Run `ptm --help` for all options.

Formatting and release workflow
--------------------------------
The Makefile encodes the recommended workflow:
- `make format` runs `ruff format` on `src/` and `tests/`.
- `make git-push` formats your code before pushing.
- `make release` formats, tests, lints, type-checks, builds, and then tags the release.

Contributing
------------
1. Clone the repo and run `make install-dev`.
2. Use `make format`, `make lint`, and `make test` while iterating.
3. Before pushing, run `make git-push` to enforce formatting.
4. For publishing, follow `make release` and `make upload`.

License
-------
MIT Licensed. See `LICENSE` for details.

