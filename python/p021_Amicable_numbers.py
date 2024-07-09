# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under n.

# Approach amicable numbers are such that sum of proper divisors of a = b and sum of proper divisors of b = a
# such numbers a, b are called as amicable numbers
# you need a dictionary to store the sum of proper divisors of each number
# there are some self amicable numbers 
# in the for loop for i = 220 the values of a and b will be 
# a = 284, b = 220
# to remove the self amicable numbers we need to check if i != b

## Approach 2 you can calculate all the divisors sum once and store them in a auxillary array

def sum_amicable_numbers(n):
    amicable_numbers = set()
    for i in range(2, n):
        a = sum_proper_divisors(i)
        b = sum_proper_divisors(a)
        if i == b and i != a:
            amicable_numbers.add(i)
            amicable_numbers.add(a)
    return sum(amicable_numbers)

def sum_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sum(divisors)

# print(sum_amicable_numbers(10000))

import unittest

class Test(unittest.TestCase):
    def test_sum_amicable_numbers(self):
        self.assertEqual(sum_amicable_numbers(10000), 31626)
        
    def test_2(self):
        self.assertEqual(sum_amicable_numbers(1000),504)
        
    def test_3(self):
        self.assertEqual(sum_amicable_numbers(2000), 2898)
    
    def test_4(self):
        self.assertEqual(sum_amicable_numbers(5000), 8442)    
        

if __name__ == '__main__':
    unittest.main()
