// """Return count number of prime numbers, starting at 2.

// For example::

//     >>> primes(0)
//     []

//     >>> primes(1)
//     [2]

//     >>> primes(5)
//     [2, 3, 5, 7, 11]

// """

function primeCount(n) {

    var primeList = [];

    for (var i = 2; primeList.length < n; i++) {
        var isPrime = true;
        for (var j = 2; j < i; j++) {
            if (i % j === 0) {
                isPrime = false;
            }
        }
        if (isPrime) {
            primeList.push(i);
        }
    }

    return primeList
}

console.log(primeCount(0))
console.log(primeCount(1))
console.log(primeCount(5))