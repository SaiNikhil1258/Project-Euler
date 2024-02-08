# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.


def pythagorean_triplet(n):
    triplets_product = []
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                # print(a, b, c)
                triplets_product.append(a*b*c)
# another list because for some n values there are multiple triplets so we append all the triplets into a list and return the list
    return triplets_product




# print(pythagorean_triplet(120))
import unittest

class Testpythagorean_triplet(unittest.TestCase):
    
    def test_pythagorean_triplet_1(self):
        self.assertEqual(pythagorean_triplet(1000), [31875000])
        
    def test_pythagorean_triplet_2(self):
        self.assertEqual(pythagorean_triplet(24), [480])
        
    # write a test case for n = 120
    def test_pythagorean_triplet_3(self):
        self.assertEqual(pythagorean_triplet(120), [49920,55080,60000])
        


if __name__ == '__main__':
    unittest.main()