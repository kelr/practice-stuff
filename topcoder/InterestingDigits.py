class InterestingDigits:
	def digits(self, base):
		"""
		Tests all the numbers, n, from 2 to base if all the multiples of n from
		1 to base^3 has the property that the sum of their digits is also a multiple of n
		"""
		interesting_list = list()
		for n in range(2, base):
			# Test multiples only up to 4 digits long in the chosen base
			for x in range(1, base**3):
				# Find a multiple of n
				if x % n == 0:
					# Break if the sum of the digits for this multiple of n, x
					# Is not also a multiple of n, failure case
					if self.sum_digits(x, base) % n != 0:
						break
			else:
				# Only add the current digit to the interesting list
				# If all cases pass
				interesting_list.append(n)
		return interesting_list

	def sum_digits(self, n, base):
		ret_val = 0
		# For a number, n of any base, base, sum the digits of n in base
		while n:
			# The // is integer division in Python 3
			ret_val, n = ret_val + n % base, n // base
		return ret_val

dig = InterestingDigits()
print(dig.digits(10))
print(dig.digits(3))
print(dig.digits(30))