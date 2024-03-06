# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1000000, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def decimal_to_binary(n):
    return bin(n)[2:]

def is_palindrome(n):
    return str(n) == str(n)[::-1]


def Double_base_palindromes(n):
    sum = 0
    for i in range(n):
        if is_palindrome(i) and is_palindrome(decimal_to_binary(i)):
           sum += i 
    return sum
# print(Double_base_palindromes(1000000))


import unittest

class Test(unittest.TestCase):

    def test_Double_base_palindromes(self):
        self.assertEqual(Double_base_palindromes(1000000), 872187)

    def test_Double_base_palindromes_2(self):
        self.assertEqual(Double_base_palindromes(1000), 1772)

    def test_Double_base_palindromes_3(self):
        self.assertEqual(Double_base_palindromes(50000), 105795)

    def test_Double_base_palindromes_4(self):
        self.assertEqual(Double_base_palindromes(500000), 286602)




if __name__ == '__main__':
    unittest.main()