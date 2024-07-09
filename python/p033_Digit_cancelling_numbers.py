# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly 
# believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
# result = []
# numbers = sorted(set(range(10,100)))
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if i/j == (i//10)/j%10:
#             result.append(i/j) 

# print(result)
def compute():
    nums = []
    dens = []
    for i in range(10,100):
        for j in range(i+1,100):
            num = i//10
            cmn1 = i%10
            den = j%10
            cmn2 = j //10

            if den != 0 and  (i /j) == (num/den) and (cmn1== cmn2):
                # print(i,j)
                # print(num, cmn1, den, cmn2)
                if den % num == 0:
                    den = den // num
                    num = 1
                nums.append(num)
                dens.append(den)
    x = 1
    y =1
    for i in nums:
        x *= i
    for i in dens:
        y *= i
    return y//x



import unittest


class Test(unittest.TestCase):
    def test_compute(self):
        self.assertEqual(compute(), 100)

if __name__ == "__main__":
    unittest.main()