/* # By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the nth prime number?

# The output of this program is 104729.  */

package problems

func Is_prime(n int) bool {
	if n <= 1 {
		return false
	} else if n <= 3 {
		return true
	} else if n%2 == 0 || n%3 == 0 {
		return false
	}
	i := 5
	for i*i <= n {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
		i += 6
	}
	return true
}

func Nth_prime(n int) int {
	count := 0
	i := 2
	for count < n {
		if Is_prime(i) {
			count++
		}
		i++
	}
	return i - 1
}
