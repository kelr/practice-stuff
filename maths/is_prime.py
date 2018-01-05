def is_prime(n):
    if n < 2:
        raise ValueError
    # We only need to check divisibility for up to floor(n <= sqrt(n))
    max = int(n**(0.5))

    # 2 is the loneliest prime
    if n == 2:
        return True

    # Get the even primes out of the way
    if n % 2 == 0:
        return False

    # Iterate over odd test values as 2 is the only even prime
    for test in range(3, max, 2):
        if n % test == 0:
            return False

    return True

if __name__ == '__main__':
    import sys
    print(is_prime(int(sys.argv[1])))