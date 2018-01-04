import sys

def sieve(n):
	"""
	Some slow implementation for the Sieve of Eratosthenes.
	Takes a positive integer n and returns a list containing all the primes
	from 2 to n.
	"""
	n = int(n)
	# Use a dict for the marked list for better searching
	marked = dict()
	prime_list = list()
	# Test all positive integers sans 1 within the given range
	for curr in range(2, n+1):
		# If the current integer being tested wasn't marked by the sieve,
		# It must be prime, then mark all multiples of the current integer
		if curr not in marked.keys():
			prime_list.append(curr)
			# Mark all multiples of the current integer, because they aren't prime.
			# We start marking from curr^2 as all smaller multiples of curr will have already been marked
			for m in range(curr**2, n+1, curr):
				marked[m] = False
	return prime_list


if __name__ == '__main__':
	print(sieve(sys.argv[1]))