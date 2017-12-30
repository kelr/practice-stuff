import sys
import math
import time
from functools import wraps
import matplotlib.pyplot as plot

collatz_history = dict()

def time_it(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		time_start = time.time()
		result = func(*args, **kwargs)
		time_end = time.time()
		print ('%r %4.4f ms' % (func.__name__, (time_end - time_start) * 1000))
		return result
	return wrapper		

def collatz(num):
	global collatz_history
	num = int(num)
	curr = num
	count = 0
	if num > 0:
		while curr != 1:
			if curr in collatz_history.keys():
				collatz_history[num] = count + collatz_history[curr]
				return count + collatz_history[curr]
			if (curr % 2 == 0):
				curr = int(curr/2)
				count += 1
			else:
				curr = (3*curr + 1)/2
				count += 2
		collatz_history[num] = count
	else:
		print("Need to be positive int")
	return count

@time_it
def longest_collatz(max):
	curr_max = 0
	result = 0
	num_result = 0
	index_list = list()
	count_list = list()
	max = int(max)
	for num in range(1,max):
		result = collatz(num)
		if result > curr_max:
			curr_max = result
			num_result = num
	for index in collatz_history:
		index_list.append(index)
		count_list.append(collatz_history[index])
	plot.scatter(index_list, count_list, s=1)
	plot.show()
	print("Max iters: " + str(curr_max) + " at num: " + str(num_result) + " for range 1 to " + str(max))

if __name__ == "__main__":
 	longest_collatz(sys.argv[1])
