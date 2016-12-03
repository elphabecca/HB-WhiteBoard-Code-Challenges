"""Is a number a prime number?

Only numbers >1 can be prime numbers:

    >>> is_prime(0)
    False

    >>> is_prime(1)
    False

Any number >1 that has no divisors other than 1 and itself
is a prime number:

    >>> is_prime(2)
    True

    >>> is_prime(3)
    True

    >>> is_prime(4)
    False

    >>> is_prime(11)
    True

    >>> is_prime(999)
    False
"""


def is_prime(num):
    """Is a number a prime number?"""

    if num <= 1:
        return False

    for div in range(2,num):
        if num % div == 0:
            return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU MET YOUR PRIME DIRECTIVE!\n"


# LEARNED FROM SOLUTION:

# Could sub first conditional with if num < 2: return False




