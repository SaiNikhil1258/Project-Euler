# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def multiples_of_3_or_5(number):
    multiples = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return sum(multiples)

# print(multiples_of_3_or_5(100))


# 233168    
import unittest

class TestMultiplesOf3Or5(unittest.TestCase):

    def test_multiples_of_3_or_5_1(self):
        self.assertEqual(multiples_of_3_or_5(10), 23)

    def test_multiples_of_3_or_5_2(self):
        self.assertEqual(multiples_of_3_or_5(8456), 16687353)

    def test_multiples_of_3_or_5_3(self):
        self.assertEqual(multiples_of_3_or_5(1000), 233168)

    def test_multiples_of_3_or_5_4(self):
        self.assertEqual(multiples_of_3_or_5(49), 543)

    def test_multiples_of_3_or_5_5(self):
        self.assertEqual(multiples_of_3_or_5(19564), 89301183)

if __name__ == '__main__':
    unittest.main()


# multiples_of_3_or_5(1000) should return 233168
# multiples_of_3_or_5(49) should return 543
# multiples_of_3_or_5(19564) should return 89301183