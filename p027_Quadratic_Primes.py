# Euler discovered the remarkable quadratic formula:

# n2+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values  0≤n≤39
#  . However, when  n=40,402+40+41=40(40+1)+41
#   is divisible by 41, and certainly when  n=41,412+41+41
#   is clearly divisible by 41.

# The incredible formula  n2−79n+1601
#   was discovered, which produces 80 primes for the consecutive values  0≤n≤79
#  . The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:

# n2+an+b, where  |a|<range and  |b|≤range

# where  |n| is the modulus/absolute value of  n

# e.g.  |11|=11 and  |−4|=4

# Find the product of the coefficients,  a and  b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of  n, starting with  n=0

import math
import unittest


def is_prime(n):
    """
    Checks if a number is prime using Miller-Rabin primality test.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 0
    k = n - 1
    while k % 2 == 0:
        i += 1
        k //= 2
    d = k

    for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if a >= n:
            break
        x = pow(a, k, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(i - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def quadratic_primes(max_range):
    max_a = max_range
    max_b = max_range
    max_n = 79

    max_primes = 0
    best_a = 0
    best_b = 0

    for a in range(-max_a, max_a + 1):
        for b in range(-max_b, max_b + 1):
            current_primes = 0
            for n in range(0, max_n + 1):
                if is_prime(n**2 + a*n + b):
                    current_primes += 1
                else:
                    break
            if current_primes > max_primes:
                max_primes = current_primes
                best_a = a
                best_b = b

    return best_a * best_b


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(quadratic_primes(1000), -59231)

    def test_2(self):
        self.assertEqual(quadratic_primes(800), -43835)

    def test_3(self):
        self.assertEqual(quadratic_primes(500), -18901)

    def test_4(self):
        self.assertEqual(quadratic_primes(200), -4925)


if __name__ == "__main__":
    unittest.main()

# print(quadratic_primes(200))
