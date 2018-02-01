from . import time_it
from .helperfuncs import ceiling

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

    # 2 is still the loneliest prime
    prime_list.append(2)
    
    # Test all positive non even integers within the given range
    for curr in range(3, n, 2):
        # If the current integer being tested wasn't marked by the sieve,
        # It must be prime, then mark all multiples of the current integer
        if curr not in marked:
            prime_list.append(curr)
            # Mark all multiples of the current integer, because they aren't prime.
            # We start marking from curr^2 as all smaller multiples of curr will have already been marked
            for m in range(curr*curr, n+1, curr):
                marked[m] = False
    return prime_list

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

@time_it.time_it
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

def is_prime(n):
    # 1 is not prime, by the way
    if n < 2:
        return False
        
    # We only need to check divisibility for up to floor(n <= sqrt(n))
    # Added a +1 to deal with small values of n. I'm aware that I can just use ceiling.
    n_max = ceiling(n**(0.5))
    
    # 2 is the loneliest prime
    if n == 2:
        return True

    # Get the even primes out of the way
    if n % 2 == 0:
        return False

    test = 3
    # Iterate over odd test values as 2 is the only even prime. Terminates early if a divisor is found
    while n % test != 0 and test < n_max:
        test += 2

    # This will return true if we've iterated through everything from 3 to sqrt(n)+1, meaning prime
    return test > n_max

def generate_prime():
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2

if __name__ == '__main__':
    import sys
    print(is_prime(int(sys.argv[1])))