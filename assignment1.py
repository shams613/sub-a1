#!/usr/bin/env python3

"""
OPS445 Assignment 1 Version C
Program: assignment1.py 
The python code in this file is original work written by
Shams Bin Harun. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or online resource. I have not shared this Python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Shams Bin Harun
Student ID: 155871221
Semester: Fall 2024
Description: This script calculates the end date, including the day of the week,
             given a start date and a number of days.
"""

import sys

def day_of_week(date: str) -> str:
    """ Returns the day of the week for a given date in DD/MM/YYYY format. Based on the algorithm by Tomohiko Sakamoto. """
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    """  Returns True if the year is a leap year, otherwise False. """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """ Returns the maximum number of days for the given month and year. """
    if month == 2:  # February
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:
        return 31  # All other months

def after(date: str) -> str:
    """ Returns the next day's date in DD/MM/YYYY format. """
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1
    if day > mon_max(mon, year):
        day = 1
        mon += 1
        if mon > 12:
            mon = 1
            year += 1
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    """  Returns the previous day's date in DD/MM/YYYY format. """
    day, mon, year = (int(x) for x in date.split('/'))
    day -= 1
    if day < 1:
        mon -= 1
        if mon < 1:
            mon = 12
            year -= 1
        day = mon_max(mon, year)
    return f"{day:02}/{mon:02}/{year}"

def usage():
    """ Prints a usage message and exits the script. """
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    """ Validates if the given date is in DD/MM/YYYY format and is a real date. """
    try:
        day, month, year = (int(x) for x in date.split('/'))
        if 1 <= month <= 12 and 1 <= day <= mon_max(month, year):
            return True
        return False
    except (ValueError, IndexError):
        return False

def day_iter(start_date: str, num: int) -> str:
    """ Iterates from a start date by the given number of days. Returns the resulting date in DD/MM/YYYY format. """
    current_date = start_date
    if num > 0:
        for _ in range(num):
            current_date = after(current_date)
    elif num < 0:
        for _ in range(-num):
            current_date = before(current_date)
    return current_date

if __name__ == "__main__":
    """ Checks the number of command-line arguments """
    if len(sys.argv) != 3:
        usage()

    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()

    """ Validate the input date """
    if not valid_date(start_date):
        usage()

    """ Calculate the end date """
    end_date = day_iter(start_date, num_days)
    end_day = day_of_week(end_date)

    """ Prints the result """
    print(f"The end date is {end_day}, {end_date}.")
