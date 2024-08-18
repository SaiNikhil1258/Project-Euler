/*
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless
it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?

date.weekday()
Returns the day of the week as an integer, where Monday is 0 and Sunday is 6.
For example, date(2002, 12, 4).weekday() == 2, a Wednesday
*/

package problems

import (
	"time"
)

// Using the Date package check if the first of every  month is a sunday or not.
func Counting_Sundays() int {
	lower := 1901
	upper := 2000
	count := 0
	for year := lower; year <= upper; year++ {
		for month := 1; month <= 12; month++ {
			date := time.Date(year, time.Month(month), 1, 0, 0, 0, 0, time.Local)
			if date.Weekday() == time.Sunday {
				count++
			}
		}
	}
	return count
}

/* func daysInMonth(month int, isLeapYear bool) int {
	switch month {
	case 2:
		if isLeapYear {
			return 29
		}
		return 28
	case 4, 6, 9, 11:
		return 30
	default:
		return 31
	}
}

func isLeapYear(year int) bool {
	return year%4 == 0 && (year%100 != 0 || year%400 == 0)
} */

// DoomsDay algorithm
func dayOfWeek(day, month, year int) int {
	if month <= 2 {
		month += 12
		year -= 1
	}
	c := year / 100
	y := year % 100
	w := (day + (26*(month+1))/10 + y + y/4 - c/4 - 2*c) % 7
	// fmt.Println(c, y, w)
	return w
}

func countSundaysOnFirst(startYear, endYear int) int {
	sundayCount := 0
	for year := startYear; year <= endYear; year++ {
		for month := 1; month <= 12; month++ {
			if dayOfWeek(1, month, year) == 0 {
				sundayCount++
				// fmt.Printf("Sunday on the first of %d-%d\n", month, year)
			}
		}
	}
	return sundayCount
}

func Sunday() int {
	startYear := 1901
	endYear := 2000
	count := countSundaysOnFirst(startYear, endYear)
	return count
}
