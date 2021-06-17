# Is a Number Prime?
# https://www.codewars.com/kata/5262119038c0985a5b00029f

# Challenge:
# Define a function that takes one integer argument and returns 
# logical value true or false depending on if the integer is a prime.

# Constraints:
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
# NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.

# Code:

def is_prime(num):
    """ Determine whether the given number is prime. 

        e.g.
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(-1)
        False
        >>> is_prime(73)
        True

    """
    import math
    
    if num < 2:         # 1, 0, and negative numbers are not prime
        return False
    
    if num == 2:        # edge case: the only even prime number
        return True
    
    if num % 2 == 0:    # narrow down results by excluding even numbers
        return False
    
    """ Side note on the algorithm:

    Initially, I had the for-loop run from 3 to num/2+1, but that timed out 
    (as expected) for large numbers and included many duplicate factor pairs.

    I used this source as inspiration for a handy math trick: 
    https://medium.com/swlh/an-algorithm-a-day-how-to-check-for-a-prime-number-in-javascript-7052630fb4ef
    and now use the square root as the max since that is the largest number
    for factor pairs before repeats start to happen.
    
    This method improves runtime for very large numbers and makes it doable! 

    """
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
        
    return True


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
