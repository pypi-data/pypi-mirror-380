from __future__ import annotations

import re
from typing import Any

import nh3

BASE_ALLOWED_TAGS = frozenset(
    {
        "p",
        "div",
        "span",
        "br",
        "hr",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "ul",
        "ol",
        "li",
        "dl",
        "dt",
        "dd",
        "strong",
        "b",
        "em",
        "i",
        "u",
        "s",
        "del",
        "ins",
        "mark",
        "small",
        "sub",
        "sup",
        "code",
        "pre",
        "kbd",
        "samp",
        "var",
        "abbr",
        "cite",
        "dfn",
        "time",
        "data",
        "a",
        "blockquote",
        "q",
    }
)

SEMANTIC_STRUCTURE_TAGS = frozenset(
    {
        "article",
        "section",
        "aside",
        "header",
        "footer",
        "main",
        "nav",
        "figure",
        "figcaption",
        "details",
        "summary",
    }
)

TABLE_TAGS = frozenset(
    {
        "table",
        "thead",
        "tbody",
        "tfoot",
        "tr",
        "td",
        "th",
        "caption",
        "colgroup",
        "col",
    }
)

MEDIA_TAGS = frozenset(
    {
        "img",
        "picture",
        "source",
        "audio",
        "video",
        "track",
        "canvas",
        "svg",
        "iframe",
    }
)

DEFAULT_NAVIGATION_CLASSES: frozenset[str] = frozenset(
    {
        "vector-header",
        "vector-main-menu",
        "vector-page-tools",
        "vector-toc",
        "mw-jump-link",
        "mw-navigation",
        "navbox",
        "navigation-box",
        "sidebar",
        "nav",
        "header",
        "footer",
        "menu",
        "breadcrumb",
        "topbar",
        "toolbar",
    }
)


def preprocess_html(
    html: str,
    *,
    remove_navigation: bool = True,
    remove_forms: bool = True,
    remove_scripts: bool = True,
    remove_styles: bool = True,
    remove_comments: bool = True,
    preserve_semantic_structure: bool = True,
    preserve_tables: bool = True,
    preserve_media: bool = True,
    custom_tags_to_remove: set[str] | None = None,
    custom_attributes_to_remove: set[str] | None = None,
    excluded_navigation_classes: set[str] | None = None,
    extra_navigation_classes: set[str] | None = None,
) -> str:
    if not html or not html.strip():  # pragma: no cover
        return html

    html = _remove_class_based_navigation(
        html,
        remove_navigation,
        excluded_navigation_classes,
        extra_navigation_classes,
    )

    nh3_config = _configure_cleaning_rules(
        remove_navigation=remove_navigation,
        remove_forms=remove_forms,
        remove_scripts=remove_scripts,
        remove_styles=remove_styles,
        remove_comments=remove_comments,
        preserve_semantic_structure=preserve_semantic_structure,
        preserve_tables=preserve_tables,
        preserve_media=preserve_media,
        custom_tags_to_remove=custom_tags_to_remove or set(),
        custom_attributes_to_remove=custom_attributes_to_remove or set(),
    )

    cleaned_html = nh3.clean(
        html,
        tags=nh3_config["tags"],
        attributes=nh3_config["attributes"],
        clean_content_tags=nh3_config["clean_content_tags"],
        strip_comments=nh3_config["strip_comments"],
    )

    cleaned_html = _remove_navigation_patterns(cleaned_html, remove_navigation)
    return _fix_whitespace_issues(cleaned_html)


def _configure_cleaning_rules(
    *,
    remove_navigation: bool,
    remove_forms: bool,
    remove_scripts: bool,
    remove_styles: bool,
    remove_comments: bool,
    preserve_semantic_structure: bool,
    preserve_tables: bool,
    preserve_media: bool,
    custom_tags_to_remove: set[str],
    custom_attributes_to_remove: set[str],
) -> dict[str, Any]:
    allowed_tags = set(BASE_ALLOWED_TAGS)

    if preserve_semantic_structure:
        allowed_tags.update(SEMANTIC_STRUCTURE_TAGS)

    if preserve_tables:
        allowed_tags.update(TABLE_TAGS)

    if preserve_media:
        allowed_tags.update(MEDIA_TAGS)

    allowed_tags -= custom_tags_to_remove

    clean_content_tags = set()

    if remove_navigation:
        clean_content_tags.update(
            {
                "nav",
                "menu",
                "menuitem",
                "header",
                "footer",
                "mw-jump-link",
                "vector-header",
                "vector-header-container",
                "vector-main-menu",
                "vector-page-tools",
                "vector-toc",
                "mw-navigation",
                "navbox",
                "navigation-box",
                "sidebar",
            }
        )

    if remove_forms:
        clean_content_tags.update(
            {
                "form",
                "input",
                "button",
                "select",
                "option",
                "optgroup",
                "textarea",
                "fieldset",
                "legend",
                "label",
                "output",
                "progress",
                "meter",
                "datalist",
            }
        )

    if remove_scripts:
        clean_content_tags.update({"script", "noscript"})

    if remove_styles:
        clean_content_tags.update({"style"})

    clean_content_tags.update(custom_tags_to_remove)

    allowed_tags -= clean_content_tags

    allowed_attributes = {
        "*": {"id", "class", "lang", "dir", "title"},
        "a": {"href"},
        "img": {"src", "alt", "width", "height"},
        "th": {"scope", "colspan", "rowspan"},
        "td": {"colspan", "rowspan"},
    }

    if custom_attributes_to_remove:
        for attrs in allowed_attributes.values():
            if isinstance(attrs, set):
                attrs.difference_update(custom_attributes_to_remove)

    return {
        "tags": allowed_tags,
        "attributes": allowed_attributes,
        "clean_content_tags": clean_content_tags,
        "strip_comments": remove_comments,
    }


def _remove_class_based_navigation(
    html: str,
    remove_navigation: bool,
    excluded_navigation_classes: set[str] | None,
    extra_navigation_classes: set[str] | None,
) -> str:
    if not remove_navigation:
        return html

    class_names = set(DEFAULT_NAVIGATION_CLASSES)

    if excluded_navigation_classes:
        class_names.difference_update(excluded_navigation_classes)

    if extra_navigation_classes:
        class_names.update(extra_navigation_classes)

    for class_name in class_names:
        class_pattern = rf'{re.escape(class_name)}[^"]*'

        block_pattern = rf'<(?P<tag>[^>\s]+)[^>]*class="[^"]*{class_pattern}[^"]*"[^>]*>.*?</(?P=tag)>'
        html = re.sub(block_pattern, "", html, flags=re.DOTALL | re.IGNORECASE)

        self_closing_pattern = rf'<[^>]*class="[^"]*{class_pattern}[^"]*"[^>]*/>'
        html = re.sub(self_closing_pattern, "", html, flags=re.IGNORECASE)

    return html


def _remove_navigation_patterns(html: str, remove_navigation: bool) -> str:
    if not remove_navigation:
        return html

    html = _remove_wikipedia_navigation_lists(html)

    patterns_to_remove = [
        r"\[Jump to content\]\(#[^)]*\)",
        r"\[Jump to content\]",
        r"Jump to content",
        r"Main menu.*?hide.*?Navigation",
        r"move to sidebar.*?hide",
        r"Home\s*[>»]\s*[^<]*[>»]",
        r"\[Skip to [^]]*\]",
        r"\[Skip [^]]*\]",
        r"<label[^>]*>.*?menu.*?</label>",
        r"<button[^>]*>.*?(menu|toggle|expand|collapse|show|hide).*?</button>",
        r"The Free Encyclopedia[^a-zA-Z]*",
        r"<img[^>]*wikipedia[^>]*>",
        r"\[Wikipedia\]\([^)]*\)",
        r'\[Search\]\([^)]*"Search[^)]*"\)',
        r"\[Add links\]\([^)]*\)",
        r"This is a good article\. Click here for more information\.",
        r"From Wikipedia, the free encyclopedia",
        r'<img[^>]*alt=[\'"][\'"][^>]*>',
        r'<img[^>]*src=[\'"][\'"][^>]*>',
        r"div\\>",
        r"</?\w+\\>",
        r"^Main menu\s*$",
        r"^Search\s*$",
        r"^History\s*$",
        r"^ProgrammingTranslatorReferencesExternal links\s*$",
    ]

    for pattern in patterns_to_remove:
        html = re.sub(pattern, "", html, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)

    return html


def _remove_wikipedia_navigation_lists(html: str) -> str:
    patterns = [
        r"Main menu\s*\n\n(-\s*\[.*?\]\(.*?\).*?\n){3,}",
        r"(-\s*\[[^\]]*\]\(/wiki/[^)]*\).*?\n){5,}",
    ]

    for pattern in patterns:
        html = re.sub(pattern, "", html, flags=re.DOTALL | re.MULTILINE)

    return html


def _fix_whitespace_issues(html: str) -> str:
    html = re.sub(r"[ \t]{2,}", " ", html)
    html = re.sub(r"\n\s*\n", "\n\n", html)

    return re.sub(r">\s*<", "><", html)


PRESETS: dict[str, dict[str, Any]] = {
    "minimal": {
        "remove_navigation": True,
        "remove_forms": True,
        "remove_scripts": True,
        "remove_styles": True,
        "remove_comments": True,
        "preserve_semantic_structure": False,
        "preserve_tables": True,
        "preserve_media": False,
    },
    "standard": {
        "remove_navigation": True,
        "remove_forms": True,
        "remove_scripts": True,
        "remove_styles": True,
        "remove_comments": True,
        "preserve_semantic_structure": True,
        "preserve_tables": True,
        "preserve_media": True,
    },
    "aggressive": {
        "remove_navigation": True,
        "remove_forms": True,
        "remove_scripts": True,
        "remove_styles": True,
        "remove_comments": True,
        "preserve_semantic_structure": False,
        "preserve_tables": True,
        "preserve_media": False,
        "custom_tags_to_remove": {"aside", "footer", "header"},
    },
}


def create_preprocessor(preset: str = "standard", **overrides: Any) -> dict[str, Any]:
    if preset not in PRESETS:
        msg = f"Unknown preset '{preset}'. Available presets: {list(PRESETS.keys())}"
        raise ValueError(msg)

    config: dict[str, Any] = dict(PRESETS[preset])
    config.update(overrides)

    return config
