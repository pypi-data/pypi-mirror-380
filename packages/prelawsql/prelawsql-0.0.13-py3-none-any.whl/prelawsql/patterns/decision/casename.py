import re
from collections.abc import Iterator

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


def clean_vs_casename(text: str):
    """
    Replace triple-asterisk case markers with single-asterisk italics.

    Args:
        text (str): Input string possibly containing ***Case vs. Case*** markers.

    Returns:
        str: String with markers replaced by *Case vs. Case*.

    Examples:
        >>> clean_vs_casename("This is a case: ***People vs. Santos***.")
        'This is a case: *People vs. Santos*.'

        >>> clean_vs_casename("Multiple ***Lopez v. Dela Cruz*** and ***Garcia vs. Reyes*** here")
        'Multiple *Lopez v. Dela Cruz* and *Garcia vs. Reyes* here'

        >>> clean_vs_casename("Nothing to clean here")
        'Nothing to clean here'
    """
    while True:
        if match := italicized_case.search(text):
            text = text.replace(match.group(), f"*{match.group('casename')}*")
        else:
            break
    return text


def tags_from_title(id: str, text: str) -> Iterator[dict[str, str]]:
    """
    Generate tags from case titles based on keyword matching.

    Args:
        id (str): Identifier for the case.
        text (str): Title or description of the case.

    Yields:
        dict[str, str]: Dictionary containing {"key_id": id, "tag": tag}.

    Examples:
        >>> list(tags_from_title("123", "In re: Petition for Habeas Corpus"))
        [{'key_id': '123', 'tag': 'specpro'}]

        >>> list(tags_from_title("456", "People of the Philippines vs. Santos"))
        [{'key_id': '456', 'tag': 'crime'}]

        >>> list(tags_from_title("789", "Commissioner of Internal Revenue vs. Cruz"))
        [{'key_id': '789', 'tag': 'tax'}]

        >>> list(tags_from_title("101", "Employment dispute, NLRC"))
        [{'key_id': '101', 'tag': 'labor'}]

        >>> list(tags_from_title("202", "Civil case with no keywords"))
        []
    """

    def is_contained(target_text: str, matches: list[str]) -> bool:
        return any(m.lower() in target_text.lower() for m in matches)

    tags = []
    if is_contained(
        text,
        [
            "habeas corpus",
            "guardianship of",
            "writ of amparo",
            "habeas data",
            "change of name",
            "correction of entries",
            "escheat",
        ],
    ):
        tags.append("specpro")

    if is_contained(
        text,
        [
            "matter of the will",
            "testamentary proceedings",
            "probate",
        ],
    ):
        tags.append("succession")

    if is_contained(
        text,
        [
            "disbarment",
            "practice of law",
            "office of the court administrator",
            "disciplinary action against atty.",
        ],
    ):
        tags.append("ethics")

    if is_contained(
        text,
        [
            "for naturalization",
            "certificate of naturalization",
            "petition for naturalization",
            "citizen of the philippines",
            "commissioner of immigration",
            "commissioners of immigration",
            "philippine citizenship",
        ],
    ):
        tags.append("Immigration")

    if is_contained(
        text,
        [
            "central bank of the philippines",
            "bangko sentral ng pilipinas",
        ],
    ):
        tags.append("bank")

    if is_contained(
        text,
        [
            "el pueblo de filipinas",
            "el pueblo de las islas filipinas",
            "los estados unidos",
            "testamentaria",
        ],
    ):
        tags.append("legacy-spanish")

    if is_contained(
        text,
        ["the united States, plaintiff "],
    ):
        tags.append("legacy-us")

    if is_contained(
        text,
        [
            "people of the philipppines",
            "people of the philippines",
            "people  of the philippines",
            "people of the  philippines",
            "people of the philipines",
            "people of the philippine islands",
            "people philippines, of the",
            "sandiganbayan",
            "tanodbayan",
            "ombudsman",
        ],
    ):
        tags.append("crime")

    if is_contained(
        text,
        [
            "director of lands",
            "land registration",
            "register of deeds",
        ],
    ):
        tags.append("property")

    if is_contained(
        text,
        [
            "agrarian reform",
            "darab",
        ],
    ):
        tags.append("agrarian")

    if is_contained(
        text,
        [
            "collector of internal revenue",
            "commissioner of internal revenue",
            "bureau of internal revenue",
            "court of tax appeals",
        ],
    ):
        tags.append("tax")

    if is_contained(
        text,
        [
            "collector of customs",
            "commissioner of customs",
        ],
    ):
        tags.append("customs")

    if is_contained(
        text,
        [
            "commission on elections",
            "comelec",
            "electoral tribunal",
        ],
    ):
        tags.append("elections")

    if is_contained(
        text,
        [
            "workmen's compensation commission",
            "employees' compensation commission",
            "national labor relations commission",
            "bureau of labor relations",
            "nlrc",
            "labor union",
            "court of industrial relations",
        ],
    ):
        tags.append("labor")

    for tag in tags:
        yield {"key_id": id, "tag": tag}
