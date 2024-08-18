# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.


"""The idea is to find all the abundant numbers < n
find the sum of all the abundant numbers without duplicates you will get a set of all the numbers that can be represented as the sum of 
abundant numbers 
You want an another set that has all the numbers from 1 to n
All the positive numbers that can be written as the sum of two abundant numbers will be the difference between them"""


def sum_proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return sum(set(divisors))


def abundant_numbers(n):
    abundant_numbers = []
    for i in range(1, n + 1):
        if sum_proper_divisors(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers


def non_abundant_sum(abundant_numbers, n):
    non_abundant = set(range(1, n))
    abundant_sums = set()
    for i in abundant_numbers:
        for j in abundant_numbers:
            abundant_sums.add(i + j)
    non_abundant -= abundant_sums
    return sum(non_abundant)


# print(non_abundant_sum(abundant_numbers(15000),15000))
import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(non_abundant_sum(abundant_numbers(10000), 10000), 3731004)

    def test_2(self):
        self.assertEqual(non_abundant_sum(abundant_numbers(15000), 15000), 4039939)

    def test_3(self):
        self.assertEqual(non_abundant_sum(abundant_numbers(20000), 20000), 4159710)

    def test_4(self):
        self.assertEqual(non_abundant_sum(abundant_numbers(28123), 28123), 4179871)


if __name__ == "__main__":
    unittest.main()
