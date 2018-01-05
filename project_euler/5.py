"""
Project Euler Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def check_divisible(num, max):
    # Don't need to test for 1 or 2
    for divisor in range(3, max):
        if num % divisor != 0:
            return False
    return True

def smallest_divisible(max):

    # Numbers less than the range between 2 to max can't be divided by all numbers from 1 to max evenly
    if max % 2:
        # Adjust up one if the max was odd
        num = max + 1
    else:
        num = max
    # Ignore odd numbers because all of them can't be divided by 2
    while not check_divisible(num, max):
        num += 2
    print(num)
    return num

smallest_divisible(20)