# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two n-digit numbers.




def largest_palindrome_product(n):
    max_num = 10**n-1
    min_num = 10**(n-1)
    max_palindrome = 0
    for i in range(max_num, min_num-1, -1):
        if i*max_num < max_palindrome:
            break
        for j in range(i, min_num-1, -1): 
# you can also set the upper bound as max(min_num,i-100) or something like that 
# to have lower checks and for better efficiency but it doesn't seem to be working
            product = i*j
            if product < max_palindrome:
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = max(max_palindrome, product)
    return max_palindrome


import unittest

class TestLargestPalindromeProduct(unittest.TestCase):

    def test_largest_palindrome_product_2(self):
        self.assertEqual(largest_palindrome_product(2), 9009)

    def test_largest_palindrome_product_3(self):
        self.assertEqual(largest_palindrome_product(3), 906609)

    def test_largest_palindrome_product_4(self):
        self.assertEqual(largest_palindrome_product(4), 99000099)

    def test_largest_palindrome_product_5(self):
        self.assertEqual(largest_palindrome_product(5), 9966006699)



if __name__ == '__main__':
    unittest.main()


# print(largest_palindrome_product(5))




