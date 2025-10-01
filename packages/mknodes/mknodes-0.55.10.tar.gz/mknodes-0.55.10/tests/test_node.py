from __future__ import annotations

import pytest

import mknodes as mk


def test_equality():
    node_1 = mk.MkHeader("test")
    str(node_1)  # generate build stats
    node_2 = mk.MkHeader("test")
    str(node_2)  # generate build stats
    assert node_1 == node_2


if __name__ == "__main__":
    pytest.main([__file__])
