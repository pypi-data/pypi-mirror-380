import re
from io import StringIO

from markdown import Markdown, markdown  # type: ignore
from markupsafe import Markup

footnote_pattern = re.compile(r"\[\^\d+\]")
"""Matches footnotes of the form [^1], [^23], etc."""

two_or_more_spaces = re.compile(r"\s{2,}")
"""Matches two or more spaces (used for cleanup)"""


def mdfy(text: str, extensions: list[str] = ["footnotes", "tables"]) -> Markup:
    """Convert Markdown to safe HTML.

    Thin wrapper around markup from markdown based on provided extensions converts
    markdown content to html equivalent.

    Args:
        text: Markdown text input.
        extensions: Optional list of Markdown extensions to enable.
            Defaults to ``["footnotes", "tables"]``.

    Returns:
        A Markup-safe HTML string.

    Example:
        >>> mdfy("**bold**")
        Markup('<p><strong>bold</strong></p>')
    """
    return Markup(markdown(text, extensions=extensions))


def unmark_element(element, stream=None):
    """Recursively extract plain text from an ElementTree element.

    Args:
        element: An element from Markdown's internal XML/HTML tree.
        stream: Optional StringIO buffer for accumulating text.

    Returns:
        A string containing concatenated text without Markdown tags.
    """
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


Markdown.output_formats["plain"] = unmark_element  # type: ignore
"""Monkey-patching Markdown to allow plain-text output"""

__md = Markdown(output_format="plain")  # type: ignore
__md.stripTopLevelTags = False  # type: ignore


def clear_markdown(value: str) -> str:
    """Remove Markdown syntax and footnotes, leaving plain text.

    - Converts Markdown into a text-only format.
    - Removes footnotes like ``[^1]``.
    - Collapses multiple spaces into one.
    - Uses part of the code described in https://stackoverflow.com/a/54923798/9081369

    Args:
        value: A Markdown string.

    Returns:
        Plain text string without Markdown syntax.

    Example:
        >>> clear_markdown("This is **bold** and [^1]")
        'This is bold and '
    """
    unmarked = __md.convert(value)
    result = footnote_pattern.sub("", unmarked)
    result = two_or_more_spaces.sub(" ", result)
    return result
