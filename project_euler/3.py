"""
Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def factorize(num):
	factor_list = list()
	# We only need to check up to floor(sqrt(num)) if a number is prime
	max = int(num**(0.5))
	for n in range(2, max):
		while num % n == 0:
			print(n, num)
			num = num // n
			factor_list.append(n)
	return factor_list

def largest_prime_factor(num):
	prime_list = list()

	if num % 2 == 0:
		num = num // 2
		prime_list.append(2)
	if num % 3 == 0:
		num = num // 3
		prime_list.append(3)


factorize(600851475143)
#largest_prime_factor(600851475143)