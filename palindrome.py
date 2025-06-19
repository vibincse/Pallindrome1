"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(value):
    if not isinstance(value, str):
        raise ValueError("Input must be a string")
    if value == "":
        return False
    if len(value) == 1:
        return True

    dq = deque(value.lower())  # convert to lowercase
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


