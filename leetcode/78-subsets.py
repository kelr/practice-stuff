
# Start with an empty set. For each number in nums, create new sets by
# concatinating the number with each set in the output.
# Bottom up DP
# O(N * 2^N) time, generates 2^N subsets and linear copy time
# O(2^N) space, storing 2^N subsets.
def subsets(nums):
    output = [[]]
    
    for num in nums:
        nextSets = []
        for currSet in output:
            nextSets.append(currSet + [num])
        output += nextSets
    
    return output

# Use backtrack to build sets of size k from 0 to N.
# O(N * 2^N) time, generates 2^N subsets and linear copy time
# O(2^N) space, storing 2^N subsets + up to N recursive calls for backtrack.
def subsets(nums):
    output = []
    for k in range(len(nums) + 1):
        backtrack(0, [], k, output, nums)
    return output

# Generate all subsets of curr for length k starting from startIdx.
def backtrack(startIdx, curr, k, output, nums):
    if len(curr) == k:
        output.append(curr[:])
        return

    for i in range(startIdx, len(nums)):
        curr.append(nums[i])
        print(curr)

        # Start from the next integer
        backtrack(i + 1, curr, k, output, nums)

        curr.pop()