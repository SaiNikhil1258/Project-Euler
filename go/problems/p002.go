package problems

func Fib_n_natural(n int) int {
	res := 0
	fib := []int{1, 1, 2}
	for fib[2] < n {
		if fib[2]%2 == 0 {
			res += fib[2]
		}
		fib[0] = fib[1]
		fib[1] = fib[2]
		fib[2] = fib[0] + fib[1]

	}
	return res
}
