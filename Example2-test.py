import pytest
from Example2 import is_even


@pytest.mark.parametrize("test_input,expected", [
    (2, True),
    (1, False),
    (0, True),
    (-3, False),
    (-2, True),
    ('Start', None)
])
def test_even(test_input, expected):
    assert is_even(test_input) == expected
