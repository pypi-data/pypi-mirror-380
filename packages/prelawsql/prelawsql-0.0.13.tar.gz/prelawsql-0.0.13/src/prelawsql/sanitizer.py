from html_sanitizer.sanitizer import (
    Sanitizer,
    bold_span_to_strong,
    italic_span_to_em,
    sanitize_href,
    tag_replacer,
    target_blank_noopener,
)

decision_sanitizer = Sanitizer(
    {
        "tags": {
            "a",
            "h1",
            "h2",
            "h3",
            "strong",
            "center",
            "em",
            "p",
            "ul",
            "ol",
            "li",
            "br",
            "blockquote",
            "sub",
            "sup",
            "hr",
            "table",
            "tbody",
            "td",
            "tr",
        },
        "attributes": {
            "p": ("align",),
            "a": ("href", "name", "target", "title", "id", "rel"),
            "sup": ("id",),
        },
        "empty": {"hr", "a", "br"},
        "separate": {"a", "p", "li", "td", "tr"},
        "whitespace": {"br"},
        "keep_typographic_whitespace": True,
        "add_nofollow": False,
        "autolink": False,
        "sanitize_href": sanitize_href,
        "element_preprocessors": [
            bold_span_to_strong,
            italic_span_to_em,
            tag_replacer("b", "strong"),
            tag_replacer("i", "em"),
            tag_replacer("form", "p"),
            target_blank_noopener,
        ],
        "element_postprocessors": [],
        "is_mergeable": lambda e1, e2: True,
    }
)
"""Configured sanitizer for cleaning decision documents.

- Allows headings, blockquotes, tables, and inline tags like `<em>` and `<strong>`.
- Preserves typographic whitespace (e.g., non-breaking spaces).
- Converts `<b>` → `<strong>`, `<i>` → `<em>`, and `<form>` → `<p>`.
- Ensures `<a>` tags only allow safe attributes.
"""


statute_sanitizer = Sanitizer(
    {
        "tags": {
            "h2",
            "h3",
            "em",
            "center",
            "p",
            "ul",
            "ol",
            "li",
            "br",
            "blockquote",
            "hr",
            "table",
            "tbody",
            "td",
            "tr",
        },
        "attributes": {"p": ("id", "data-type")},
        "empty": {"br", "hr"},
        "separate": {"p", "li"},
        "whitespace": {"br"},
        "keep_typographic_whitespace": False,
        "add_nofollow": False,
        "autolink": False,
        "sanitize_href": sanitize_href,
        "element_preprocessors": [
            italic_span_to_em,
            tag_replacer("i", "em"),
            tag_replacer("span", "p"),
            tag_replacer("font", "p"),
            target_blank_noopener,
        ],
        "element_postprocessors": [],
        "is_mergeable": lambda e1, e2: True,
    }
)
"""Configured sanitizer for cleaning statutes and legal codes.

- Allows structural tags (paragraphs, lists, tables) and inline emphasis.
- Normalizes `<i>` → `<em>`, `<span>` → `<p>`, `<font>` → `<p>`.
- Does not preserve typographic whitespace.
- Ensures links are sanitized with safe attributes.
"""
