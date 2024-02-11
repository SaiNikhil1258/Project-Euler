# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# date.weekday()
# Returns the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, date(2002, 12, 4).weekday() == 2, a Wednesday

# Doomsday Algorithm
def days_in_month(month, is_leap_year):
    """Returns the number of days in a month, considering leap years."""
    if month == 2:
        return 29 if is_leap_year else 28
    else:
        return 31 if month in (1, 3, 5, 7, 8, 10, 12) else 30

def is_leap_year(year):
    """Determines if a year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_week(day, month, year):
    """Calculates the day of the week for a given date."""
    if month == 1 or month == 2:
        month += 12
        year -= 1
    c = year // 100
    y = year % 100
    w = (day + (26 * (month + 1) // 10) + y + y // 4 - c // 4 - 2 * c) % 7
    return w

def count_sundays_on_first(start_year, end_year):
    """Counts Sundays occurring on the first day of a month within a timeframe."""
    sunday_count = 0
    year = start_year
    while year <= end_year:
        for month in range(1, 13):
            if day_of_week(1, month, year) == 0:
                sunday_count += 1
        year += 1
    return sunday_count



# using python date time module
from datetime import date

def counting_sundays(lower,upper):
    count = 0
    for y in range(lower,upper+1):
        for m in range(1,13):
            if date(y,m,1).weekday() == 6:
                count +=1
    return count

# print(counting_sundays(1901,2000))

# print(count_sundays_on_first(1901, 2000))  # Output: 171
# print(count_sundays_on_first(1995, 2000))  # Output: 10
# print(count_sundays_on_first(1943, 1946))  # Output: 6


import unittest


class Test(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual(counting_sundays(1901,2000),171)
        self.assertEqual(count_sundays_on_first(1901,2000),171)
        
    def test_2(self):
        self.assertEqual(counting_sundays(1995,2000),10)
        self.assertEqual(count_sundays_on_first(1995,2000),10)
        

if __name__=='__main__':
    unittest.main()
