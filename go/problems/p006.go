/* # The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first n natural
numbers and the square of the sum. */

package problems

func Sum_square_difference(n int) int {
	x := sum_of_squares(n)
	y := square_of_sums(n)
	return y - x
}

func sum_of_squares(n int) int {
	sum := 0
	for i := 1; i < n+1; i++ {
		sum += i * i
	}
	return sum
}

func square_of_sums(n int) int {
	sum := n * (n + 1) / 2
	return sum * sum
}

/*
there are also mathematical formulae for calculating
sum of n natural numbers = (n*(n+1)/2)**2
square of n natural numbers = (n*(n+1) * (2*n+1)/6)
*/
