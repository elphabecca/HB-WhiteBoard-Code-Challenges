"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"
    
    curr = 0
    count = 0

    if len(branches) == 2:
        return 1

    while curr < len(branches) - 1:
        if branches[curr + 2] == 0:
            curr += 1
        curr += 1
        count += 1

    return count

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"


# SOLUTION:
# If you always add two but then subtract one if the lemur CAN'T jump that far, you'll take care
# of the edge cases without specifically having to account for them.

#     at = 0
#     n_jumps = 0

#     while at < len(branches) - 1:
#         at += 2
#         if at >= len(branches) or branches[at] == 1:
#             # We can jump this far, so only jump 1
#             at -= 1
#         n_jumps += 1

#     return n_jumps



