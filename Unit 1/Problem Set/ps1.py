###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    cow_list = cows.copy()
    sorted_cowList = sorted(cow_list, key = cow_list.get, reverse = True)
    cargo_weight = 0
    total = []

    while (cargo_weight <= limit) and len(sorted_cowList) > 0:
        result = []
        for i in sorted_cowList:
            if (cargo_weight + cow_list[i]) <= limit:
                result.append(i)
                cargo_weight += cow_list[i]
        for j in result:
            sorted_cowList.remove(j)
        if len(sorted_cowList) > 0:
            cargo_weight = 0
        total.append(result)    

    return total
        

# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def access_weight(L, dic, limit):
        for i in L:
            weight = 0
            for j in i:
                weight +=dic[j]
            if weight > limit:
                return False
        return True
            
    cow_list = cows.copy()
    result = []
    try:
        # sort partitions into a list by increasing order based on length
        partitions = sorted(get_partitions(cows), key = len)
        for i in partitions:
            if access_weight(i, cow_list, limit):
                result = i
                return i
    except StopIteration:
        return result

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy_cow_transport(cows, limit)
    end = time.time()
    print(end - start)
    start = time.time()
    brute_force_cow_transport(cows, limit)
    end = time.time()
    print(end - start)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""


limit=100

cows = load_cows("ps1_cow_data.txt")
print(cows)
print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

