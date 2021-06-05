# Create a recursive function that takes in a string and a character
# and returns the string with any instances of that character removed.

def remove_char(string, char):
    """ given a string and a character, 
        remove all instances of that character from that string,
        return the resulting string

        e.g.
        >>> remove_char('abba', 'b')
        'aa'

        >>> remove_char('aaaaaa', 'A')
        'aaaaaa'
    """

    if char not in string: # base case - exit out of recursion when this condition is met
        return string

    pass # TODO: write this recursive function!



#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
