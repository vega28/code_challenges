# Valid Braces
# https://www.codewars.com/kata/5277c8a221e209d3f6000b56/python

# Challenge:
# Write a function that takes a string of braces, and determines 
# if the order of the braces is valid. It should return true if 
# the string is valid, and false if it's invalid.
#  
# This Kata is similar to the Valid Parentheses Kata, but 
# introduces new characters: brackets [], and curly braces {}. 

# Constraints:
# All input strings will be nonempty, and will only consist of 
# parentheses, brackets and curly braces: ()[]{}.

BRACES = {
    '(' : ')',
    '{' : '}', 
    '[' : ']'
}


def are_braces_valid(string_in):
    """ given a set of braces, determine if they are valid
        braces include (), {}, [] 
        
        e.g. 
        >>> are_braces_valid('[(](){}')
        False

        >>> are_braces_valid('[()](){}')
        True

        >>> are_braces_valid('[({[([')
        False
    """

    open = []
    chars = [char for char in string_in]

    for char in chars:
        if char in BRACES.keys():
            open.append(char)
        elif open and char == BRACES[open[-1]]: 
            close = open.pop()
        else:
            return False
        
    return True if not open else False


def are_braces_valid_rec(string_in, opened=[]):
    """ RECURSION VERSION
        given a set of braces, determine if they are valid
        braces include (), {}, [] 
        
        e.g. 
        >>> are_braces_valid_rec('[(](){}', [])
        False

        >>> are_braces_valid_rec('[()](){}', [])
        True

        >>> are_braces_valid_rec('[({[([', [])
        False
    """

    if (not string_in) and (not opened): 
        return True
    elif not string_in:
        return False
    
    if string_in[0] in BRACES.keys():
        opened.append(string_in[0])
    elif string_in[0] == BRACES[opened[-1]]:
        opened.pop()
    else:
        return False

    return are_braces_valid_rec(string_in[1:], opened)




#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
