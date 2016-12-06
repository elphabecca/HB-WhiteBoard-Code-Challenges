"""Given a list of numbers 1...max_num, find which one is missing in a list."""


def missing_number(nums, max_num):
    """Given a list of numbers 1...max_num, find which one is missing.

    *nums*: list of numbers 1..[max_num]; exactly one digit will be missing.
    *max_num*: Largest potential number in list
    """

    n = len(nums) + 1
    s = (n * (n+1))/2
    num_sum = sum(nums)

    num = s - num_sum

    return num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASS. NICELY DONE!\n"


# Learned from Solution:

# If you didn't know the formula for the sum:
# expected = sum(range(max_num + 1))