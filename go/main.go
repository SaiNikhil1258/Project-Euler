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
	p11 := problems.Largest_product_in_grid()
	fmt.Println("Result of P011:", p11)
	p12 := problems.Highly_divisible_triangular_number(500)
	fmt.Println("Result of P012:", p12)
	p13 := problems.Large_sum(10)
	fmt.Println("Result of P013:", p13)
	p14 := problems.Collatz(14)
	fmt.Println("Result of p014:", p14)
	p15 := problems.Lattice_paths()
	fmt.Println("Result of p015:", p15)
	p16 := problems.Power_digit_sums()
	fmt.Println("Result of p016:", p16)
	p17 := problems.Number_letter_count(1000)
	fmt.Println("Result of p017:", p17)
	p18 := problems.Max_path_sum()
	fmt.Println("Result of p018:", p18)
	p19 := problems.Sunday()
	fmt.Println("Result of p019:", p19)
	p20 := problems.Sum_factorial_Digits()
	fmt.Println("Result of p020:", p20)
	p21 := problems.Sum_Amicable_numbers()
	fmt.Println("Result of p021:", p21)
	p22 := problems.Name_Score()
	fmt.Println("Result of p022:", p22)
	p23 := problems.Non_abundant_Numbers_sum()
	fmt.Println("Result of p023:", p23)
	p24 := problems.Nth_lexiographical_permutation()
	fmt.Println("Result of p024:", p24)
	p25 := problems.Find_nth_digit_fibonacci_number()
	fmt.Println("Result of p025:", p25)
	p26 := problems.Max_reciprocal_cycle_length()
	fmt.Println("Result of p026:", p26)
	p27 := problems.Quadratic_primes()
	fmt.Println("Result of p027", p27)
	p28 := problems.Sum_of_spiral_diagonal()
	fmt.Println("Result of p028:", p28)
	p29 := problems.Distant_powers()
	fmt.Println("Result of p029:", p29)
	p30 := problems.Digit_power()
	fmt.Println("Result of p30:", p30)
	p31 := problems.Change()
	fmt.Println("Result of p031:", p31)
	p32 := problems.Pandigital_products()
	fmt.Println("Result of p032:", p32)
	p33 := problems.Digit_cancelling_numbers()
	fmt.Println("Result of p033:", p33)
	p34, p034 := problems.Digit_factorials()
	fmt.Println("Result of p034:", p34, p034)
	p35 := problems.CircularPrimes()
	fmt.Println("Result of p035:", p35)
	p36 := problems.Double_base_palindrome(1000)
	fmt.Println("Result of p036:", p36)
	y := time.Since(x)
	fmt.Println("The time taken is", y)
	// This time since will get the time it has been since the time stamp x
}
