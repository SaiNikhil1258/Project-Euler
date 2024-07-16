/* The following iterative sequence is defined for the set of positive integers:

 n → n/2 (n is even)
 n → 3n + 1 (n is odd)
 Using the rule above and starting with 13, we generate the following sequence:

 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
 It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

 Which starting number, under the given limit, produces the longest chain?

 Note: Once the chain starts the terms are allowed to go above limit. */

package problems

func len_sequence(n int) int {
	if n < 1 {
		return 0
	}
	i := 1
	for n != 1 {
		if n%2 == 0 {
			n /= 2
		} else {
			n = 3*n + 1
		}
		i++
	}
	return i
}

func Collatz(n int) int {
	maxLength := len_sequence(n)
	maxIndex := 0
	for i := 1; i < n; i++ {
		length := len_sequence(i)
		if length > maxLength {
			maxLength = length
			maxIndex = i
		}
	}
	return maxIndex
}
