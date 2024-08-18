/*
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide
evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under n.

Approach amicable numbers are such that sum of proper divisors of a = b and sum of
proper divisors of b = a
such numbers a, b are called as amicable numbers
you need a dictionary to store the sum of proper divisors of each number
there are some self amicable numbers
in the for loop for i = 220 the values of a and b will be
a = 284, b = 220
to remove the self amicable numbers we need to check if i != b

 Approach 2 you can calculate all the divisors sum once and store them in a auxillary
array */

package problems

func Sum_Amicable_numbers() int {
	n := 10000
	amicable_numbers := 0
	for i := 2; i < n; i++ {
		a := sum_proper_divisors(i)
		b := sum_proper_divisors(a)
		if i == b && i != a {
			amicable_numbers += i
		}
	}
	return amicable_numbers
}

func sum_proper_divisors(n int) int {
	sum := 1
	for i := 2; i <= (n/2)+1; i++ {
		if n%i == 0 {
			sum += i
		}
	}
	return sum
}
