# Get Middle
# https://www.codewars.com/kata/56747fd5cb988479af000028

# Challenge:
# You are going to be given a non-empty string. Your job is to 
# return the middle character(s) of the string.
# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters. 

# Constraints: none


def get_middle(s):
    """ given a string s, return the middle character(s)
        
        e.g. 
        >>> get_middle('test')
        'es'

        >>> get_middle('testing')
        't'

        >>> get_middle('middle')
        'dd'

        >>> get_middle('A')
        'A'
    """
 
    if len(s) % 2 == 1:
        mid = s[int((len(s) - 1) / 2)]
    else:
        mid = s[int(len(s) / 2 - 1)] + s[int(len(s) / 2)]

    return mid


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
