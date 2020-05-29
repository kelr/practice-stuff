def smallerNumbersThanCurrentBrute(nums):
    out = [0] * len(nums)
    for i, curr_num in enumerate(nums):
        for j, compare_num in enumerate(nums):
            if i != j and compare_num < curr_num:
                out[i] += 1
    return out

# Sort the array and map the first instance of the sorted numbers to their index in the sorted array.
# Their index is how many numbers it is larger than.
# O(NlgN) due to an NlgN sort + N iterations to fill the map + N iterations to create output array
# O(N) space due to output array
def smallerNumbersThanCurrent(nums):
    idx_map = {}
    for i, num in enumerate(sorted(nums)):
        if num not in idx_map:
            idx_map[num] = i
    return [idx_map[num] for num in nums]

# If the range is known (here its 0 <= n <= 100) then create an array of range + 1 values initialized to 0.
# Iterate nums and increment the num+1th entry per number. Then loop through the number range and
# replace values with a running sum. Each num used as index will have a value that is the # of nums smaller than it.
# O(N) due to N iterations to fill the count array. 
# O(N) space due to output array.
def smallerNumbersThanCurrentLinear(nums):
    count = [0] * 102
    for num in nums:
        count[num+1] += 1
    for i in range(1, 102):
        count[i] += count[i-1]
    return [count[num] for num in nums]