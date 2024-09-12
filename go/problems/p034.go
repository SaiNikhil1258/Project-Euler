/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the numbers and the sum of the numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
you can just brute force for the solution
a small addition of storing the factorials of 0 through 9
this will improve the speed
*/

package problems

import "strconv"

func fact(n int) int {
	if n == 0 {
		return 1
	}
	result := 1
	for i := 2; i <= n; i++ {
		result *= i
	}
	return result
}

func Digit_factorials() (int, []int) {
	factorials := make(map[string]int)
	for i := 0; i < 10; i++ {
		factorials[strconv.Itoa(i)] = fact(i)
	}
	res := []int{}
	totalSum := 0
	for i := 3; i < 10000000; i++ {
		sum_of_fact := 0
		strNum := strconv.Itoa(i)
		for _, digit := range strNum {
			sum_of_fact += factorials[string(digit)]
		}
		if i == sum_of_fact {
			res = append(res, i)
			totalSum += i
		}
	}
	return totalSum, res
}
