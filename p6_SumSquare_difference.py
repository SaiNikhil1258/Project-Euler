# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.

def sum_square_difference(n):
    """the sum of squares of the first n natural numbers and the square of the sum

    Args:
        n (int): a number

    Returns:
        int: the difference between the sum of squares of n natural numebers and the square of the sum
    this is the iterative approach
    """
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n+1):
        sum_of_squares += i**2
        square_of_sum += i
    square_of_sum **= 2
    return square_of_sum - sum_of_squares


# n * (n + 1) * (2n + 1) / 6 for the sum of squares of n natural numbers
# n (n + 1) / 2) for the sum of n natural numbers
# n (n + 1) / 2)**2 for the sum of squares of n natural numbers  

# Using mathematical formulae

def sum_square_difference_math(n):
    return (n * (n + 1) / 2)**2 - (n * (n + 1) * (2*n + 1) / 6)  

# print(sum_square_difference_math(20))



import unittest

class TestSumSquareDifference(unittest.TestCase):
    def test_sum_square_difference(self):
        self.assertEqual(sum_square_difference(10), 2640)
        self.assertEqual(sum_square_difference(20), 41230)
        self.assertEqual(sum_square_difference(100), 25164150)
        
    def test_sum_square_difference_math(self): 
        self.assertEqual(sum_square_difference_math(10), 2640)
        self.assertEqual(sum_square_difference_math(20), 41230)
        self.assertEqual(sum_square_difference_math(100), 25164150)



if __name__ == '__main__':
    unittest.main()     
