# Make freq map and count freqs above 1.
# O(N) time, N pass to build, up to N/2 to loop through all elements of the map.
# O(N) space, up to N/2 elements in map.
def findDuplicates(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    out = []
    for num in freq:
        if freq[num] > 1:
            out.append(num)
    return out

# Use the value of the array - 1 as an index. Negate the value at the index.
# If the value appeard twice, an index will be negative twice and be positive.
# Find all positive values. If value-1 of that index is postive it appears twice.
# O(N) time, two passes of N
# O(1) space, O(N) if output array is counted
def findDuplicates(nums):
    out = []
    
    for num in nums:
        nums[abs(num)-1] *= -1
    
    for num in nums:
        if nums[abs(num) - 1] > 0:
            out.append(abs(num))
            nums[abs(num)-1] *= -1
    return out


# Single pass version
# O(N), O(1) (technically N space for output)
def findDuplicates(nums):
    out = []
    for num in nums:
        # If the index value is negative, we've seen it before so append
        if nums[abs(num) - 1] < 0:
            out.append(abs(num))
        else:
            nums[abs(num)-1] *= -1
    return out