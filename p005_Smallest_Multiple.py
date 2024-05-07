# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?



def compute_gcd(x, y):
  while(y):
    x, y = y, x % y
  return x

# This function computes LCM of two numbers
def compute_lcm(x, y):
  lcm = (x*y)//compute_gcd(x,y)
  return lcm

# This function computes LCM of numbers from 1 to n
def compute_lcm_range(n):
  lcm = 1
  for i in range(1, n+1):
    lcm = compute_lcm(lcm, i)
  return lcm

# print(compute_lcm_range(10))


# For n = 10, let's find the LCM using prime factorization:

# Prime factorize each number from 1 to 10:
# 1 = 1
# 2 = 2
# 3 = 3
# 4 = 2^2
# 5 = 5
# 6 = 2 * 3
# 7 = 7
# 8 = 2^3
# 9 = 3^2
# 10 = 2 * 5
# Identify the highest power of each prime factor across all numbers:
# 2: highest power is 3 (from 8)
# 3: highest power is 2 (from 9)
# 5: highest power is 1 (from 5 and 10)
# 7: appears only in 7, with power 1
# Take the product of these highest powers:
# LCM = 2^3 * 3^2 * 5 * 7 = 2520



# 2520
import unittest

class TestSmallestMultiple(unittest.TestCase):

    def test_compute_gcd_1(self):
        self.assertEqual(compute_gcd(12, 18), 6)

    def test_compute_gcd_2(self):
        self.assertEqual(compute_gcd(25, 15), 5)

    def test_compute_lcm_1(self):
        self.assertEqual(compute_lcm(12, 18), 36)

    def test_compute_lcm_2(self):
        self.assertEqual(compute_lcm(25, 15), 75)

    def test_compute_lcm_range_1(self):
        self.assertEqual(compute_lcm_range(10), 2520)

    def test_compute_lcm_range_2(self):
        self.assertEqual(compute_lcm_range(20), 232792560)
        
    def test_compute_lcm_range_3(self):
        self.assertEqual(compute_lcm_range(13), 360360)

if __name__ == '__main__':
    unittest.main()
