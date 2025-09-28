import re

from bs4 import BeautifulSoup
from citation_title import cite_title
from citation_utils import Citation

from .clean import is_text_possible


def is_opinion_label(text: str) -> bool:
    """Check if a string appears to be a court opinion label.

    A valid opinion label must be non-empty, under 50 characters, and
    contain at least one of: "opinion", "dissent", "separate", "concur".

    Args:
        text (str): Input label text.

    Returns:
        bool: True if text is a likely opinion label, otherwise False.

    Examples:
        >>> is_opinion_label("Concurring Opinion")
        True
        >>> is_opinion_label("Random Heading")
        False
    """
    if not is_text_possible(text, max_len=50):
        return False

    candidate = text.lower()
    for marker in ("opinion", "dissent", "separate", "concur"):
        if marker in candidate:
            return True
    return False


ENBANC_PATTERN = re.compile(r"banc", re.I)
"""Regex that matches the phrase 'En Banc' in a case heading, case-insensitive."""

DIVISION_PATTERN = re.compile(r"division", re.I)
"""Regex that matches the phrase 'Division' in a case heading, case-insensitive."""


def spaced(z: str):
    return re.compile("\\s*".join(i for i in z), re.I | re.X)


DECISION_PATTERN = spaced("decision")
"""Regex that matches the word 'Decision' even if spaced out letter by letter
(e.g., 'D E C I S I O N')."""

RESOLUTION_PATTERN = spaced("resolution")
"""Regex that matches the word 'Resolution' even if spaced out letter by letter
(e.g., 'R E S O L U T I O N')."""


def clean_composition(soup: BeautifulSoup) -> str | None:
    """Extract the court composition (En Banc or Division) from an <h2> heading.

    Args:
        soup (BeautifulSoup): Parsed HTML document.

    Returns:
        str | None: "En Banc", "Division", or None if not found.

    Examples:
        >>> soup = BeautifulSoup("<h2>Supreme Court En Banc</h2>", "lxml")
        >>> clean_composition(soup)
        'En Banc'
    """
    targets = soup("h2")
    if not targets:
        return None

    text = targets[0].text.title()

    if ENBANC_PATTERN.search(text):
        return "En Banc"
    elif DIVISION_PATTERN.search(text):
        return "Division"
    return None


def clean_date(soup: BeautifulSoup) -> str | None:
    """Extract a decision date from an <h2> heading.

    Args:
        soup (BeautifulSoup): Parsed HTML document.

    Returns:
        str | None: Cleaned date string, or None if not found.

    Note:
        This function is currently a placeholder for date extraction logic.
    """
    targets = soup("h2")
    if not targets:
        return None


def clean_category(soup: BeautifulSoup) -> str | None:
    """Extract the category (Decision or Resolution) from an <h3> heading.

    Args:
        soup (BeautifulSoup): Parsed HTML document.

    Returns:
        str | None: "Decision", "Resolution", or None if unrecognized.

    Examples:
        >>> soup = BeautifulSoup("<h3>Decision</h3>", "lxml")
        >>> clean_category(soup)
        'Decision'
    """
    targets = soup("h3")
    if not targets:
        return None

    candidates = targets[0].find_all(string=True, recursive=False)
    if not candidates:
        return None

    text = candidates[-1].strip()

    if DECISION_PATTERN.search(text):
        return "Decision"

    elif RESOLUTION_PATTERN.search(text):
        return "Resolution"

    # Some cases are improperly formatted / spelled or use different phrases
    # "Ecision", "Kapasyahan" - 29848, "Opinion" - 36567, or lack label entirely - 60046
    return None


def clean_heading_from_title(raw_title: str):
    """Clean noisy case headings and return a structured title.

    Removes trailing spaced-out markers ("D E C I S I O N", "R E S O L U T I O N")
    and returns both a full and short title.

    Args:
        raw_title (str): Original title text.

    Returns:
        dict[str, str]: Dict with keys "title" (cleaned full title) and "short"
        (cite-formatted title).
    """
    full_title = (
        raw_title.title()
        .strip()
        .removesuffix("D E C I S I O N")
        .strip()
        .removesuffix("R E S O L U T I O N")
        .strip()
    )
    return {"title": full_title, "short": cite_title(full_title)}


def get_header_citation(soup: BeautifulSoup):
    """Extract the case citation from the header of a decision document.

    This scans the portion of HTML before the first <br> tag,
    ignoring boilerplate (like 'E-Library') and applying a Citation extractor.

    Args:
        soup (BeautifulSoup): Parsed HTML document.

    Returns:
        Citation | None: Extracted citation object if found, else None.
    """
    breaks = soup("br")
    if not breaks:
        return None

    for counter, el in enumerate(breaks, start=1):
        el["id"] = f"mark-{counter}"

    first_br = breaks[0]
    body = str(soup)
    marker = str(first_br)
    index = body.find(marker) + len(marker)
    candidate = body[:index]
    if not is_text_possible(candidate, max_len=150):
        return None

    soup = BeautifulSoup(candidate, "lxml")
    texts = soup(string=True)
    for text in texts:
        check_text = text.lower().strip()
        if "-library" in check_text:
            continue
        if citation := Citation.extract_citation(check_text):
            return citation
    return None
