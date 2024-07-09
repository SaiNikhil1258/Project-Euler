package main

import (
	"fmt"
	"project-euler/problems"
)

func main() {
	p1 := problems.Natural(10)
	fmt.Println("Result of P001:", p1)
	p2 := problems.Fib_n_natural(34)
	fmt.Println("Result of P002:", p2)
	p3 := problems.Largest_prime_factor(13195)
	fmt.Println("Result of P003:", p3)
	p4 := problems.Largest_palindrome(3)
	fmt.Println("Result of P004:", p4)
	p5 := problems.Smallest_multiple(10)
	fmt.Println("Result of P005:", p5)
	p6 := problems.Sum_square_difference(20)
	fmt.Println("Result of P006:", p6)
	p7 := problems.Nth_prime(10001)
	fmt.Println("Result of P007:", p7)

}
