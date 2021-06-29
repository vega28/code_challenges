# Alphabet War - Airstrike
# https://www.codewars.com/kata/5938f5b606c3033f4700015a


# Challenge:

# There are two groups of hostile letters: the left side and right side.

# Write a function that accepts fight string consists of only small letters 
# and * which means a bomb drop place. Return who wins the fight after bombs 
# are exploded. When the left side wins return Left side wins!, when the right 
# side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:
#  w - 4
#  p - 3 
#  b - 2
#  s - 1

# The right side letters and their power:
#  m - 4
#  q - 3 
#  d - 2
#  z - 1

# The other letters don't have power and are only victims.
# The * bombs kills the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ ); 


# Code:

def alphabet_war(s):
    """ determine who wins the war: left side letters or right side letters 
    
    e.g.
    >>> alphabet_war('s*zz')
    Right side wins!
    >>> alphabet_war('*zd*qm*wp*bs*')
    Let's fight again!
    >>> alphabet_war('zzzz*s*')
    Right side wins!
    >>> alphabet_war('www*www****z')
    Left side wins!
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
