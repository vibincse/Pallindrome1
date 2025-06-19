"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome

def test_raises_value_error_on_non_string_input():
    with pytest.raises(ValueError):
        is_palindrome(123)

def test_returns_false_on_empty_string():
    assert is_palindrome("") is False

def test_returns_true_for_single_character():
    assert is_palindrome("a") is True

def test_returns_true_for_two_same_characters():
    assert is_palindrome("bb") is True
