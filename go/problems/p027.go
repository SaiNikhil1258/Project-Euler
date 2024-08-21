/*
Euler discovered the remarkable quadratic formula:

n2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values
0≤n≤39. However, when  n=40,402+40+41=40(40+1)+41
  is divisible by 41, and certainly when  n=41,412+41+41
  is clearly divisible by 41.

The incredible formula  n2−79n+1601
  was discovered, which produces 80 primes for the consecutive values  0≤n≤79
 . The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where  |a|<range and  |b|≤range

where  |n| is the modulus/absolute value of  n

e.g.  |11|=11 and  |−4|=4

Find the product of the coefficients,  a and  b, for the quadratic expression
that produces the maximum number of primes for consecutive values of  n, starting with
n=0
*/

package problems

// For all the possible values of n (-n to +n) for a and b for those a and b we find
// the quedratic primes with value of n upto 79 from n = 0 we keep track of current
// consecutive primes for this values of a and b if the current_primes is greater than
// the max_primes then we would update the max_consecutive primes nuber and update the
// value of a and b to hold the best value until now
func Quadratic_primes() int {
	max_range := 1000
	max_a := max_range
	max_b := max_range
	max_n := 79
	max_primes, best_a, best_b := 0, 0, 0
	for a := -max_a; a < max_a+1; a++ {
		for b := -max_b; b < max_b+1; b++ {
			current_primes := 0
			for n := 0; n < max_n+1; n++ {
				if Is_prime(n*n + a*n + b) {
					current_primes++
				} else {
					break
				}
			}
			if current_primes > max_primes {
				max_primes = current_primes
				best_a = a
				best_b = b
			}
		}
	}
	return best_a * best_b
}
