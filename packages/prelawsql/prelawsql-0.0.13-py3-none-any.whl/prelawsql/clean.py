import re

xao = re.compile(r"\xa0")
"""Matches non-breaking space characters (U+00A0)."""

xad = re.compile(r"\xad")
"""Matches soft hyphen characters (U+00AD)."""

cap_start = re.compile(r"^\s+(?=[A-Z\*].+)", re.M)
"""Matches leading whitespace before lines that start with an uppercase letter or an asterisk."""

x_placeholder = r"\s*[x][\sx]+\n{2}"
xxx = "x x x"

xxx_bq_ideal = " " + xxx + "\n"
"""Canonical replacement form for placeholder blockquotes: `' x x x\\n'`."""

xxx_bq1 = re.compile(rf"(?<=^>){x_placeholder}", re.M)
"""Matches a placeholder 'x x x' line inside a single-level blockquote."""

xxx_bq2 = re.compile(rf"(?<=^>\s>){x_placeholder}", re.M)
"""Matches a placeholder 'x x x' line inside a nested two-level blockquote."""

xxx_bq3 = re.compile(rf"(?<=^>\s>\s>){x_placeholder}", re.M)
"""Matches a placeholder 'x x x' line inside a nested three-level blockquote."""

line_starts_with_space = re.compile(r"^\s+")
"""Matches lines that begin with one or more whitespace characters."""

two_spaces_then_line = re.compile(r"\s{2}\n")
"""Matches exactly two spaces immediately followed by a newline (used to normalize spacing)."""

start_bq = re.compile(r"\n{2}(>\n){2}", re.M)
"""Matches the start of a blockquote section introduced by two blank lines and two blockquote markers."""

end_bq = re.compile(r"(\n[>\s]+){2}\n{2}", re.M)
"""Matches the end of a blockquote section consisting of two blockquote lines followed by two blank lines."""

lone_bq = re.compile(r"\n{2}[>\s]+\n{2}", re.M)
"""Matches a lone blockquote marker surrounded by two blank lines before and after."""

sp_empty_bq = re.compile(r"(?<=^>)\n{2}(?=>)")
"""Matches an empty blockquote that ends with two line breaks and is followed by another blockquote."""

bq_line_next_line_not_bq = re.compile(
    r"""
            ^> # starts with blockquote marker
            .+$ # has content and terminates
            \n # new line
            ^(?!>|\s) # start of new line not another blockquote or a space
            """,
    re.M | re.X,
)
"""Matches a blockquote line followed by a non-blockquote line,
used to insert an extra newline so that the blockquote is visually separated."""


def clean_text(raw_content: str):
    """Clean and normalize case text by replacing special quotes and variants of 'vs.'.

    Args:
        raw_content (str): Input text containing raw case content.

    Returns:
        str: Cleaned text with normalized quotation marks and 'v.' forms.

    Examples:
        >>> clean_text("“Hello” vs. World")
        '"Hello" v. World'
        >>> clean_text("‘A’ *vs* B")
        "'A' v. B"
    """
    for old, new in [
        ("`", "'"),
        ("“", '"'),
        ("”", '"'),
        ("‘", "'"),
        ("’", "'"),
        ("\u2018", "'"),
        ("\u2019", "'"),
        ("\u0060", "'"),
        ("*vs*.", "v."),
        ("*vs*", "v."),
        ("*v.*", "v."),
        ("*v*.", "v."),
        ("_vs_.", "v."),
        ("_vs_", "v."),
        ("_v._", "v."),
        ("_v_.", "v."),
        (" vs. ", " v. "),
        (", v. ", " v. "),
        (", vs. ", " v. "),
        ("'' ", '" '),
        (" ''", ' "'),
    ]:
        raw_content = raw_content.replace(old, new)
    return raw_content


italicized_case = re.compile(
    r"""
    \*{3} # marker
    (?P<casename>
        (.+?)
        (\svs?\.\s)
        (.+?)
    )
    \*{3} # marker
    """,
    re.X,
)


def add_extra_line(text: str):
    """Add an extra line break after blockquote lines followed by normal text.

    Recursively scans the text and inserts extra `\\n` where needed.

    Args:
        text (str): Input text with blockquotes.

    Returns:
        str: Text with extra line breaks added.

    Examples:
        >>> sample = "> Quoted line\\nNext line"
        >>> print(add_extra_line(sample))
        > Quoted line
        <BLANKLINE>
        Next line
    """
    while True:
        if match := bq_line_next_line_not_bq.search(text):
            line = match.group()
            text = text.replace(line, line + "\n")
        else:
            break
    return text


def format_text(text: str):
    """Format text by normalizing spacing, quotes, and blockquote handling.

    Args:
        text (str): Raw input text.

    Returns:
        str: Formatted text.

    Examples:
        >>> format_text("  Hello  \\nWorld")
        'Hello\\n\\nWorld'
        >>> format_text("x x x\\n")
        'x x x\\n'
    """
    text = two_spaces_then_line.sub("\n\n", text)
    text = line_starts_with_space.sub("", text)
    text = cap_start.sub("\n", text)
    text = text.replace("`", "'h")
    text = xao.sub(" ", text)
    text = xad.sub("", text)
    text = xxx_bq1.sub(xxx_bq_ideal, text)
    text = xxx_bq2.sub(xxx_bq_ideal, text)
    text = xxx_bq3.sub(xxx_bq_ideal, text)
    text = start_bq.sub("\n\n", text)
    text = end_bq.sub("\n\n", text)
    text = lone_bq.sub("\n\n", text)
    text = sp_empty_bq.sub("\n", text)
    text = add_extra_line(text)
    return text


def is_text_possible(text: str, max_len: int = 30) -> bool:
    """Check if text is non-empty and within the maximum length.

    Args:
        text (str): The text to check.
        max_len (int, optional): Maximum allowed length. Defaults to 30.

    Returns:
        bool: True if text is non-empty and within length, False otherwise.

    Examples:
        >>> is_text_possible("Hello")
        True
        >>> is_text_possible("   ")
        False
        >>> is_text_possible("This sentence is definitely longer than thirty characters.")
        False
    """
    if text := text.strip():  # not empty string
        if len(text) <= max_len:
            return True
    return False
