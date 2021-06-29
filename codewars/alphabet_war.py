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
    'Right side wins!'
    >>> alphabet_war('*zd*qm*wp*bs*')
    "Let's fight again!"
    >>> alphabet_war('zzzz*s*')
    'Right side wins!'
    >>> alphabet_war('www*www****z')
    'Left side wins!'
    """

    left_side = {
        'w' : 4,
        'p' : 3,
        'b' : 2,
        's' : 1
    }

    right_side = {
        'm' : 4,
        'q' : 3,
        'd' : 2,
        'z' : 1
    }

    aftermath = [char for char in s]
    
    for i, char in enumerate(s): 
        if char == '*':
            aftermath[i] = '_'
            if i < len(s) - 1:
                aftermath[i+1] = '_'
            if i > 0:
                aftermath[i-1] = '_'

    aft = ''.join(aftermath)

    left_score = 0
    right_score = 0

    for char in aft:
        if left_side.get(char):
            left_score += left_side[char]
        elif right_side.get(char):
            right_score += right_side[char]

    if right_score > left_score:
        return "Right side wins!"
    elif right_score < left_score:
        return "Left side wins!"
    else:
        return "Let's fight again!"


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
