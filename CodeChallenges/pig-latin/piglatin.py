"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """
    word_list = phrase.split()
    vowel_set = set(['a', 'e', 'i', 'o', 'u'])
    new_phrase = ''

    for word in word_list:
        if word[0] in vowel_set:
            curr_word = word + 'yay '
            new_phrase += curr_word
        else:
            curr_word = word[1:] + word[0] + 'ay '
            new_phrase += curr_word

    return new_phrase[0:-1]


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
