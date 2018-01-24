import sys
import math
import time
import matplotlib.pyplot as plot
#from time_it import time_it

collatz_history = dict()
    

def collatz(num):
    """
    Calculates the number of Collatz iterations it takes for a given number num to reach 1. 
    """
    global collatz_history
    num = int(num)
    curr = num
    count = 0
    if num > 0:
        while curr != 1:
            # If the current number has already had its Collatz iterations calculated before, just retrieve it from the cached hash table.
            # This will speed up this algorithm some at the cost of space.
            # I'm aware that ~100 million entries in this table will use 8 GB+ of memory. Oh well, because it's faster than not doing it.
            # Maybe a hash table isn't the best data structure for this...
            if curr in collatz_history.keys():
                collatz_history[num] = count + collatz_history[curr]
                return count + collatz_history[curr]
            if (curr % 2 == 0):
                curr = curr / 2
                count += 1
            else:
                # It saves some time to do two steps in one if the current number is odd
                # since 3n+1 will always be even if n is odd.
                curr = (3*curr + 1) / 2
                count += 2
        collatz_history[num] = count
    else:
        print("Need to be positive int")
    return count

def max_collatz(max):
    """
    The entry point for this script
    """
    curr_max = 0
    result = 0
    num_result = 0
    num_list = list()
    count_list = list()
    max = int(max)
    # Caluclate the Collatz iterations for every integer in the given range
    for num in range(1,max):
        result = collatz(num)
        # We only really care about the running maximum 
        if result > curr_max:
            curr_max = result
            num_result = num

    # Seperate out the history dictionary into lists for easier plotting
    for number in collatz_history:
        num_list.append(number)
        count_list.append(collatz_history[number])
    plot.scatter(num_list, count_list, s=1)
    plot.show()

    print("Max iters: " + str(curr_max) + " at num: " + str(num_result) + " for range 1 to " + str(max))

if __name__ == "__main__":
     max_collatz(sys.argv[1])