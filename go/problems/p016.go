/* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2exponent? */

package problems

import (
	"math/big"
	"strconv"
)

// NOTE: since this problem invloves larger number we have to use the math/big module for precise calculations
// convert the large numbers into string to get the sum of the digits

func sum_of_digits(s string) uint64 {
	sum := uint64(0)
	for _, c := range s {
		n, _ := strconv.Atoi(string(c))
		sum += uint64(n)
	}
	return sum
}

func Power_digit_sums() uint64 {
	n := new(big.Int)
	n.Exp(big.NewInt(2), big.NewInt(1000), nil)
	res := sum_of_digits(n.String())
	return res
}
