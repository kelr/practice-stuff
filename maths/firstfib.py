import math

# O(sqrt(N)) time O(1) space.
def numFactors(n):
    count = 0
    # Increment count twice to handle the corresponding factor on the other side of the sqrt.
    # Only count once if the sqrt of the number is the current possible factor otherwise it itself will be counted twice.
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            if n == i*i:
                count += 1
            else:
                count += 2
    return count

# Finds the first fib with more than 1k factors.
# O(N*sqrt(F)) time where N is the nth fib number and F is the actual fib number.
def firstFibWith1KFactors():
    a = 1
    b = 1

    factors = numFactors(a)
    while factors != 1000:
        factors = numFactors(a)
        print(a, "has", factors)
        a, b = b, a + b
    print("found:", a, factors)

firstFibWith1KFactors()