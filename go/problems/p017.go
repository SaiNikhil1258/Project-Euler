/*
Problem 17: Number letter counts

	If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters
	used in total.
	If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

	Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and

115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
*/
package problems

var digits = map[int]int{
	1: 3, //"one",
	2: 3, //"two",
	3: 5, //"three",
	4: 4, //"four",
	5: 4, //"five",
	6: 3, //"six",
	7: 5, //"seven",
	8: 5, //"eight",
	9: 4, //"nine",
}

var tens = map[int]int{
	10: 3, //"ten",
	11: 6, //"eleven",
	12: 6, //"twelve",
	13: 8, //"thirteen",
	14: 8, //"fourteen",
	15: 7, //"fifteen",
	16: 7, //"sixteen",
	17: 9, //"seventeen",
	18: 8, //"eighteen",
	19: 8, //"nineteen",
	2:  6, //"twenty",
	3:  6, //"thirty",
	4:  5, //"forty",
	5:  5, //"fifty",
	6:  5, //"sixty",
	7:  7, //"seventy",
	8:  6, //"eighty",
	9:  6, //"ninety",
}

/*
// NOTE: you create two maps one for singe digit number and one for two digit numbers from then on you can
add the third digits and more from them on or you can do that also as an array since we only do for the numbers
in the range of thousand so use if only
*/
func Number_letter_count(n int) uint64 {
	sum := uint64(0)
	for i := 1; i <= n; i++ {
		// println(i, num_letters(i))
		sum += uint64(num_letters(i))
	}
	return sum
}

func num_letters(n int) int {
	if digits[n] > 0 {
		return digits[n]
	}
	if tens[n] > 0 {
		return tens[n]
	}
	if n == 1000 {
		return 3 + 8
	}
	if n%100 == 0 {
		return digits[n/100] + 7
	}
	if n > 100 {
		return digits[n/100] + 10 + num_letters(n%100)
	}
	if n%10 == 0 {
		return tens[n/10]
	}
	return tens[n/10] + digits[n%10]

}
