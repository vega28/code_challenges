# Advent of Code - Day 1
# 
# https://adventofcode.com/2024/day/1


def distance_between_lists(list1, list2):
    """ given two lists, determine how far apart they are when sorted

        e.g.
        >>> list1 = [3, 4, 2, 1, 3, 3]
        >>> list2 = [4, 3, 5, 3, 9, 3]
        >>> distance_between_lists(list1, list2)
        11
    """

    list1.sort()
    list2.sort()
    dist_list = []
    
    for i, num in enumerate(list1):
        dist_list.append(abs(num-list2[i]))

    total_distance = sum(dist_list)

    return total_distance

def parse_list(filename):
    """ import data from a text file and store as lists """

    file = open(filename, 'r')
    list1, list2 = [], []

    for line in file:
        x, y = line.split()
        list1.append(int(x))
        list2.append(int(y))

    return list1, list2

def get_similarity_score(list1, list2):
    """ given two lists, determine how similar they are when sorted

        e.g.
        >>> list1 = [3, 4, 2, 1, 3, 3]
        >>> list2 = [4, 3, 5, 3, 9, 3]
        >>> get_similarity_score(list1, list2)
        31
    """
    list1_counts = {}
    similarity_score = 0

    for num in list1:
        val = list1_counts.get(num, 0) + 1
        list1_counts[num] = val

    for num in list2:
        list1_val = list1_counts.get(num, 0)
        similarity_score += num * list1_val

    return similarity_score


#####################################################################
# determine the challenge answers

print("PART 1")
list1, list2 = parse_list('day_1_data.txt')
total_distance = distance_between_lists(list1, list2)
print("total distance is", total_distance)

print("PART 2")
similarity_score = get_similarity_score(list1, list2)
print("similarity score is", similarity_score)


#####################################################################
# run doctests

if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. NICE!")
    print()
