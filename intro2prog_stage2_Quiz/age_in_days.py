# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.
#
# This is my attempt prior to the start of the lesson, per the instructions of the lesson.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
    return False

    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    return days

print isLeapYear(2020)
print isLeapYear(2019)
print isLeapYear(1800)
print isLeapYear(2000)
