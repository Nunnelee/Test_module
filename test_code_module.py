#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     11/12/2020
# Copyright:   (c) Owner 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def turn_clockwise(cp):
    if cp == "N":
        return "E"
    if cp == "E":
        return "S"
    if cp == "W":
        return "N"
    else:
        return


def day_name(d):
    if d == 0:
        return "Sunday"
    if d == 1:
        return "Monday"
    if d == 2:
        return "Tuesday"
    if d == 3:
        return "Wednesday"
    if d == 4:
        return "Thursday"
    if d == 5:
        return "Friday"
    if d == 6:
        return "Saturday"
    else:
        return

print(day_name(2))

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42)== None)

test_suite()

def to_secs(h, m, s):
    h = int(h * 3600)
    m = int(m * 60)
    s = int(s * 1)
    total_secs = (h+m+s)
    return total_secs

def hours_in(s):
    s = s / 3600
    total_hours = int(s)
    return total_hours

def minutes_in(s):
    m = s % 3600
    x = m / 60
    left_minutes = int(x)
    return left_minutes

def seconds_in(s):
    m = s % 3600
    x = m / 60
    y = m % 60
    left_seconds = (y)
    return left_seconds

import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

test_suite()