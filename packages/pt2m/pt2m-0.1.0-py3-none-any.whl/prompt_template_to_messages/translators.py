"""Translators convert parsed fragments into message structures."""

from __future__ import annotations

from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    MutableMapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)

from .exceptions import PromptTemplateToMessagesError
from .models import Fragment, PT2MTag

MessageContent = Dict[str, Any]
Message = Dict[str, Any]
SingleTranslatorItem = Union[Message, MessageContent]
TranslatorOutput = Union[SingleTranslatorItem, Sequence[SingleTranslatorItem]]
TranslatorFunc = Callable[[PT2MTag, "TranslationContext"], TranslatorOutput]


class BaseTranslator:
    priority: int = 0
    tags: Tuple[str, ...] = ()

    def matches(self, fragment: Fragment) -> bool:
        return isinstance(fragment, PT2MTag) and fragment.name in self.tags

    def translate(
        self, fragment: Fragment, context: "TranslationContext"
    ) -> Optional[TranslatorOutput]:
        raise NotImplementedError


class PlainTextTranslator(BaseTranslator):
    priority = -100
    tags: Tuple[str, ...] = ()

    def matches(self, fragment: Fragment) -> bool:  # type: ignore[override]
        return isinstance(fragment, str)

    def translate(
        self, fragment: Fragment, context: "TranslationContext"
    ) -> Optional[TranslatorOutput]:  # type: ignore[override]
        if not isinstance(fragment, str):
            return None
        if not fragment.strip():
            return None
        return {"type": "text", "text": fragment}


class PT2MMessageTranslator(BaseTranslator):
    priority = 100
    tags = ("message",)

    def translate(
        self, fragment: Fragment, context: "TranslationContext"
    ) -> Optional[TranslatorOutput]:
        if not isinstance(fragment, PT2MTag):
            return None
        role = fragment.attrs.get("role")
        if not role:
            raise PromptTemplateToMessagesError("<pt2m-message> tag requires a 'role' attribute")
        content_items = context.translate_children(fragment.children)
        return {"role": role, "content": content_items}


class PT2MImageTranslator(BaseTranslator):
    priority = 10
    tags = ("image",)

    def translate(
        self, fragment: Fragment, context: "TranslationContext"
    ) -> Optional[TranslatorOutput]:
        if not isinstance(fragment, PT2MTag):
            return None
        url = fragment.attrs.get("url") or fragment.attrs.get("ref")
        if not url:
            raise PromptTemplateToMessagesError(
                "<pt2m-image> tag requires a 'ref' or 'url' attribute"
            )
        payload: Dict[str, Any] = {"url": url}
        if "detail" in fragment.attrs:
            payload["detail"] = fragment.attrs["detail"]
        result: Dict[str, Any] = {"type": "image_url", "image_url": payload}
        # metadata = {
        #     key: value
        #     for key, value in fragment.attrs.items()
        #     if key not in {"ref", "url", "detail"}
        # }
        # if metadata:
        #     result["metadata"] = metadata
        return result


class FunctionTranslator(BaseTranslator):
    def __init__(self, tag: str, func: TranslatorFunc, priority: int = 0):
        self.tags = (tag,)
        self._func = func
        self.priority = priority

    def translate(
        self, fragment: Fragment, context: "TranslationContext"
    ) -> Optional[TranslatorOutput]:
        if not isinstance(fragment, PT2MTag):
            return None
        return self._func(fragment, context)


class TranslationContext:
    def __init__(self, translators: Sequence[BaseTranslator], default_role: str = "user") -> None:
        self.translators = sorted(translators, key=lambda t: t.priority, reverse=True)
        self.default_role = default_role

    def find_translator(self, fragment: Fragment) -> Optional[BaseTranslator]:
        for translator in self.translators:
            if translator.matches(fragment):
                return translator
        return None

    def translate_fragment(self, fragment: Fragment) -> List[SingleTranslatorItem]:
        translator = self.find_translator(fragment)
        if translator is None:
            raise PromptTemplateToMessagesError(
                f"No translator registered for fragment: {fragment!r}"
            )
        result = translator.translate(fragment, self)
        return _normalize_output(result)

    def translate_children(self, fragments: Sequence[Fragment]) -> List[MessageContent]:
        items: List[MessageContent] = []
        for fragment in fragments:
            translated_items = self.translate_fragment(fragment)
            for item in translated_items:
                if _is_message(item):
                    raise PromptTemplateToMessagesError("Nested PT2M messages are not supported")
                _append_content(items, item)
        return items

    def translate_top_level(self, fragments: Sequence[Fragment]) -> List[Message]:
        messages: List[Message] = []
        current: Optional[Message] = None

        def ensure_current() -> Message:
            nonlocal current
            if current is None:
                current = {"role": self.default_role, "content": []}
                messages.append(current)
            return current

        for fragment in fragments:
            translated_items = self.translate_fragment(fragment)
            for item in translated_items:
                if _is_message(item):
                    current = None
                    messages.append(item)  # type: ignore[arg-type]
                else:
                    ensure_current()
                    _append_content(ensure_current()["content"], item)  # type: ignore[index]

        cleaned_messages: List[Message] = []
        for message in messages:
            if _is_message(message) and message["content"]:
                cleaned_messages.append(message)
        return cleaned_messages


def _normalize_output(result: Optional[TranslatorOutput]) -> List[SingleTranslatorItem]:
    if result is None:
        return []
    if isinstance(result, Sequence) and not isinstance(result, (str, bytes, bytearray)):
        return list(cast(Sequence[SingleTranslatorItem], result))
    return [cast(SingleTranslatorItem, result)]


def _is_message(item: SingleTranslatorItem) -> bool:
    return isinstance(item, MutableMapping) and "role" in item and "content" in item


def _append_content(container: List[MessageContent], item: SingleTranslatorItem) -> None:
    if not isinstance(item, MutableMapping):
        raise PromptTemplateToMessagesError(
            f"Invalid message content produced by translator: {item!r}"
        )
    if _is_message(item):
        raise PromptTemplateToMessagesError("Unexpected nested message during content assembly")
    if item.get("type") == "text" and container:
        last = container[-1]
        if isinstance(last, MutableMapping) and last.get("type") == "text":
            last["text"] = f"{last.get('text', '')}{item.get('text', '')}"
            return
    container.append(dict(item))


DEFAULT_TRANSLATORS: List[BaseTranslator] = [
    PT2MMessageTranslator(),
    PT2MImageTranslator(),
    PlainTextTranslator(),
]


def prepare_translators(custom: Optional[Iterable[Any]]) -> List[BaseTranslator]:
    translators = list(DEFAULT_TRANSLATORS)
    if not custom:
        return translators
    for translator in custom:
        normalized = _normalize_translator(translator)
        if normalized.tags:
            translators = [t for t in translators if not set(t.tags) & set(normalized.tags)]
        translators.append(normalized)
    translators.sort(key=lambda t: t.priority, reverse=True)
    return translators


def _normalize_translator(translator: Any) -> BaseTranslator:
    if isinstance(translator, BaseTranslator):
        return translator
    if isinstance(translator, tuple) and len(translator) == 2:
        tag, func = translator
        if not isinstance(tag, str) or not callable(func):
            raise TypeError("Translator tuple must be (str, callable)")
        typed_func = cast(TranslatorFunc, func)
        return FunctionTranslator(tag, typed_func)
    if callable(translator) and hasattr(translator, "tags"):
        return cast(BaseTranslator, translator)
    raise TypeError("Unsupported translator specification")
