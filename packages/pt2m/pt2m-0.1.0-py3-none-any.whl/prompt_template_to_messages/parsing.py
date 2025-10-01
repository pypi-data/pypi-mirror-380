"""Rendering and parsing logic converting templates into fragments."""

from __future__ import annotations

from html.parser import HTMLParser
from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Tuple

from jinja2 import Environment, StrictUndefined, TemplateError

from .constants import PT2M_PREFIX
from .exceptions import PromptTemplateToMessagesError
from .models import Fragment, PT2MTag
from .scope import DEFAULT_SCOPE
from .translators import TranslationContext, prepare_translators


def _create_environment() -> Environment:
    return Environment(undefined=StrictUndefined, autoescape=False)


def _render_template(template: str, scope: Mapping[str, Any]) -> str:
    env = _create_environment()
    try:
        jinja_template = env.from_string(template)
        return jinja_template.render(scope)
    except TemplateError as exc:
        raise PromptTemplateToMessagesError(f"Failed to render template: {exc}") from exc


class _PT2MHTMLParser(HTMLParser):
    def __init__(self, allowed_plain_tags: Optional[Set[str]] = None) -> None:
        super().__init__(convert_charrefs=True)
        self._fragments_stack: List[List[Fragment]] = [[]]
        self._tag_stack: List[Tuple[str, Dict[str, Any]]] = []
        self._plain_tags: Set[str] = allowed_plain_tags or set()

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attrs_dict = {key: value for key, value in attrs if key and value is not None}
        if tag.startswith(PT2M_PREFIX):
            self._tag_stack.append((tag[len(PT2M_PREFIX) :], attrs_dict))
            self._fragments_stack.append([])
            return
        if tag in self._plain_tags:
            self._tag_stack.append((tag, attrs_dict))
            self._fragments_stack.append([])
            return
        text = self.get_starttag_text()
        if text:
            self._append_text(text)

    def handle_endtag(self, tag: str) -> None:
        if not self._tag_stack:
            self._append_text(f"</{tag}>")
            return
        if tag.startswith(PT2M_PREFIX):
            expected_name = tag[len(PT2M_PREFIX) :]
        elif tag in self._plain_tags:
            expected_name = tag
        else:
            self._append_text(f"</{tag}>")
            return
        tag_name, attrs = self._tag_stack.pop()
        if tag_name != expected_name:
            self._append_text(f"</{tag}>")
            return
        children = tuple(self._fragments_stack.pop())
        self._fragments_stack[-1].append(PT2MTag(tag_name, attrs, children))

    def handle_startendtag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attrs_dict = {key: value for key, value in attrs if key and value is not None}
        if tag.startswith(PT2M_PREFIX):
            self._fragments_stack[-1].append(PT2MTag(tag[len(PT2M_PREFIX) :], attrs_dict, tuple()))
            return
        if tag in self._plain_tags:
            self._fragments_stack[-1].append(PT2MTag(tag, attrs_dict, tuple()))
            return
        text = self.get_starttag_text()
        if text:
            self._append_text(text)

    def handle_data(self, data: str) -> None:
        self._append_text(data)

    def handle_entityref(self, name: str) -> None:
        self._append_text(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self._append_text(f"&#{name};")

    def handle_comment(self, data: str) -> None:  # pragma: no cover
        self._append_text(f"<!--{data}-->")

    def handle_decl(self, decl: str) -> None:  # pragma: no cover
        self._append_text(f"<!{decl}>")

    def handle_pi(self, data: str) -> None:  # pragma: no cover
        self._append_text(f"<?{data}>")

    def close(self) -> None:
        super().close()
        while self._tag_stack:
            tag_name, attrs = self._tag_stack.pop()
            children = tuple(self._fragments_stack.pop())
            self._fragments_stack[-1].append(PT2MTag(tag_name, attrs, children))

    def _append_text(self, text: Optional[str]) -> None:
        if not text:
            return
        fragments = self._fragments_stack[-1]
        if fragments and isinstance(fragments[-1], str):
            fragments[-1] += text
        else:
            fragments.append(text)

    def get_fragments(self) -> List[Fragment]:
        fragments: List[Fragment] = []
        for fragment in self._fragments_stack[0]:
            if isinstance(fragment, str) and not fragment.strip():
                continue
            fragments.append(fragment)
        return fragments


def parse_rendered_output(
    rendered: str, allowed_plain_tags: Optional[Set[str]] = None
) -> List[Fragment]:
    if not rendered:
        return []
    parser = _PT2MHTMLParser(allowed_plain_tags=allowed_plain_tags)
    parser.feed(rendered)
    parser.close()
    return parser.get_fragments()


def compile_prompt_to_messages(
    prompt_text: str,
    scope: Optional[Mapping[str, Any]] = None,
    translators: Optional[Iterable[Any]] = None,
    default_role: str = "user",
) -> List[Dict[str, Any]]:
    if not isinstance(prompt_text, str):
        raise TypeError("prompt_text must be a string")

    combined_scope: Dict[str, Any] = dict(DEFAULT_SCOPE)
    if scope:
        combined_scope.update(scope)

    rendered = _render_template(prompt_text, combined_scope)
    translator_objects = prepare_translators(translators)
    allowed_plain_tags: Set[str] = set()
    for translator in translator_objects:
        for tag in translator.tags:
            if tag and not tag.startswith(PT2M_PREFIX):
                allowed_plain_tags.add(tag)
    fragments = parse_rendered_output(rendered, allowed_plain_tags=allowed_plain_tags)
    context = TranslationContext(translator_objects, default_role=default_role)
    return context.translate_top_level(fragments)
