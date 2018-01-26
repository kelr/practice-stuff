"""
Project Euler Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""
from math import factorial

def num_of_routes(grid_size):
    # Possible permuations / permutations of right / permutations of down
    return (factorial(grid_size*2) / factorial(grid_size) / factorial(grid_size))

print(num_of_routes(20))