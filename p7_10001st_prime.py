# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

# The output of this program is 104729. 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    i = 2
    while count < n:
        if is_prime(i):
            count += 1
        i += 1
    return i - 1

# print(nth_prime(10001))


import unittest


class Testnth_prime(unittest.TestCase):
    def test_nth_prime_1(self):
        self.assertEqual(nth_prime(6), 13)

    def test_nth_prime_2(self):
        self.assertEqual(nth_prime(10001), 104743)
    
    def test_nth_prime_3(self):
        self.assertEqual(nth_prime(1000), 7919)
        
    def test_nth_prime_4(self):
        self.assertEqual(nth_prime(100), 541)


if __name__ == '__main__':
    unittest.main()