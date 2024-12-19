# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014

# Challenge:
# Create a function that returns the sum of the two lowest positive 
# numbers given an array of minimum 4 positive integers. 
# 
# For example, when an array is passed like [19, 5, 42, 2, 77], 
# the output should be 7.

# Constraints: 
# No floats or non-positive integers will be passed.


def sum_two_smallest_numbers(a):
    """ given an array a, return the sum of the lowest two integers
        
        e.g. 
        >>> sum_two_smallest_numbers([5, 8, 12, 18, 22])
        13

        >>> sum_two_smallest_numbers([7, 15, 12, 18, 22])
        19

        >>> sum_two_smallest_numbers([25, 42, 12, 18, 22])
        30

        >>> sum_two_smallest_numbers([1, 1, 1, 4])
        2
    """

    a.sort()
    return a[0]+a[1]


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
