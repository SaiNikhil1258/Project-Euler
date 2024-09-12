/*
In England the currency is made up of pound, £, and pence, p, and there are eight
coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can n pence be made using any number of coins?
*/

package problems

var coins = []int{1, 2, 5, 10, 20, 50, 100, 200}

func Change() int {
	n := 200
	dp := make([]int, n+1)
	dp[0] = 1
	for _, coin := range coins {
		for i := coin; i < n+1; i++ {
			dp[i] += dp[i-coin]
		}
	}
	return dp[n]
}
