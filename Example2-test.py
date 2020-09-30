import pytest
from Example2 import is_even


@pytest.mark.parametrize("test_input,expected",
                         [
                             (2, True),
                             (0, True),
                             (-3, False),
                             ('Start', None)
                         ])
def test_even(test_input, expected):
    assert is_even(test_input) == expected
