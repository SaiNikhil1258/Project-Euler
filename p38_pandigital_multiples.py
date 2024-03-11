# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192×1=192192×2=384192×3=576
 
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

# What is the largest 1 to k pandigital k-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?

import unittest

def pandigital_multiples(digit):
    string = "".join(str(i) for i in sorted(set(range(1,digit+1))))
    # create a pandigital number of n digits
    ans = ""
    # we need the multiples from 2 to 9
    for n in range(2,10):
        for i in range(1,10**(digit//n)):
            # this will keep the upper limit to be under the 9 digit limit
            s = "".join(str(i*j) for j in range(1,n+1))
            if "".join(sorted(s)) == string:
                ans = max(ans, s)
    return ans




class Test(unittest.TestCase):
    def test_pandigital_multiples(self):
        self.assertEqual(pandigital_multiples(8), "78156234")
        self.assertEqual(pandigital_multiples(9), "932718654")

if __name__ == "__main__":
    unittest.main()
