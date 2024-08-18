package problems

import "strconv"

var fibMap = make(map[int]int)

func Fibonacci(n int) int {
	if n <= 1 {
		return n
	}
	if val, ok := fibMap[n]; ok {
		return val
	}
	fibMap[n] = Fibonacci(n-1) + Fibonacci(n-2)
	return fibMap[n]
	// a, b := 0, 1
	// i := 0
	// for i < n {
	// 	a, b = b, a+b
	// 	i++
	// }
	// return a
}

func Find_nth_digit_fibonacci_number() int {
	n := 20
	i := 0
	for {
		fib := Fibonacci(i)
		fib_length := len(strconv.Itoa(fib))
		if fib_length == n {
			return i
		} else if fib_length > n {
			break
		}
		i++
	}
	return -1
}
