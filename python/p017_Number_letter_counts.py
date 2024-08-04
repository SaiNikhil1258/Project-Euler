# Problem 17: Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
# used in total.
# If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


import unittest

# x = "".join(char for char in txt if char not in ",- ")


def number_letter_counts(n):
    res = []
    for i in range(1, n + 1):
        res.append(p.number_to_words(i))

    sum = 0
    for i in res:
        sum += len("".join(char for char in i if char not in ",- "))
        # print(f"{i}: {sum}")

    return sum


# print(number_letter_counts(100)) --> 864


class Test(unittest.TestCase):
    def test_number_letter_counts(self):
        self.assertEqual(number_letter_counts(1000), 21124)

    def test_number_letter_counts_2(self):
        self.assertEqual(number_letter_counts(5), 19)

    def test_number_letter_counts_3(self):
        self.assertEqual(number_letter_counts(100), 864)

    def test_number_letter_counts_4(self):
        self.assertEqual(number_letter_counts(150), 1903)


if __name__ == "__main__":
    unittest.main()
