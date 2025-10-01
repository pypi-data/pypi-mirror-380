from __future__ import annotations

import pytest

import mknodes as mk


EXPECTED = """## Header

[^1]:
    abcde
    fghi
[^2]:
    abcde
    fghi
[^3]:
    abcde
    fghi
[^4]:
    abcde
    fghi
[^5]:
    abcde
    fghi
[^6]:
    abcde
    fghi
[^7]:
    abcde
    fghi
[^8]:
    abcde
    fghi
[^9]:
    abcde
    fghi
[^10]:
    abcde
    fghi
"""

EXPECTED_SORTED = """[^1]:
    1
[^2]:
    2
"""


def test_empty():
    annotation = mk.MkFootNotes()
    assert not str(annotation)


def test_if_annotations_get_sorted():
    node = mk.MkFootNotes()
    node[2] = "2"
    node[1] = "1"
    assert str(node) == EXPECTED_SORTED


def test_markdown():
    annotation = mk.MkFootNotes(["abcde\nfghi"] * 10, header="Header")
    assert str(annotation) == EXPECTED


def test_constructors():
    annotation_1 = mk.MkFootNotes(["abc", "def"])
    anns = {1: "abc", 2: "def"}
    annotation_2 = mk.MkFootNotes(anns)
    assert str(annotation_1) == str(annotation_2)


def test_mapping_interface():
    ann = mk.MkFootNotes()
    ann[1] = "test"
    assert str(ann[1]) == "[^1]:\n    test\n"


if __name__ == "__main__":
    pytest.main([__file__])
