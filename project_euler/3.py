"""
Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys
sys.path.append("..")
from maths import sieve, is_prime

def prime_factorization(num):
    if is_prime.is_prime(num):
        return num
    saved_num = num
    factor_list = list()
    max_sieve = int(num**(0.5))

    print("Sieving for all primes from 2 to", str(max_sieve), "be patient, it might take a while for large numbers.")
    test_primes = sieve.sieve(max_sieve)
    while not is_prime.is_prime(num):
        for n in test_primes:
            if num % n == 0:
                num = num // n
                factor_list.append(n)
                break
    factor_list.append(num)

    print("Prime factorization of", saved_num, ":", str(factor_list))
    largest = 0
    for factor in factor_list:
        if factor > largest:
            largest = factor 
    print("Largest Prime factor:", largest)
    return largest

prime_factorization(600851475143)