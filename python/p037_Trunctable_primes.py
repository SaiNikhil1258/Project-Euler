# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right #  and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only n (8 ≤ n ≤ 11) primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


import itertools
import unittest


def truncatable_primes(n):
    ans = sum(itertools.islice(
        filter(is_truncatable_prime, itertools.count(10)), n))
    return ans


def is_truncatable_prime(n):
    # Test if left-truncatable
    i=10
    while i <= n:
        if not is_prime(n % i):
            return False
        i *= 10

    # Test if right-truncatable
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


def is_prime(n):
    if n < 2:
        return False

    if n % 2 == 0:
        return n == 2

    if n % 3 == 0:
        return n == 3

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
    return True



class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(truncatable_primes(10),8920)

    def test_2(self):
        self.assertEqual(truncatable_primes(11), 748317)

    def test_3(self):
        self.assertEqual(truncatable_primes(8), 1986)

    def test_4(self):
        self.assertEqual(truncatable_primes(9),5123)\
        


if __name__== "__main__":
    unittest.main()