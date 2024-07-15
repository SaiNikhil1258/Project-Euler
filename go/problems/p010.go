package problems

func Summation_of_primes(n int) int {
	sum := 0
	for i := 1; i < n; i++ {
		if Is_prime(i) {
			sum += i
		}
	}
	return sum
}
