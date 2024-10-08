/*
Consider all integer combinations of  a^b
  for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

2^2=4,  2^3=8,   2^4=16,  2^5=32
3^2=9,  3^3=27,  3^4=81,  3^5=243
4^2=16, 4^3=64,  4^4=256, 4^5=1024
5^2=25, 5^3=125, 5^4=625, 5^5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
How many distinct terms are in the sequence generated by  ab
  for 2 ≤ a ≤ n and 2 ≤ b ≤ n?
*/

package problems

import (
	"math"
	"sort"
)

func Distant_powers() int {
	n := 15
	list := []float64{}
	for i := 2; i < n+1; i++ {
		for j := 2; j < n+1; j++ {
			x := math.Pow(float64(i), float64(j))
			list = append(list, x)
		}
	}
	sort.Float64s(list)
	// return len(list)
	return len(removeDuplicates(list))
}

func removeDuplicates(sortedList []float64) []float64 {
	unique_list := []float64{}
	for i := 0; i < len(sortedList); i++ {
		if i == 0 || sortedList[i] != sortedList[i-1] {
			unique_list = append(unique_list, sortedList[i])
		}
	}
	return unique_list
}
