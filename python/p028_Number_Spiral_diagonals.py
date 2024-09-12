# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in an n by n spiral formed in the same way?
# for the top right element `n^2`
# for the top left element the pattern will be  n^2 -(n-1)
# for th bottom left element n^2 -2(n-1)
# for the bottom right element n^2 - 3(n-1)
#  for the inner matrix the pattern wil just be n -= 2
# repeat the process for every inner circle from the 3 to n+1

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13


def sum_spiral_diagonals(n):
    ans = 1
    ans += sum(4 * i * i - 6 * (i - 1) for i in range(3, n + 1, 2))
    return ans


# print(sum_spiral_diagonals(1001))

import unittest


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(sum_spiral_diagonals(101), 692101)

    def test_2(self):
        self.assertEqual(sum_spiral_diagonals(303), 18591725)

    def test_3(self):
        self.assertEqual(sum_spiral_diagonals(505), 85986601)

    def test_4(self):
        self.assertEqual(sum_spiral_diagonals(1001), 669171001)


if __name__ == "__main__":
    unittest.main()
