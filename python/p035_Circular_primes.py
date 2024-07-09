# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below n, whereas 100 ≤ n ≤ 1000000?

# Note:

# Circular primes individual rotation can exceed n



def sieve_of_eratosthenes(n):
    """
    Uses the Sieve of Eratosthenes to find all prime numbers up to n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]


def is_circular_prime(n,is_prime):
    """
    Checks if a number is a circular prime.
    """
    s = str(n)
    for i in range(len(s)):
        if int(s[i:] + s[:i]) not in is_prime:
            return False
    return True


def circular_primes(n):
    """
    Returns the number of circular primes below n.
    """
    is_prime = sieve_of_eratosthenes(n)
    return len([i for i in is_prime if is_circular_prime(i, is_prime)])


import unittest

class TestCircularPrimes(unittest.TestCase):
    def test_circular_primes(self):
        self.assertEqual(circular_primes(100), 13)
    def test_circular_primes_2(self):
        self.assertEqual(circular_primes(100000), 43)
    def test_circular_primes_4(self):
        self.assertEqual(circular_primes(1000000), 55)
if __name__ == '__main__':
    unittest.main()