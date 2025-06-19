"""
Validates strings as palindromes.
"""
def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    if value == "":
        return False


