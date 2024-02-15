# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain n digits?


def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        
    return a

# print(len(fibonacci(9)))

def find_nth_digit_fibonacci(n):
    i = 0
    while True:
        fib = fibonacci(i)
        fib_length = len(str(fib))
        
        if fib_length == n:
            return i
        elif fib_length > n:
            break
        i += 1
    return -1

# print(find(15))

import unittest

class Test(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(find_nth_digit_fibonacci(5),21)
        
    def test_2(self):
        self.assertEqual(find_nth_digit_fibonacci(10),45)
        
    def test_3(self):
        self.assertEqual(find_nth_digit_fibonacci(15),69)
        
    def test_4(self):
        self.assertEqual(find_nth_digit_fibonacci(20),93)
        
if __name__ == '__main__':
    unittest.main()


