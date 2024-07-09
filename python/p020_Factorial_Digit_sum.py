# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits n!


import math

def sum_factorial_Digits(n):
    digits = str(math.factorial(n))
    return sum(int(c) for c in digits)

# print(sum_factorial_Digits(100))


import unittest

class Test(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(sum_factorial_Digits(100),648)
        
    def test_2(self):
        self.assertEqual(sum_factorial_Digits(25),72)
        
    def test_3(self):
        self.assertEqual(sum_factorial_Digits(10),27)


if __name__ == '__main__':
    unittest.main()