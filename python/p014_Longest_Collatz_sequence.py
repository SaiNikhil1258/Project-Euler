# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under the given limit, produces the longest chain?

# Note: Once the chain starts the terms are allowed to go above limit.


# using a while true loop initialize if n is odd then perform 3n+1 if it is odd then perform n/2


import unittest

def len_sequence(n):
    if n < 1:
        return 0
    i = 1
    while n != 1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n + 1
            
        i += 1
    return i


def collatz(n):
    for i in range(1,n):
        if len_sequence(i) > len_sequence(n):
            n = i
    return n



# print(collatz(10))


class TestCollatz(unittest.TestCase):
    def test_collatz(self):
        self.assertEqual(collatz(10), 9)
        
    def test_collatz_2(self):
        self.assertEqual(collatz(14), 9)
    
    # ** this takes a long time    
    # def test_collatz_3(self):
    #     self.assertEqual(collatz(1000000), 837799)
    
    def test_collatz_4(self):
        self.assertEqual(collatz(5847),3711)
    
    def test_collatz_5(self):
        self.assertEqual(collatz(54512),52527)


if __name__ == '__main__':
    unittest.main()


