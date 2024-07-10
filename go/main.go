package main

import (
	"fmt"
	"project-euler/problems"
	"time"
)

func main() {

  x := time.Now()
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

	p8 := problems.Largest_product_in_a_series(13)
	fmt.Println("Result of P008:", p8)
	p9 := problems.Pythagorean_triplets(120)
	fmt.Println("Result of P009:", p9)
	p10 := problems.Summation_of_primes(2000000)
	fmt.Println("Result of P010:", p10)
	y := time.Since(x)
	fmt.Println("The time taken is", y)
}
