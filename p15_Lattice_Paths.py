# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a given gridSize?



# this problem has a direct formula to get the answer it uses combinations

# if n is the size of the grid then the number of paths is about (2*n)combination n

# 2*n comb n

# consider a 10x10 grid

# In this grid you have 10 down moves and 10 right moves 
# the set of moves has 20 moves(10 down and 10 right)
# and from this set of 20 moves we only need 10 moves of any order for us to reach from top left to bottom right

# to get this we have a formula Binomial coefficients

# Binomial Coefficients represent the number of ways to choose k elements from a set of n elements regardless of order is 
# this combinations formula in python is comb from the math module
# nCk = n! / (k! * (n-k)!)
# 20C10 = 20! / (10! * (20-10)!)
# this will get the number of possible paths to reach from the top left to the bottom right

import math
import unittest


def lattice_paths(gridSize):
    return math.comb(2*gridSize, gridSize)


class Test(unittest.TestCase):
    
    def test_lattice_paths(self):
        self.assertEqual(lattice_paths(2), 6)
    
    def test_lattice_paths_2(self):
        self.assertEqual(lattice_paths(20), 137846528820)
        
    def test_lattice_paths_3(self):
        self.assertEqual(lattice_paths(9), 48620)


if __name__ == '__main__':
    unittest.main()            


# print(lattice_paths(20))
