# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:

# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can n pence be made using any number of coins?



coins = [1, 2, 5, 10, 20, 50, 100, 200]

def change(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin,n+1):
            dp[i] += dp[i-coin]
    return dp[n]
# print(change(200))

import unittest

class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(change(200), 73682)

    def test_2(self):
        self.assertEqual(change(50), 451)
    
    def test_3(self):
        self.assertEqual(change(100),4563)

    def test_4(self):
        self.assertEqual(change(150),21873)


if __name__ == '__main__':
    unittest.main()














