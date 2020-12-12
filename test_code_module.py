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