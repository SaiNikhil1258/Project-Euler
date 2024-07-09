# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below n.

def is_prime(n):
    """
    Return True if n is prime, False otherwise.
    """

    # If n is 1, it is not prime.
    if n == 1:
        return False

    # Iterate over all numbers from 2 to the square root of n.
    for i in range(2, int(n ** 0.5) + 1):
        # If n is divisible by any number from 2 to its square root, it is not prime.
        if n % i == 0:
            return False

    # If n is divisible by no number from 2 to its square root, it is prime.
    return True

def sum_primes(n):
    """
    Return the sum of all the primes below n.
    """

    # Initialize the sum to 0.
    sum = 0 

    # Iterate over all numbers from 2 to n.
    for i in range(2, n):
        # If i is prime, add it to the sum.     
        if is_prime(i):
            sum += i

    # Return the sum.
    return sum

# Print the sum of all the primes below 10.
# print(sum_primes(17))



import unittest

class Testsum_primes(unittest.TestCase):
    
    def test_sum_primes_1(self):
        self.assertEqual(sum_primes(17),41)
        
    def test_sum_primes_3(self):
        self.assertEqual(sum_primes(2001),277050)
    
    def test_sum_primes_4(self):
        self.assertEqual(sum_primes(140759),873608362)
    
    def test_sum_primes_5(self):
        self.assertEqual(sum_primes(2000000),142913828922)


if __name__=='__main__':
    unittest.main()