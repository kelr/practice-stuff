"""
Leetcode 1
Given an array of integers, return indicies of the
two numbers such that they add up to a target.

You may assume each input would have exactly one solution
may not use the same element twice

Ex:
[2, 7, 11, 15], target = 9

return [0, 1]

"""
""" 
Planning:

Create map
Loop through each, elem, i with enumerate
if map[elem] exists
    return [map[elem], i]

find compliment of elem -> compliment = abs(elem - target)
add map entry: map[compliment] = i
    trying to map the index of elem to the wanted compliment

Complexity
O(N) where N is number of elems in nums since there is only one pass. 

Space
O(N) where N is number of elems, will create a dict entry per element if no element sums to target
"""
class Solution:
    def two_sum(self, nums, target):
        comp_map = {}
        for i, elem in enumerate(nums):
            try:
                return [comp_map[elem], i]
            except KeyError:
                compliment = abs(elem - target)
                comp_map[compliment] = i
        return []

    # O(N^2) time, O(1) space
    def two_sum_brute_force(self, nums, target):
        for i, elem1 in enumerate(nums):
            for j, elem2 in enumerate(nums):
                if elem1 + elem2 == target:
                    return [i, j]
        return []


assert Solution().two_sum([2,7,11,15], 9) == [0, 1]
assert Solution().two_sum_brute_force([2,7,11,15], 9) == [0, 1]
