# Create a recursive function that takes in a string and a character
# and returns the string with any instances of that character removed.

# Constraints:
#   do not use str.replace()

def remove_char(string, char):
    """ Given a string and a character, 
        remove all instances of that character from that string,
        return the resulting string.

        e.g.
        >>> remove_char('abba', 'b')
        'aa'

        >>> remove_char('aaaaaa', 'A')
        'aaaaaa'

        >>> remove_char('', 'a')
        ''
    """

    if char not in string: # base case: stop recursion when this condition is met
        return string

    char_loc = string.find(char) # location of first instance of char in string
    
    return remove_char(string[0:char_loc] + string[char_loc+1:], char)



#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
