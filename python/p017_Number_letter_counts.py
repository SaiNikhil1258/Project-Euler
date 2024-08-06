# Problem 17: Number letter counts
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
# used in total.
# If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


import unittest

# x = "".join(char for char in txt if char not in ",- ")


def number_letter_counts(n):
    ans = sum(len(to_english(i)) for i in range(1,1001))
    return str(ans)

def to_english(n):
    if 0 <= n < 20:
		return ONES[n]
	elif 20 <= n < 100:
		return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return ONES[n // 100] + "hundred" + (("and" + to_english(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return to_english(n // 1000) + "thousand" + (to_english(n % 1000) if (n % 1000 != 0) else "")
	else:
		raise ValueError()


ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


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
