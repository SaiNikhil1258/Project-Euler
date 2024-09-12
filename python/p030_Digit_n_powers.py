# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of n powers of their digits.

import unittest


def digit_power(n, power):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**power
        n //= 10
    return sum


# print(digit_power(1634, 4))
# print(1**4 + 6**4 + 3**4 + 4**4)


def Digitpower(n):
    result = []
    for i in range(2, 10 ** (n + 1)):
        if i == digit_power(i, n):
            result.append(i)
    return sum(result)


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Digitpower(2), 0)

    def test_2(self):
        self.assertEqual(Digitpower(3), 1301)

    def test_3(self):
        self.assertEqual(Digitpower(4), 19316)

    def test_4(self):
        self.assertEqual(Digitpower(5), 443839)


if __name__ == "__main__":
    unittest.main()
