# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?
#* Hint
# we need to find a arithmetic sequence in which each of the terms increases by a certain number one such sequence with a step of 3330 is given above
# there is another sequence with 4-digit sequence
# 4-digit < 10000
# a,b,c < 10000 and should be primes
# we need to find another such sequence so we can eliminate the numbers starting with the 1487 or its permutation.
# so basically the condition is 
# (a,b,c)< 10_000 and should be primes and each should be a permutation of each other.

import unittest
import math


def list_primality(n: int):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(math.isqrt(n) + 1):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def compute():
    LIMIT = 10000
    isprime = list_primality(LIMIT - 1)
    for base in range(1000, LIMIT):
        if isprime[base]:
            for step in range(1, LIMIT):
                a = base + step
                b = a + step
                if a < LIMIT and isprime[a] and has_same_digits(a, base) and b < LIMIT and isprime[b] and has_same_digits(b, base) and (base != 1487 or a != 4817):
                    return str(base) + str(a) +  str(b)
    raise RuntimeError("Not found")


def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compute(),'296962999629')

if __name__=="__main__":
    unittest.main()