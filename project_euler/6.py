"""
Project Euler Problem 6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_square_diff(max):
    sum_of_squares, curr_sum = 0, 0
    for n in range(1, max+1):
        sum_of_squares += n**2
        curr_sum += n 
    square_of_sum = curr_sum**2
    return square_of_sum - sum_of_squares

print(sum_square_diff(10))
print(sum_square_diff(100))