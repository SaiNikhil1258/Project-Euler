# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2exponent?




def power_digit_sum(n):
    power = 2**n
    sum =0
    digits = str(power)
    for i in digits:
        sum += int(i)
    return sum
# or you can use list comprehension
    # return sum(int(i) for i in str(2**n))



# print(power_digit_sum(1000))

import unittest

class Testpower_digit_sum(unittest.TestCase):
    
    def test_power_digit_sum(self):
        self.assertEqual(power_digit_sum(1000), 1366)
        
    def test_power_digit_sum_2(self):
        self.assertEqual(power_digit_sum(128), 166)
        
    def test_power_digit_sum_3(self):
        self.assertEqual(power_digit_sum(15), 26)

if __name__ == '__main__':
    unittest.main()


