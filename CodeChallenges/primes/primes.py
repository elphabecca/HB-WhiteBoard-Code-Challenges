"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(count):
    """Return count number of prime numbers, starting at 2."""

    return_primes = []

    for i in range(2, 101):

        if len(return_primes) == count:
            return return_primes

        is_prime = True

        for j in range(2,i):
            if i % j == 0:
                is_prime = False

        if is_prime:
            return_primes.append(i)




    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT WORK!\n"
