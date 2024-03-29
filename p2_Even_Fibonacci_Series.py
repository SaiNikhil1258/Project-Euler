# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.

def even_fibonacci_series(n):
    """sum of the even fibonacci series

    Args:
        n(int): given a number 

    Returns:
        int: the sum of the even numbers in the fibonacci series 
    """
    
    fib_sequence = [1, 2]
    while fib_sequence[-1] < n:
        next_number = fib_sequence[-2] + fib_sequence[-1]
        fib_sequence.append(next_number)
    even_fib_sum = 0
    for number in fib_sequence:
        if number % 2 == 0:
            even_fib_sum += number
    return even_fib_sum



# 4613732
import unittest

class TestEvenFibonacciSeries(unittest.TestCase):

    def test_even_fibonacci_series_1(self):
        self.assertEqual(even_fibonacci_series(10), 10)

    def test_even_fibonacci_series_2(self):
        self.assertEqual(even_fibonacci_series(34), 44)

    def test_even_fibonacci_series_3(self):
        self.assertEqual(even_fibonacci_series(60), 44)

    def test_even_fibonacci_series_4(self):
        self.assertEqual(even_fibonacci_series(1000), 798)
    
    def test_even_fibonacci_series_5(self):
        self.assertEqual(even_fibonacci_series(4000000), 4613732)



if __name__ == '__main__':
    unittest.main()


# when you run test cases from a separate file the if condition evaluates to false because the test file is being imported when it is imported the name
# becomes the name of the module thus running the test cases 

# Remove the if __name__ == '__main__': block: This allows the tests to run regardless of whether the file is imported or executed directly. 
# However, be cautious using this approach as it might lead to unintended test runs during imports.


