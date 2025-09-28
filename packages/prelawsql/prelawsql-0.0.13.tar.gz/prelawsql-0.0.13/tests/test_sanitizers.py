import pytest

from prelawsql.sanitizer import decision_sanitizer, statute_sanitizer


@pytest.mark.parametrize(
    "html, expected",
    [
        ("<b>Bold</b>", "<strong>Bold</strong>"),
        ("<i>Italic</i>", "<em>Italic</em>"),
        ("<span style='font-weight:bold'>Bold</span>", "<strong>Bold</strong>"),
        ("<form>Form</form>", "<p>Form</p>"),
    ],
)
def test_decision_sanitizer_transforms(html, expected):
    """Decision sanitizer should normalize inline tags properly."""
    result = decision_sanitizer.sanitize(html)
    assert result == expected


def test_decision_sanitizer_preserves_typographic_whitespace():
    html = "Hello&nbsp;World"
    result = decision_sanitizer.sanitize(html)
    # Decision sanitizer keeps non-breaking spaces as Unicode \xa0
    assert "Hello\xa0World" in result


@pytest.mark.parametrize(
    "html, expected",
    [
        ("<i>Italic</i>", "<em>Italic</em>"),
        ("<span>Span text</span>", "<p>Span text</p>"),
        ("<font>Font text</font>", "<p>Font text</p>"),
    ],
)
def test_statute_sanitizer_transforms(html, expected):
    """Statute sanitizer should normalize inline tags properly."""
    result = statute_sanitizer.sanitize(html)
    assert result == expected


def test_statute_sanitizer_does_not_preserve_typographic_whitespace():
    html = "Hello&nbsp;World"
    result = statute_sanitizer.sanitize(html)
    # &nbsp; converted to space
    assert "Hello World" in result


def test_anchor_sanitization_decision():
    html = '<a href="http://example.com" target="_blank">Link</a>'
    result = decision_sanitizer.sanitize(html)
    # Keeps href and ensures rel="noopener" is present for security
    assert '<a href="http://example.com"' in result
    assert 'target="_blank"' in result
    assert 'rel="noopener"' in result
    assert "Link</a>" in result


def test_anchor_sanitization_statute():
    html = '<a href="http://example.com" target="_blank">Link</a>'
    result = statute_sanitizer.sanitize(html)
    # Since "a" is not allowed in statute_sanitizer, link is stripped
    assert "Link" in result
    assert "<a" not in result
