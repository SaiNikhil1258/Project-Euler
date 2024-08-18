# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal fraction part.


def max_reciprocal_cycle_length(n):
    max_cycle_length = 0
    max_cycle_d = 0
    for d in range(2, n):
        cycle_length = get_cycle_length(d)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            max_cycle_d = d
    return max_cycle_d


def get_cycle_length(d):
    remainders = []
    remainder = 1
    while remainder not in remainders:
        remainders.append(remainder)
        remainder *= 10
        remainder %= d
    return len(remainders) - remainders.index(remainder)


# max_reciprocal_cycle_length(900)
import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(max_reciprocal_cycle_length(1000), 983)

    def test_2(self):
        self.assertEqual(max_reciprocal_cycle_length(700), 659)

    def test_3(self):
        self.assertEqual(max_reciprocal_cycle_length(800), 743)

    def test_4(self):
        self.assertEqual(max_reciprocal_cycle_length(900), 887)


if __name__ == "__main__":
    unittest.main()
