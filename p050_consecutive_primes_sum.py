# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


# * Hint
#  first you want to have a list of primes within 1_000_000 and another bool array of a prime or not.
# with two loops you loop through the numbers and checking if the sum is also a prime or not.


import math
import unittest


def list_primality(n: int):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(math.isqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def list_primes(n: int):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


def compute():
    res = 0
    is_prime = list_primality(999999)
    primes = list_primes(999999)
    consecutive = 0
    for i in range(len(primes)):
        # you loop the primes and add all the other primes until 1000000 limit
        sum = primes[i]
        count = 1
        for j in range(i+1, len(primes)):
            # loop through all the other primes and add them to sum and check if sum is a prime and less than the limit
            sum += primes[j]
            count += 1
            if sum >= len(is_prime):
                break
# is sum is prime and count is greater than the consecutive then we have found a potential number
            # we update it
            if is_prime[sum] and count > consecutive:
                res = sum
                consecutive = count
    return res


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(), 997651)


if __name__ == "__main__":
    unittest.main()
