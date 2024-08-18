/*
 A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
1 + 2 + 4 + 7 + 14 = 28, which meres that 28 is a perfect number.
 A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.
 As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number
that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum of
two abundant numbers is less than this limit.
 Find the sum of all positive integers <= n which cannot be written as the sum of two
abundant numbers. */

/* The idea is to find all the abundant numbers < n
find the sum of all the abundant numbers without duplicates you will get a set
of all the numbers that can be represented as the sum of
abundant numbers
You want an another set that has all the numbers from 1 to n
All the positive numbers that can be written as the sum of two abundant numbers
will be the difference between them */

package problems

func sum_of_proper_divisors(n int) int {
	sum := 1
	for i := 2; i < (n/2)+1; i++ {
		if n%i == 0 {
			sum += i
		}
	}
	return sum
}

func abundant_numbers(n int) []int {
	abundant_numbers := []int{}
	for i := 10; i < n; i++ {
		if sum_of_proper_divisors(i) > i {
			abundant_numbers = append(abundant_numbers, i)
		}
	}
	return abundant_numbers
}

func Non_abundant_Numbers_sum() int {
	n := 10000
	res := abundant_numbers(n)
	ans := map[int]int{}
	for _, a := range res {
		ans[a] = 1
	}
	// fmt.Println(ans)
	sum := 1
	for i := 2; i < n+1; i++ {
		found := false
		// if i is the sum of two abundant n's, there exists an res < i such
		// that i-a is an res;  use the map to check this membership in O(1)
		for _, a := range res {
			if a > i {
				break
			}
			// fmt.Println(a, i)
			if ans[i-a] != 0 {
				found = true
				// fmt.Println(ans[i-a])
				break
			}
		}
		if !found {
			sum += i
		}
	}
	return sum
}
