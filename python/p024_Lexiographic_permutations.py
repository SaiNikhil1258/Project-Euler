# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210
# What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


import unittest
from itertools import permutations

numbers = list(range(10))


def nth_lexicographic_permutation(lst, n):
    # This will generate all the possible permutations of the given list
    permutations_list = list(permutations(lst))
    number = permutations_list[n]
    result = int("".join(str(x) for x in number))
    return result


class Test(unittest.TestCase):

    def test_699999(self):
        self.assertEqual(nth_lexicographic_permutation(numbers, 699999), 1938246570)

    def test_899999(self):
        self.assertEqual(nth_lexicographic_permutation(numbers, 899999), 2536987410)

    def test_900000(self):
        self.assertEqual(nth_lexicographic_permutation(numbers, 900000), 2537014689)

    def test_999999(self):
        self.assertEqual(nth_lexicographic_permutation(numbers, 999999), 2783915460)


if __name__ == "__main__":
    unittest.main()


"""recursive function"""

# # Python function to print permutations of a given list
# def permutation(lst):
#     if len(lst) == 0:
#         return []

#     # If there is only one element in lst then, only
#     # one permutation is possible
#     if len(lst) == 1:
#         return [lst]

#     # Find the permutations for lst if there are
#     # more than 1 characters

#     l = [] # empty list that will store current permutation

#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#        m = lst[i]

#        # Extract lst[i] or m from the list.  remLst is
#        # remaining list
#        remLst = lst[:i] + lst[i+1:]

#        # Generating all permutations where m is first
#        # element
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l
