from bs4 import BeautifulSoup

from prelawsql.header import (
    DECISION_PATTERN,
    DIVISION_PATTERN,
    ENBANC_PATTERN,
    RESOLUTION_PATTERN,
    clean_category,
    clean_composition,
    clean_heading_from_title,
    get_header_citation,
    is_opinion_label,
)


def test_is_opinion_label():
    assert is_opinion_label("Concurring Opinion")
    assert is_opinion_label("Dissenting Opinion")
    assert not is_opinion_label("Random Label")
    assert not is_opinion_label("x" * 100)


def test_clean_composition_enbanc():
    soup = BeautifulSoup("<h2>Supreme Court En Banc</h2>", "lxml")
    assert clean_composition(soup) == "En Banc"


def test_clean_composition_division():
    soup = BeautifulSoup("<h2>Third Division</h2>", "lxml")
    assert clean_composition(soup) == "Division"


def test_clean_category_decision():
    soup = BeautifulSoup("<h3>Decision</h3>", "lxml")
    assert clean_category(soup) == "Decision"


def test_clean_category_resolution_spaced():
    soup = BeautifulSoup("<h3>R E S O L U T I O N</h3>", "lxml")
    assert clean_category(soup) == "Resolution"


def test_clean_heading_from_title():
    raw = "Case Title D E C I S I O N"
    cleaned = clean_heading_from_title(raw)
    assert "Case Title" in cleaned["title"]
    assert "short" in cleaned


def test_patterns_match():
    assert ENBANC_PATTERN.search("en banc")
    assert DIVISION_PATTERN.search("division")
    assert DECISION_PATTERN.search("D E C I S I O N")
    assert RESOLUTION_PATTERN.search("R E S O L U T I O N")


def test_get_header_citation_none():
    # Minimal soup with no <br> means no citation
    soup = BeautifulSoup("<html><body>No breaks here</body></html>", "lxml")
    assert get_header_citation(soup) is None
