# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?





import itertools
import unittest

# print(primes)


def main():
    # this is the trick we only return the number that doesn't satisfy the condition
    ans = next(itertools.filterfalse(goldbach, itertools.count(9, 2)))
    return ans


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


def goldbach(n):
    if n % 2 == 0 or is_prime(n):
        # if prime then not a composite number
        return True
    for i in itertools.count(1):
        k = n - 2 * i * i
        if k <= 0:
            return False
        elif is_prime(k):
            return True


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main(), 5777)


if __name__ == "__main__":
    unittest.main()
