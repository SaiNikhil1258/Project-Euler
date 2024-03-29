# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

# you want to create a string of consecutive numbers and get the required index
import math
import unittest



def constant(n):
    s = "".join(str(i) for i in range(1,n))
    ans = 1
    for i in range(int(math.log10(n))+1):
        ans *= int(s[10**i-1])
    return ans


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(constant(100), 5)

    def test_2(self):
        self.assertEqual(constant(1000), 15)

    def test_3(self):
        self.assertEqual(constant(1000000), 210)


if __name__ == "__main__":
    unittest.main()
