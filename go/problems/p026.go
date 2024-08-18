/*
A unit fraction contains 1 in the numerator. The decimal representation of the unit
fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that
1/7 has a 6-digit recurring cycle.

Find the value of d < n for which 1/d contains the longest recurring cycle in its
decimal fraction part.
*/

package problems

// for every number below n you find the cycle_length of the 1/n & compare it with the max
// and return the max cycle
func Max_reciprocal_cycle_length() int {
	n := 1000
	max_cycle_length := 0
	max_cycle_d := 0
	for i := 2; i < n; i++ {
		cycle_length := get_cycle_length(i)
		if cycle_length > max_cycle_length {
			max_cycle_length = cycle_length
			max_cycle_d = i
		}
	}
	return max_cycle_d
}

// Keeps track of the remainders of the division and returns the length of the cycle if
// cycle is found
func get_cycle_length(d int) int {
	remainders := []int{}
	remainder := 1
	for {
		for i, r := range remainders {
			if r == remainder {
				return len(remainders) - i
			}
		}
		// add 1 to the list and then and then keep on multiplying the remainder with 10
		// and find the % modulo to that with the "d" for quotient
		remainders = append(remainders, remainder)
		remainder *= 10 // multiply the remainder with 10
		remainder %= d  // modulo with the 10 to get the quotient(divisors)
	}
}
