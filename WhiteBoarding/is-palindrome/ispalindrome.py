"""Is this word a palindrome?

    >>> is_palindrome("a")
    True

    >>> is_palindrome("noon")
    True

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("porcupine")
    False

Treat spaces and uppercase letters normally:

    >>> is_palindrome("Racecar")
    False
"""


def is_palindrome(word):
    """Return True/False if this word is a palindrome."""

    i = -1

    for char in word:
        if char != word[i]:
            return False
        i -= 1

    return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"

# LEARNED FROM SOLUTION:

# for i in range(len(word) / 2):
#         if word[i] != word[-i - 1]:
#             return False

# return True

