# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# yuou can just brute force for the solution
# a small addition of storing the factorials of 0 through 9
# this will improve the speed

from math import factorial as fact
import unittest

# print(fact(5))


def Digit_factorials():
    factorials = {str(i): fact(i) for i in range(10)}
    res = []
    for i in range(3, 10000000):
        sum_of_fact = sum([factorials[x] for x in str(i)])
        if i == sum_of_fact:
            res.append(i)

    return {"sum":sum(res), "numbers":res}






class Test(unittest.TestCase):

    def test_Digit_factorials(self):
        self.assertEqual(Digit_factorials(),{'sum': 40730, 'numbers': [145, 40585]})
if __name__ == '__main__':
    unittest.main()