/*
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1000000, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
*/

package problems

import (
	"fmt"
	"strconv"
)

func Decimal_to_binary(n int) string {
	return strconv.FormatInt(int64(n), 2)
}

func is_string_palindrome(n interface{}) bool {
	// Convert to string for uniform palindrome checking
	str := fmt.Sprintf("%v", n)
	for i := 0; i < len(str)/2; i++ {
		if str[i] != str[len(str)-i-1] {
			return false
		}
	}
	return true
}

func Double_base_palindrome(n int) int {
	sum := 0
	for i := 1; i < n; i++ {
		if is_string_palindrome(i) && is_string_palindrome(Decimal_to_binary(i)) {
			sum += i
		}
	}
	return sum
}
