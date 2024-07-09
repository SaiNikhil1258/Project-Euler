# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the given number? 


#  the intuition is to first find the 
def largest_prime_factor(number):
    """Return the largest prime factor of the given number."""
    # Find all the prime factors of the number.
    prime_factors = []
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime_factors.append(i)
            while number % i == 0:
                number //= i
    # If the number is prime, it is its own largest prime factor.
    if number > 1:
        prime_factors.append(number)
    # Return the largest prime factor.
    return max(prime_factors)

# remember that any composite number non prime can be expressed as a product of prime numbers
# to do that if number i is divisible by i even if i is not a prime number 
# i itself must be a product of smaller prime numbers to get the smaller prime factors you repeatedly divide it by i


# 6857
import unittest

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor_1(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_largest_prime_factor_2(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)

    def test_largest_prime_factor_3(self):
        self.assertEqual(largest_prime_factor(10), 5)

    def test_largest_prime_factor_4(self):
        self.assertEqual(largest_prime_factor(17), 17)

    def test_largest_prime_factor_5(self):
        self.assertEqual(largest_prime_factor(100), 5)

if __name__ == '__main__':
    unittest.main()
