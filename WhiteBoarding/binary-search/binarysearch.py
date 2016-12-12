"""Using a binary search, find val in a range of 1-100. Return # of guesses.

Construct a list of 1-100 (inclusive). Write a binary search that searches
for val in that list (val will always be a number between 1 and 100).

Return the number of searches it took to find val. For a proper binary search
of 1-100, this should never be more than 7.

    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
"""

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"
    num_guesses = 1
    nums = range(1,101)
    guess = 50

    while guess != val:
        if val > guess:
            nums = range(guess, max(nums)+1)
            i = len(nums)/2
            guess = nums[i]
            num_guesses += 1
        if val < guess:
            nums = range(nums[0], guess)
            i = len(nums)/2
            guess = nums[i]
            num_guesses += 1

    return num_guesses


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"

# SOLUTION:
# This keeps num_guesses at 0, and the higher_than/lower_than keeps it from always having to create new lists,
# which is positive for runtime.  Also the guess = None is really clever!

# def binary_search(val):
#     """Using binary search, find val in range 1-100. Return # of guesses."""

#     assert 0 < val < 101, "Val must be between 1-100"

#     num_guesses = 0

#     # START SOLUTION #

#     higher_than = 0
#     lower_than = 101
#     guess = None

#     while guess != val:
#         num_guesses += 1
#         guess = (lower_than - higher_than) / 2 + higher_than

#         if val > guess:
#             higher_than = guess

#         elif val < guess:
#             lower_than = guess

#     # END SOLUTION

#     return num_guesses
