package problems

import "math"

func Largest_prime_factor(num int) int {
	prime_factors := []int{}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			prime_factors = append(prime_factors, i)
			for num%i == 0 {
				num /= i
			}
		}
	}
	if num > 1 {
		prime_factors = append(prime_factors, num)
	}

	if len(prime_factors) == 0 {
		return 0
	}
	max := prime_factors[0]
	for _, element := range prime_factors {
		if element > max {
			max = element
		}
	}
	return max
}
