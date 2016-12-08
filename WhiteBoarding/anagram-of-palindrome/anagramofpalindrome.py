"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    pal_dict = {}

    for char in word:
        pal_dict[char] = pal_dict.get(char, 0) + 1

    if len([value for value in pal_dict.values() if value % 2 != 0]) > 1:
        return False

    return True

if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

# LEARNED FROM SOLUTION:
# I liked this b/c it returns false as soon as the second "odd" count comes in

# seen_an_odd = False

#     for count in seen.values():
#         if count % 2 != 0:
#             if seen_an_odd:
#                 return False
#             seen_an_odd = True

#     return True
