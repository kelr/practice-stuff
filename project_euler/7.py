"""
Project Euler Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import sys
sys.path.append("..")
from maths.prime import generate_prime

def get_nth_prime(n):
    count = 1
    if n < 1:
        print("Need an input greater than 1")
        return
    for p in generate_prime():
        #print (p)
        if count == n:
            return p
        count += 1

print(get_nth_prime(6))
print(get_nth_prime(10001))