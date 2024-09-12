/*
Surprisingly there are only three numbers that can be written as the sum of fourth
powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of n powers of their
digits.
*/
package problems

import (
	"math"
)

func Digit_power() int {
	n := 5
	results := []int{}
	for i := 2; i < int(math.Pow10(n+1)); i++ {
		if i == digit_power(i, n) {
			results = append(results, i)
		}
	}
	sum := 0
	for _, x := range results {
		sum += x
	}
	return sum
}

func digit_power(i, n int) int {
	sum := 0
	for i > 0 {
		digit := i % 10
		sum += int(math.Pow(float64(digit), float64(n)))
		i /= 10
	}
	return sum
}
