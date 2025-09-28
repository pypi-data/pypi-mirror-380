from http import HTTPStatus

import httpx
from bs4 import BeautifulSoup


def url_to_content(url: str) -> bytes | None:
    """Fetch the contents of a URL.

    This function issues a GET request to the given URL. If the response
    returns status 200 (OK), the raw content (e.g., HTML, PDF, image bytes)
    is returned. Otherwise, ``None`` is returned.

    Args:
        url: The URL to fetch.

    Returns:
        The response body as bytes if the status code is 200, otherwise ``None``.

    Example:
        >>> from unittest.mock import patch, Mock
        >>> mock_response = Mock(status_code=200, content=b"<html></html>")
        >>> with patch("httpx.get", return_value=mock_response):
        ...     url_to_content("http://example.com")
        b'<html></html>'
    """
    res = httpx.get(url, follow_redirects=True, timeout=90.0)
    if res.status_code == HTTPStatus.OK:
        return res.content
    return None


def url_to_soup(url: str) -> BeautifulSoup | None:
    """Fetch a URL and parse it into a `BeautifulSoup` object.

    This function first fetches content from the given URL using
    :func:`url_to_content`. If successful, the raw content is parsed into
    a BeautifulSoup object using the ``lxml`` parser.

    Args:
        url: The URL to fetch.

    Returns:
        A BeautifulSoup object if the URL could be fetched successfully,
        otherwise ``None``.

    Example:
        >>> from unittest.mock import patch, Mock
        >>> mock_response = Mock(status_code=200, content=b"<html><p>Hello</p></html>")
        >>> with patch("httpx.get", return_value=mock_response):
        ...     soup = url_to_soup("http://example.com")
        >>> soup.p.text
        'Hello'
    """
    content = url_to_content(url=url)
    if content:
        return BeautifulSoup(content, "lxml")
    return None
