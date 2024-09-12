/*
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79,
and 97.

How many circular primes are there below n, whereas 100 ≤ n ≤ 1000000?

Note:
Circular primes individual rotation can exceed n
*/

package problems

import (
	"math"
	"strconv"
)

// in the given range of n returns the primes array in []bools
func Primes_in_given_range(n int) []bool {
	primes := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		primes[i] = true
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if primes[i] {
			for j := i * i; j <= n; j += i {
				primes[j] = false
			}
		}
	}
	return primes
}

func isCircularPrime(n int, primes []bool) bool {
	s := strconv.Itoa(n)
	length := len(s)
	for i := 0; i < length; i++ {
		rotated, _ := strconv.Atoi(s[i:] + s[:i])
		if !primes[rotated] {
			return false
		}
	}
	return true
}

func CircularPrimes() int {
	n := 1000000
	primes := Primes_in_given_range(n)
	count := 0
	for i := 2; i < n; i++ {
		if primes[i] && isCircularPrime(i, primes) {
			count++
		}
	}
	return count
}
