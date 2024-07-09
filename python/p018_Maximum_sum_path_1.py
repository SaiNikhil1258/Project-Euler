# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force,
# and requires a clever method! ;o)


# you create a 2d array of same dimensions as the input array adn traverse it from the bottom to top i.e., reverse order
# for you to have the max sum path you need base since you cannot add more numbers to the bottom you keep the bottom row as same
# At each element [i][j], calculate the maximum possible sum by comparing the sums achievable from its two adjacent elements below
# and update the element as the max sum and repeat the process upto the top at the top you will have the max sum 


triangle = [  # Mutable
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20, 4,82,47,65],
	[19, 1,23,75, 3,34],
	[88, 2,77,73, 7,63,67],
	[99,65, 4,28, 6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
	[ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23],
]


arr = [
    [3],
    [7, 4],
    [2, 4, 6],
    [8, 5, 9, 3]
]
#  for this array you will get the output array as
# [
#     [23],
#     [20, 19],
#     [10, 13, 15],
#     [8, 5, 9, 3],
# ] returning the [0][0] since it will be the max path sum



def max_path_sum(triangle):
    """returns the max sum path in the given triangle

    Args:
        triangle (2d_array): a 2 dimensional array

    Returns:
        int: returns the maximum sum path in the given triangle
    """
    if len(triangle) == 1:
        return triangle[0][0] # Base case: single element triangle
    for i in range(len(triangle)-2,-1,-1):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
            
    return triangle[0][0]
#    "# if you dont want to csmodify the array you can use another array similar in dimensions to the input array"


import unittest

class Test(unittest.TestCase):
    
    def test_max_path_sum(self):
        self.assertEqual(max_path_sum(arr), 23)
    
    def test_max_path_sum_2(self):
        self.assertEqual(max_path_sum(triangle), 1074)
        
        
if __name__ == '__main__':
    unittest.main()

