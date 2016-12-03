"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    poss_num_list = [1,2,3,4,5,6,7,8,9,10]
    r_num_list = []

    for num in range(n):
        n = random.choice(poss_num_list)
        r_num_list.append(n)
        poss_num_list.remove(n)

    return r_num_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"


# FROM THE SOLUTION:

#     You can denote a list of a range of numbers like this:
#     nums = range(1, 11)