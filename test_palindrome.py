"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome

def test_raises_value_error_on_non_string_input():
    with pytest.raises(ValueError):
        is_palindrome(123)
