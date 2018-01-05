from sieve import sieve
from time_it import time_it
import sys

def lucas_lehmer(prime):
    """
    Implements the Lucas-Lehmer test to determine
    if the given prime number, p, yields a Mersenne prime
    of the form Mp = 2^p - 1
    """
    # 2 is the loneliest prime number
    if prime == 2:
        return True

    s = 4
    M = (2 ** prime) - 1

    for _ in range(0, prime-2):
        s = (s ** 2 - 2) % M

    return True if s == 0 else False

def calc_mersenne(prime):
    return (2 ** prime) - 1

@time_it
def mersenne(prime_max):
    """
    Calculates all the primes from 2 to prime_max,
    Then determines which of those primes yield Mersenne Primes
    Returns a list of Mersenne Primes
    """
    mersennes = list()
    primes = sieve(int(prime_max))
    for prime in primes:
        if lucas_lehmer(prime):
            mersennes.append(calc_mersenne(prime))
    return mersennes


if __name__ == '__main__':
    print(mersenne(sys.argv[1]))