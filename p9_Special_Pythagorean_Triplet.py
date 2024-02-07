# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.

# The output of this program is 31875000.

def find_triplet(n):
    """Finds the pythagorean triplet for which a + b + c = n and returns the product abc

    Args:
        n (int): integer for which a + b + c = n

    Returns:
        _type_: the product abc for which a + b + c = n
    """
    for a in range(1, n // 3):
        for b in range(a + 1, n // 2):
            c = n - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

print(find_triplet(100))

# print(200**2)
# print(300**2)
# print(500**2)

# import unittest


# class Testfind_triplet(unittest.TestCase):
#     def test_find_triplet_1(self):
#         self.assertEqual(find_triplet(1000), 31875000)

#     def test_find_triplet_2(self):
#         self.assertEqual(find_triplet(100), 3750)

#     def test_find_triplet_3(self):
#         self.assertEqual(find_triplet(10), 30)


# if __name__ == '__main__':
#     unittest.main()