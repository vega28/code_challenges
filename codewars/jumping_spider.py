# Jumping Spider
# https://www.codewars.com/kata/5a30e7e9c5e28454790000c1


# Challenge:

# A spider web is defined by the following web coordinates:
#   "rings" numbered radially out from the center as 0, 1, 2, 3, 4
#   "radials" labelled clock-wise from the top as A, B, C, D, E, F, G, H (angles)
# Each point where the rings & radials intersect is a "web coordinate".

# Our jumping spider is resting at web-coordinate 'spider'.
# A fly bumbles into the web at web-coordinate 'fly' and gets itself stuck.

# Your task is to calculate and return the distance the spider must jump 
# to get to the fly.


# Constraints:

# The center of the web will always be referred to as A0
# The rings intersect the radials at evenly spaced distances of 1 unit


# Code:

def get_distance(spider, fly):
    """ Find and return the distance between the spider and the fly. """
    
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
