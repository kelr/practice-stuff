"""
Project Euler Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import sys
sys.path.append("..")
from maths.prime import sieve
from maths.arithmatic import sum_items

# Code reuse is great
def sum_of_primes_below(maximum):
    return sum_items(sieve(maximum))

print(sum_of_primes_below(2000000))