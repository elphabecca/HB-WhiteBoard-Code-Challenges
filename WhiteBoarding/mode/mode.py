"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> find_mode([1]) == {1}
    True

    >>> find_mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> find_mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def find_mode(nums):
    """Find the most frequent num(s) in nums."""

    num_dict = {}

    for num in nums:
        num_dict[num] = num_dict.get(num, 0) + 1

    max_count = max(num_dict.values())
    mode = set()

    for v, c in num_dict.items():
        if c == max_count:
            mode.add(v)

    return mode

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. HOORAY!\n"


# Learned from Solution:
# You don't need the ".items()" in line 29
# A Set is the best data structure to hold the list of modes for many reasons.
