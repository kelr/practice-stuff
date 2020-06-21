# Modify the array in place with running sum.
# O(N) time
# O(1) space
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] 
    return nums

# Version if we can't modify the input array inplace.
# O(N) time and space
def runningSum2(nums):
    out = [0] * len(nums)
    for i in range(len(nums)):
        out[i] += nums[i] + out[i-1] 
    return out

assert runningSum([1,2,3,4]) == [1,3,6,10]
assert runningSum([]) == []
assert runningSum([1]) == [1]
assert runningSum([-1, -2, -3]) == [-1,-3,-6]