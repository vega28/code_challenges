# Mumbling
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

# Challenge:
# Transform any input string by the given pattern:
#   for each character, multiply by the place in the string,
#   then capitalize the first one of that character,
#   then string them together by dashes. 

# Constraints:
# the input string will only contain characters a..z and A..Z.

# Code:
def accum1(s):
    """ Build the string according to the pattern.
    e.g.
    
    >>> accum1('abcd')
    'A-Bb-Ccc-Dddd'

    >>> accum1("RqaEzty")
    'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'

    >>> accum1("cwAt") 
    'C-Ww-Aaa-Tttt'
    """
    
    result = ''
    
    for i, char in enumerate(s):
        if i > 0:
            result += '-'
        result += char.upper() + (char.lower())*i
    
    return result


def accum2(s):
    """ Build the string according to the pattern.
    e.g.
    
    >>> accum2('abcd')
    'A-Bb-Ccc-Dddd'

    >>> accum2("RqaEzty")
    'R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy'

    >>> accum2("cwAt") 
    'C-Ww-Aaa-Tttt'
    """
    return '-'.join([c.upper() + c.lower()*i for i, c in enumerate(s)])



#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
