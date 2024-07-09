/* # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n? */

package problems

func compute_gcd(x, y int) int {
	for y > 0 {
		x, y = y, x%y
	}
	return x
}

func compute_lcm(x, y int) int {
	lcm := (x * y) / compute_gcd(x, y)
	return lcm
}

func Smallest_multiple(n int) int {
	lcm := 1
	for i := 1; i < n+1; i++ {
		lcm = compute_lcm(lcm, i)
	}
	return lcm
}
