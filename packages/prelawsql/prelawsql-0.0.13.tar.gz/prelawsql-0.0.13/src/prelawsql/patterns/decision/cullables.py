import re

from bs4 import BeautifulSoup

EXTRA_SIR_MADAM = re.compile(
    r"""Sirs\/Mesdames\:""",
    re.I | re.X,
)

EXTRA_ATTEST = re.compile(
    r"""I\s*attest\s*that\s*the\s*conclusion(s)?\s*in\s*the\s*above\s*(Decision|Resolution)\s*""",
    re.I | re.X,
)

EXTRA_RELEASE = re.compile(
    r"""O\s*r\s*d\s*e\s*r\s*o\s*f\s*R\s*e\s*l\s*e\s*a\s*s\s*e\s*""", re.I | re.X
)

EXTRA_NOTICE = re.compile(
    r"""N\s*o\s*t\s*i\s*c\s*e\s*o\s*f\s*J\s*u\s*d\s*g\s*m\s*e\s*n\s*t\s*""", re.I | re.X
)

EXTRA_TAKE_NOTICE = re.compile(r"""Please\s*take\s*notice\s*that\s*on""", re.I | re.X)


def is_extraneous_fragment(text: str) -> bool:
    """
    Check if the text contains extraneous fragments like notices,
    orders of release, attestations, or formal salutations.

    Args:
        text (str): Source text.

    Returns:
        bool: True if an extraneous fragment is found, else False.

    Examples:
        >>> is_extraneous_fragment("Notice of Judgment\\nThis case is resolved...")
        True

        >>> is_extraneous_fragment("Sirs/Mesdames: Please be advised...")
        True

        >>> is_extraneous_fragment("This is a substantive case discussion.")
        False
    """
    short_slice = text[:500]
    long_slice = text[:1000]
    return (
        is_notice(long_slice)
        or is_order_of_release(short_slice)
        or is_attest(long_slice)
        or is_address(long_slice)
    )


def is_notice(text: str) -> bool:
    """
    Detect if the text contains a 'Notice of Judgment' or similar variants.

    Args:
        text (str): Source text.

    Returns:
        bool: True if a notice is detected near the top of the text, else False.

    Examples:
        >>> is_notice("Notice of Judgment rendered on September 10, 2024")
        True

        >>> is_notice("This mentions notice of judgment in a footnote <sup>Notice of Judgment</sup>")
        False
    """
    return (
        is_notice_title(text) or is_notice_please(text) or notice_variant(text)
    ) and no_footnotes_found(text)
    #! although a `notice of judgment` pattern is found, it may be part of a footnote


def no_footnotes_found(text: str) -> bool:
    """
    Is there a footnote found in the raw string? Check if there are no <sup> footnotes in the HTML text.

    Args:
        text (str): HTML or plain text.

    Returns:
        bool: True if no <sup> elements are found, else False.

    Examples:
        >>> no_footnotes_found("Plain text without footnotes")
        True

        >>> no_footnotes_found("Some text<sup>1</sup>")
        False
    """
    notes = BeautifulSoup(text, "lxml")
    return False if len(notes("sup")) else True


def is_notice_title(text: str) -> bool:
    """
    Check specifically for the 'Notice of Judgment' pattern.

    Examples:
        >>> is_notice_title("Notice of Judgment")
        True

        >>> is_notice_title("Random string")
        False
    """
    return is_match_in_text(EXTRA_NOTICE, text)


def is_notice_please(text: str) -> bool:
    """
    Check for the 'Please take notice that on' variant.

    Examples:
        >>> is_notice_please("Please take notice that on October 1...")
        True

        >>> is_notice_please("Other procedural note")
        False
    """
    return is_match_in_text(EXTRA_TAKE_NOTICE, text)


def is_order_of_release(text: str) -> bool:
    """
    Check for 'Order of Release' pattern.

    Examples:
        >>> is_order_of_release("Order of Release granted")
        True

        >>> is_order_of_release("Release the funds")
        False
    """
    return is_match_in_text(EXTRA_RELEASE, text)


def is_attest(text: str) -> bool:
    """
    Check for attestation clauses.

    Examples:
        >>> is_attest("I attest that the conclusions in the above Decision are correct.")
        True

        >>> is_attest("This is a normal paragraph.")
        False
    """
    return is_match_in_text(EXTRA_ATTEST, text)


def is_address(text: str) -> bool:
    """
    Check for formal salutations like 'Sirs/Mesdames:'.

    Examples:
        >>> is_address("Sirs/Mesdames: Please be guided accordingly.")
        True

        >>> is_address("Dear colleagues,")
        False
    """
    return is_match_in_text(EXTRA_SIR_MADAM, text)


def is_match_in_text(pattern: re.Pattern, text: str) -> bool:
    """
    General matcher for patterns near the top of the document.

    Determine whether the following patterns exist in source text;
    And if they do, if they exist near the top of the source text:
    1. notice of judgment
    2. order of release
    3. attestation clause

    Args:
        pattern (re.Pattern): Compiled regex pattern.
        text (str): Text or HTML to check.

    Returns:
        bool: True if the pattern occurs near the top of the text, else False.

    Examples:
        >>> is_match_in_text(EXTRA_NOTICE, "Notice of Judgment at start")
        True

    # TODO: need to validate this
    """
    # create html object from text
    html = BeautifulSoup(text, "lxml")
    # find pattern in html object
    if not (tag := html.find(string=pattern)):
        return False
    # convert target html to string since pattern found
    initiator = str(tag)
    # create text variant of html object to serve as base
    base = str(html)
    # get the text position of initiator string from base
    pos = base.index(initiator)
    # if base position is near top of text, it likely is a match
    if pos < 500:
        return True
    return False


def notice_variant(raw: str) -> bool:
    """
    Handle special cases where 'Notice of Judgment' is hidden
    inside <center> or other HTML tags.

    Args:
        raw (str): Raw HTML string.

    Returns:
        bool: True if a notice is detected, else False.

    Examples:
        >>> notice_variant("<center>Notice of Judgment</center>")
        True

        >>> notice_variant("Plain text with no notice")
        False
    """
    html = BeautifulSoup(raw, "lxml")
    try:
        item = str(html.center.text)  # type: ignore
        return is_match_in_text(EXTRA_NOTICE, item)
    except AttributeError:
        try:
            item = str(html.text)
            return is_match_in_text(EXTRA_NOTICE, item)
        except ValueError:
            return False
    except Exception:
        return False
