/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits n!
*/

package problems

import (
	"math/big"
)

func factorial(n int) *big.Int {
	sum := big.NewInt(1)
	for i := 1; i <= n; i++ {
		temp := big.NewInt(int64(i))
		sum = sum.Mul(sum, temp)
	}
	return sum
}

func Sum_factorial_Digits() int {
	// i, j := big.NewInt(1), big.NewInt(1)
	// for j.Cmp(big.NewInt(25)) != 0 {
	// 	j.Add(j, big.NewInt(1))
	// 	i.Mul(i, j)
	// }
	i := factorial(100) // 100 -> 468
	return int(sum_of_digits(i.String()))
}
