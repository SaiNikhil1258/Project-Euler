# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through n pandigital.

# Hint: Some products can be obtained in more than one way so be sure to only include it once in your sum 1.

# one approach is to iterate through all the numbers in the range of the given number of digits and check if the number is pandigital or not.


# the better approach is by using the property of pandigital numbers.
# if the sum of digits of multiplier, multiplican and product is equal to the number of digits then the number is pandigital.
# so if the number of digits is 9 we only need to iterate for numbers less than 10000.
# this is because 99*99 = 9801 -> 8 digits if you increase either the multiplicand and the multiplier we will get a number with more than 9 digits.
# so those all are redundant calculations the limit will be under the 10000 mark

# for 4 digits the limit is less than 100
# for 6 digits the limit is less than 1000



import math 
import unittest

def pan_digital_products(digits=9):
	if digits ==4:
		limit = 100
	elif digits ==6: #these checks will reduce the number of redundant calculations.
		limit = 1000
	else:
		limit = 10000
	ans= sum(i for i in range(1,limit) if is_pandigital(i,digits))
	return ans

def is_pandigital(n,digits):    
    number = [str(i) for i in range(1,digits+1)]
    # print("".join(number))
    for i in range(1,math.isqrt(n)+1):
        if n % i == 0:
            temp = str(n) + str(i) + str(n//i)
            if "".join(sorted(temp)) == "".join(number):
                return True
    return False


class Test(unittest.TestCase):

	def test_1(self):
		self.assertEqual(pan_digital_products(4),12)
		
	def test_2(self):
		self.assertEqual(pan_digital_products(6),162)
		
	def test_3(self):
		self.assertEqual(pan_digital_products(7),0)

	def test_4(self):
		self.assertEqual(pan_digital_products(),45228)


if __name__ == "__main__":
      unittest.main()			
