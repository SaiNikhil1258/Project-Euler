/* # A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc such that a + b + c = n. */

package problems

import "math"

func Pythagorean_triplets(n int) []int {
	triplets := []int{}
	for x := 1; x < n; x++ {
		for y := x; y < n; y++ {
			z := n - x - y
			if (math.Pow(float64(x), 2) + math.Pow(float64(y), 2)) == math.Pow(float64(z), 2) {
				triplets = append(triplets, x*y*z)
			}
		}
	}
	return triplets[:]
}
