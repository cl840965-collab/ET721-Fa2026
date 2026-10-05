"""
Claudio Lopez
Oct 5, 2026
Lab 9: Unit Testing using Pytest
"""
import pytest
from math_utils import *
# ex 1
def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(-1, 5) == -5
def test_divide():
    assert divide(10,2) == 5
    assert divide(1, 3) == pytest.approx(0.33, abs=0.01)
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)
# ex 2
def test_valid_password():
    assert validate_password("pass12345") is True
def test_short_password():
    assert validate_password("pass1") is False
def test_no_number():
    assert validate_password("testingpasssword") is False
# ex 3
@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-2, True),
        (7, False),
    ]
)

def test_is_even(n, expected):
    assert is_even(n) == expected
# ex 4
@pytest.mark.parametrize(
    "n, expected",
    [
        ("pass12345", True),
        ("pass1", False),
        ("testingpassword", False),
    ]
)

def test_password(n, expected):
    assert validate_password(n) == expected