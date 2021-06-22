# Moving Zeros to the End
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

# Challenge:
# Write an algorithm that takes an array and moves all of the zeros 
# to the end, preserving the order of the other elements.

# Constraints:
# none

# Code:

def move_zeros(array):
    """ Take in an array and move all zeros to the end. 
    
        e.g.
        >>> move_zeros([1, 0, 1, 2, 0, 1, 3]) 
        [1, 1, 2, 1, 3, 0, 0]
        
        """

    zeros = []
    zero_count = 0

    # find and count all the zeros
    for i, num in enumerate(array):
        if num == 0:
            zeros.append(i)
            zero_count += 1

    # remove the zeros and add them to the end
    zeros.reverse()
    for j in zeros:
        array.pop(j)
    array.extend([0]*zero_count)

    return array


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
