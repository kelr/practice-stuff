# Compare every pair
# O(N^2) time
# O(1) space
def numIdenticalPairs(nums) -> int:
    goods = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                goods += 1
    return goods


# Create a freq map. For each number, the number of good pairs is
# N(N-1)/2. Sum them all up.
# O(N) time
# O(N) space
def numIdenticalPairs(nums) -> int:
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    s = 0
    for num in freq:
        s += (freq[num] * (freq[num] - 1)) // 2
    return s