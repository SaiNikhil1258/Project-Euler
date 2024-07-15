package problems

import "math"

func Count_of_factors(n int) int {
	count := 2
	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if n%i == 0 {
			count++
			if i*i != n {
				count++
			}
		}
	}
	return count
}

func Highly_divisible_triangular_number(i int) int {
	n := 1
	for {
		triangular_number := n * (n + 1) / 2
		if Count_of_factors(triangular_number) >= i {
			return triangular_number
		}
		n++
	}
}
