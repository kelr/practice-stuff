"""
Project Euler Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys
sys.path.append("..")
from maths.prime import sieve, is_prime
from maths.helperfuncs import ceiling

def prime_factorization(input_num):
    if is_prime(input_num):
        return input_num
    saved_num = input_num
    factor_list = list()
    max_sieve = ceiling(input_num**(0.5))

    print("Sieving for all primes from 2 to", str(max_sieve), "be patient, it might take a while for large numbers.")
    test_primes = sieve(max_sieve)
    while not is_prime(input_num):
        for n in test_primes:
            if input_num % n == 0:
                input_num = input_num // n
                factor_list.append(n)
                break
        if input_num == 1:
            break
    factor_list.append(input_num)

    print("Prime factorization of", saved_num, ":", str(factor_list))
    largest = 0
    for factor in factor_list:
        if factor > largest:
            largest = factor 
    print("Largest Prime factor:", largest)
    return largest

prime_factorization(600851475143)