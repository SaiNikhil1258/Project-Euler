/* # A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two n-digit numbers. */

package problems

import (
	"fmt"
	"math"
	"strconv"
)

func is_palindrome(i int64) bool {
	s := strconv.FormatInt(i, 10)
	i, j := int64(0), int64(len(s)-1)
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}

func Largest_palindrome(n int64) int64 {
	max_num, min_num := math.Pow(10, float64(n))-1, math.Pow(10, float64(n-1))
	res := int64(0)
	fmt.Println("before: ", res)
	for i := max_num; i > min_num; i-- {
		if i*max_num < float64(res) {
			fmt.Println("the res value is:", res)
			break
		}
		for j := i; j > min_num; j-- {
			product := int64(i * j)
			if product < res {
				break
			}
			if is_palindrome(product) {
				res = int64(math.Max(float64(res), float64(product)))
			}
		}
	}
	return res
}

/*
We need to find the largest n digit palindrome number so we can do this with reverse looping

we run two loops and we run if their product is palindrome or not
*/
