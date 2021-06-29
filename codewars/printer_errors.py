# Printer Errors
# https://www.codewars.com/kata/56541980fa08ab47a0000040


# Challenge:

# In a factory a printer prints labels for boxes. For one kind of box the 
# printer has to use colors which are named with letters from a to m.

# The colors used by the printer are recorded in a control string. 
# For example a "good" control string would be aaabbbbhaijjjm meaning that 
# the printer used three times color a, four times color b, one time color h 
# then one time color a...

# Sometimes there are problems: lack of colors, technical malfunction and a 
# "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters 
# not from a to m.

# You have to write a function printer_error which given a string will return 
# the error rate of the printer as a string representing a rational whose 
# numerator is the number of errors and the denominator the length of the 
# control string. Don't reduce this fraction to a simpler expression.


# Constraints:

# The string has a length greater or equal to one 
# and contains only letters from a to z.


# Code:

def printer_error(str):
    """ return the error rate of the printer 
    
    e.g.
    >>> printer_error("aaabbbbhaijjjm")
    0/14

    >>> printer_error("aaaxbbbbyyhwawiwjjjwwm")
    8/22

    """

    pass


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
