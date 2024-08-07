# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

# What is the largest n-length digit pandigital prime that exists?

import unittest


def is_prime(n):
    if n <= 1:
        return False

    elif n <= 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False

        i += 6
    return True


def pandigital_prime(digit):
    # Note: The only 1-digit pandigital number is 1, which is not prime. Thus we require n >= 2.
    for n in reversed(range(2, digit+1)):
        arr = list(reversed(range(1, n + 1)))
        while True:
            if arr[-1] not in NONPRIME_LAST_DIGITS:
                n = int("".join(str(x) for x in arr))
                # print(n)
                if is_prime(n):
                    return n
            if not prev_permutation(arr):
                break
    raise AssertionError()


NONPRIME_LAST_DIGITS = {0, 2, 4, 5, 6, 8}


def prev_permutation(arr):
    # this funciton will get the next maximum permutations
    i = len(arr) - 1
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(arr) - 1
    while arr[j] >= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    print(arr)
    return True


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(pandigital_prime(4), 4231)

    def test_2(self):
        self.assertEqual(pandigital_prime(7), 7652413)


if __name__ == "__main__":
    unittest.main()


# brute force solution


# def pandigital_primes(digit):
#     string = "".join(str(i) for i in sorted(set(range(1, digit+1))))
#     # create a pandigital number of n digits
#     result = []
#     list_of_primes = find_primes(10**digit)
#     for num in list_of_primes:
#         if "".join(sorted(str(num))) == string:
#             result.append(num)
#     return max(result)


# def find_primes(n):
#     primes = []
#     for num in range(2, n):
#         if is_prime(num):
#             primes.append(num)
#     return primes
