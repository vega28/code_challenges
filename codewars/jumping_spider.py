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

import math


def get_distance(spider, fly):
    """ Find and return the distance between the spider and the fly. 
        method #1 - using a dictionary to convert the letter to an angle

        e.g.
        
        >>> get_distance('H3', 'E2')
        4.63522

        """

    # first, convert "web coordinates" to polar coordinates
    angles = {
        'A' : 0,
        'B' : math.pi/4,
        'C' : math.pi/2,
        'D' : 3*math.pi/4,
        'E' : math.pi,
        'F' : 5*math.pi/4,
        'G' : 3*math.pi/2,
        'H' : 7*math.pi/4
    }

    r1, r2 = int(spider[1]), int(fly[1])
    angle1, angle2 = angles[spider[0]], angles[fly[0]]

    # then, use polar coordinate distance formula (law of cosines):
    distance = math.sqrt(r1**2 + r2**2 -2*r1*r2*math.cos(angle1 - angle2))

    return round(distance, 5)


def get_distance_v2(spider, fly):
    """ Find and return the distance between the spider and the fly. 
        method #2 - using ascii table to convert the letter to an angle

        e.g.
        
        >>> get_distance('H3', 'E2')
        4.63522

        """

    # first, convert "web coordinates" to polar coordinates
    r1, r2 = int(spider[1]), int(fly[1])
    angle1, angle2 = (ord(spider[0])-65)*math.pi/4, (ord(fly[0])-65)*math.pi/4

    # then, use polar coordinate distance formula (law of cosines):
    distance = math.sqrt(r1**2 + r2**2 -2*r1*r2*math.cos(angle1 - angle2))

    return round(distance, 5)


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
