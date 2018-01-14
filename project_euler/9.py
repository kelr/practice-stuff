"""
Project Euler Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import sys
sys.path.append("..")
from maths.arithmatic import sum_items, product_items

def generate_triplet(max_val):
    for a in range (1, max_val):
        for b in range (a, max_val):
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                yield a,b,c

def find_specific_product():
    for n in generate_triplet(1000):
        if sum_items(n) == 1000:
            return product_items(n)


print(find_specific_product())