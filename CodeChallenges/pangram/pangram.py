"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False
"""


def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    for char in sentence:
        if char in alphabet:
            alphabet.remove(char)

    if not alphabet:
        return True
    return False



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"


# FROM SOLUTION:

# Use a set to reduce runtime:
# def is_pangram(sentence):
#     """Given a string, return True if it is a pangram, False otherwise."""

#     # START SOLUTION

#     used = {char.lower() for char in sentence if char.isalpha()}
#     return len(used) == 26
