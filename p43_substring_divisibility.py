# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let  d1 be the  1st digit,  d2 be the  2nd digit, and so on.
# In this way, we note the following:

# d2d3d4=406   is divisible by 2
# d3d4d5=063   is divisible by 3
# d4d5d6=635   is divisible by 5
# d5d6d7=357   is divisible by 7
# d6d7d8=572   is divisible by 11
# d7d8d9=728   is divisible by 13
# d8d9d10=289  is divisible by 17


# Find the sum of all 0 to n pandigital numbers with sub-strings fulfilling n - 2 of these divisibility properties.

# Note: Pandigital numbers starting with 0 are to be considered in the result.


import itertools
import unittest


# checks if the substring of the given number is divisible by the n-2 primes or not
def is_divisible(num, n):
    DIVISIBILITY_primes = [2, 3, 5, 7, 11, 13, 17]
    DIVISIBILITY_TESTS = DIVISIBILITY_primes[:n-2]
    return all((int(num[i + 1]) * 100 + int(num[i + 2]) * 10 + int(num[i + 3])) % p == 0
               for (i, p) in enumerate(DIVISIBILITY_TESTS))


# The function which checks all the possible permutations which are substring divisible
def substring_divisibility(n):
    res = []
    for num in itertools.permutations(list(range(n+1))):
        temp = "".join(map(str, num))
        if is_divisible(temp, n):
            res.append(int(temp))
    return sum(res)


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(substring_divisibility(9), 16695334890)

    def test_2(self):
        self.assertEqual(substring_divisibility(8), 1113342912)

    def test_3(self):
        self.assertEqual(substring_divisibility(7), 1099210170)

    def test_4(self):
        self.assertEqual(substring_divisibility(5), 12444480)


if __name__ == '__main__':
    unittest.main()
