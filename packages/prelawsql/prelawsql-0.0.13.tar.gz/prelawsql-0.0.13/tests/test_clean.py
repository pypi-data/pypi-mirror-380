import re

import pytest

from prelawsql.clean import (
    bq_line_next_line_not_bq,
    cap_start,
    end_bq,
    line_starts_with_space,
    lone_bq,
    sp_empty_bq,
    start_bq,
    two_spaces_then_line,
    xad,
    xao,
    xxx_bq1,
    xxx_bq2,
    xxx_bq3,
)


def test_xao_matches_non_breaking_space():
    assert xao.search("Hello\xa0World")
    assert not xao.search("Hello World")


def test_xad_matches_soft_hyphen():
    assert xad.search("Hyphen­ated")  # contains U+00AD
    assert not xad.search("Hyphenated")


def test_cap_start_matches_leading_spaces_before_caps():
    assert cap_start.search("   ABC")
    assert not cap_start.search("abc")
    assert not cap_start.search("   123")


def test_xxx_placeholders_blockquote_levels():
    # single-level
    assert xxx_bq1.search("> x x x\n\n")
    # two-level
    assert xxx_bq2.search("> > x x x\n\n")
    # three-level
    assert xxx_bq3.search("> > > x x x\n\n")

    # should not match outside blockquote
    assert not xxx_bq1.search("x x x\n\n")


def test_line_starts_with_space():
    assert line_starts_with_space.match("   indented")
    assert not line_starts_with_space.match("not indented")


def test_two_spaces_then_line():
    assert two_spaces_then_line.search("word  \nnext")
    assert not two_spaces_then_line.search("word \nnext")


def test_start_bq():
    text = "\n\n>\n>\nQuoted"
    assert start_bq.search(text)
    assert not start_bq.search("> Quoted")


def test_end_bq():
    text = "\n>\n>\n\n"
    assert end_bq.search(text)
    assert not end_bq.search("> only one line\n")


def test_lone_bq():
    text = "\n\n>\n\n"
    assert lone_bq.search(text)
    assert not lone_bq.search("> line of text")


def test_sp_empty_bq():
    text = ">\n\n> Next"
    assert sp_empty_bq.search(text)
    assert not sp_empty_bq.search("> content\n\n> more content")


def test_bq_line_next_line_not_bq():
    text = "> Quoted line\nNext line"
    match = bq_line_next_line_not_bq.search(text)
    assert match
    assert match.group().startswith("> Quoted line")
    assert not bq_line_next_line_not_bq.search("> Quoted\n> Next quoted")


# Optional: Parametrize common placeholder pattern
@pytest.mark.parametrize(
    "pattern,text",
    [
        (xao, "foo\xa0bar"),
        (xad, "foo­bar"),  # soft hyphen
        (cap_start, "   Title starts here"),
    ],
)
def test_general_patterns(pattern, text):
    assert pattern.search(text)
