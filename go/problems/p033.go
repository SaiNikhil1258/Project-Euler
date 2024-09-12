/*
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly
believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one
in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
result = []
numbers = sorted(set(range(10,100)))
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if i/j == (i//10)/j%10:
            result.append(i/j)
*/

package problems

func Digit_cancelling_numbers() int {
	nums := []int{}
	dens := []int{}
	for i := 10; i < 100; i++ {
		for j := i + 1; j < 100; j++ {
			num := i / 10
			common1 := i % 10
			den := j % 10
			common2 := j / 10
			if den != 0 && float64(i)/float64(j) == float64(num)/float64(den) && common1 == common2 {
				if den%num == 0 {
					den = den / num
					num = 1
				}
				nums = append(nums, num)
				dens = append(dens, den)
			}
		}
	}
	x := 1
	y := 1
	for _, i := range nums {
		x *= i
	}
	for _, i := range dens {
		y *= i
	}
	// if x != 0 {
	// 	return y / x
	// }
	return y / x
}
