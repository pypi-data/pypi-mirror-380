"""Default scope helpers for template rendering."""

from __future__ import annotations

from typing import Any, Callable, Dict

from .constants import PT2M_PREFIX


def _render_pt2m_tag(tag_name: str, attrs: Dict[str, Any], content: str | None) -> str:
    attribute_pairs = " ".join(
        f"{key}='{value}'" for key, value in attrs.items() if value is not None
    )
    if content is None:
        return f"<{tag_name}{(' ' + attribute_pairs) if attribute_pairs else ''} />"
    return f"<{tag_name}{(' ' + attribute_pairs) if attribute_pairs else ''}>{content}</{tag_name}>"


def scope_pt2m_message(role: str, content: str | None = None, *, caller=None, **attrs: Any) -> str:
    if caller is not None and content is None:
        content = caller()
    if content is None:
        content = ""
    full_attrs = {"role": role, **attrs}
    return _render_pt2m_tag(f"{PT2M_PREFIX}message", full_attrs, content)


def scope_pt2m_resolve_image(image_ref: str, **attrs: Any) -> str:
    tag_attrs = {"ref": image_ref, **attrs}
    return _render_pt2m_tag(f"{PT2M_PREFIX}image", tag_attrs, None)


def scope_pt2m_embed(name: str, content: str | None = None, **attrs: Any) -> str:
    tag_name = f"{PT2M_PREFIX}{name}"
    return _render_pt2m_tag(tag_name, attrs, content)


DEFAULT_SCOPE: Dict[str, Callable[..., str]] = {
    "_pt2m_message": scope_pt2m_message,
    "_pt2m_resolve_image": scope_pt2m_resolve_image,
    "_pt2m_embed": scope_pt2m_embed,
}
