# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number 
# would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over n divisors?



from math import sqrt


def count_divisors(n):
    divisors = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors+=2
    return divisors


def main(i):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        if count_divisors(triangle_number) >= i:
            return triangle_number
        n += 1

# print(main(5)) #28
# print(main(500)) #76576500


import unittest

class Testmain(unittest.TestCase):
    
    def test_main_1(self):
        self.assertEqual(main(5), 28)
    
    def test_main_2(self):
        self.assertEqual(main(500), 76576500)
    
    def test_main_3(self):
        self.assertEqual(main(374), 17907120)
    
    def test_main_4(self):
        self.assertEqual(main(167), 1385280)
    
    def test_main_5(self):
        self.assertEqual(main(23), 630)
        
    
    

if __name__ == '__main__':
    unittest.main()
