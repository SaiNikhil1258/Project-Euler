# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import functools
import itertools
import unittest

@functools.cache
def unique_prime_factor(number):
    """Return the largest prime factor of the given number."""
    prime_factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime_factors.append(i)
            while number % i == 0:
                number //= i
    if number > 1:
        prime_factors.append(number)
    if len(prime_factors) == len(set(prime_factors)):
        return len(prime_factors)


def compute(n):
    def cond(i):
        for j in range(n):
            if unique_prime_factor(i + j) != n:
                return False
        return True
    ans = next(filter(cond, itertools.count(10**(n-1))))
    return ans


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(2),14)

    def test_2(self):
        self.assertEqual(compute(3),644)
    
    def test_3(self):
        self.assertEqual(compute(4),134043)


if __name__ == "__main__":
    unittest.main()