# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.# 

import unittest


def main(n,m):
    sum = 0
    for i in range(1, n+1):
        sum += i**i

    return str(sum)[-m:]



class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(main(10,3),'317')

    def test_2(self):
        self.assertEqual(main(150,6),'029045')

    def test_3(self):
        self.assertEqual(main(673,7),'2473989')

    def test_4(self):
        self.assertEqual(main(1000,10), '9110846700')


if __name__ == "__main__":
    unittest.main()





