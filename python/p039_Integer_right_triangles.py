# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ n, is the number of solutions maximized?
# first you need to find the number of integer_right_angle_triangles for every number and return the max of all of them

import unittest


def integer_right_triangles(n):
    ans = max(range(1, n+1), key=count_solutions)
    return ans


def count_solutions(p):
    result = 0
    for a in range(1, p+1):
        for b in range(a, (p-a)//2 + 1):
            c = p-a-b
            if a*a + b*b == c*c:
                result += 1
    return result


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(integer_right_triangles(500), 420)

    def test_2(self):
        self.assertEqual(integer_right_triangles(1000), 840)

    def test_3(self):
        self.assertEqual(integer_right_triangles(900), 840)

    def test_4(self):
        self.assertEqual(integer_right_triangles(800), 720)


if __name__ == '__main__':
    unittest.main()
