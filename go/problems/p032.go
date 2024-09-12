/*
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5
pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through n pandigital.

Hint: Some products can be obtained in more than one way so be sure to only
include it once in your sum 1.
one approach is to iterate through all the numbers in the range of the given
number of digits and check if the number is pandigital or not.


the better approach is by using the property of pandigital numbers.
if the sum of digits of multiplier, multiplican and product is equal to the
number of digits then the number is pandigital.
so if the number of digits is 9 we only need to iterate for numbers less than
10000.this is because 99*99 = 9801 -> 8 digits if you increase either the
multiplicand and the multiplier we will get a number with more than 9 digits.
so those all are redundant calculations the limit will be under the 10000 mark

for 4 digits the limit is less than 100
for 6 digits the limit is less than 1000
*/

package problems

import (
	"math"
	"sort"
	"strconv"
	"strings"
)

func Pandigital_products() int {
	digits := 9
	var limit int
	if digits == 4 {
		limit = 100
	} else if digits == 6 {
		limit = 1000
	} else {
		limit = 10000
	}
	res := 0
	for i := 1; i < limit; i++ {
		if is_pandigital(i, digits) {
			res += i
		}
	}
	return res
}

func is_pandigital(n, digits int) bool {
	number := array_of_digits(digits)
	// fmt.Println(number)
	for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			temp := strconv.Itoa(n) + strconv.Itoa(i) + strconv.Itoa(n/i)
			sortedTemp := strings.Split(temp, "")
			sort.Strings(sortedTemp)
			if strings.Join(sortedTemp, "") == number {
				return true
			}
		}
	}
	return false
}

func array_of_digits(digits int) string {
	res := make([]string, digits)
	for i := 1; i <= digits; i++ {
		res[i-1] = strconv.Itoa(i)
	}
	return strings.Join(res, "")
}
