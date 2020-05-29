# Find the largest current value of candies, then check if any of the kids can meet or exceed the max when you give
# them all the extras. 
# O(N) time since N comparisons to find the max, then N comparisons to check if they can have the greatest.
# O(N) space technically since an output list has to be created with one result per kid.
def kidsWithCandies(candies, extraCandies):
    maxCandies = 0

    for kid in candies:
        if kid > maxCandies:
            maxCandies = kid

    # Listcomps are real fast :O
    return [kid + extraCandies >= maxCandies for kid in candies]