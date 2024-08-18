package problems

import "sort"

/*
A permutation is an ordered arrangement of objects. For example, 3124 is one possible
permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*/
func Nth_lexiographical_permutation() int {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
	n := 699999
	permutations_list := perumatations(numbers)
	number := permutations_list[n]
	return convertListToNumber(number)
}

func convertListToNumber(numbers []int) int {
	var result int
	for _, num := range numbers {
		result = result*10 + num
	}
	return result
}

func perumatations(nums []int) [][]int {
	result := [][]int{}
	if len(nums) == 0 {
		return result
	}
	var permute func(nums []int, start int)
	permute = func(nums []int, start int) {
		if start == len(nums) {
			perm := make([]int, len(nums))
			copy(perm, nums)
			result = append(result, perm)
			return
		}
		for i := start; i < len(nums); i++ {
			swap(nums, start, i)
			permute(nums, start+1)
			swap(nums, start, i)
		}
	}
	permute(nums, 0)
	return Sort(result)
}

func Sort(arr [][]int) [][]int {
	sort.Slice(arr, func(i, j int) bool {
		for k := range arr[i] {
			if arr[i][k] != arr[j][k] {
				return arr[i][k] < arr[j][k]
			}
		}
		return false
	})
	return arr
}

func swap(nums []int, i, j int) {
	nums[i], nums[j] = nums[j], nums[i]
}
