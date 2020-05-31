# Find the 2 largest values in the array. They may be the same value but must be different indicies.
# O(N) time as 2 passes of N iterations
# O(1) space
def maxProduct(nums) -> int:
    max1 = float("-inf")
    max2 = float("-inf")
    maxidx = 0
    max2idx = 1

    for i,num in enumerate(nums):
        if num >= max1:
            max1 = num
            maxidx = i 
    print(maxidx)

    for i,num in enumerate(nums):
        if num >= max2 and i != maxidx:
            max2 = num
            max2idx = i
    print(max2idx)
    return (nums[maxidx]-1) * (nums[max2idx]-1)

# Same as above but maxes are found in a single pass. max1 stores the largest and max2 stores the second largest.
# If a value is bigger than max1 then set max2 to the old max1 and set the num to max1.
# Check if the value is bigger than max2 if it is not bigger or equal to max1.
# O(N) since its done in a single pass of nums
# O(1) space
def maxProductSingle(nums) -> int:
    max1, max2 = 0, 0
    for num in nums:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1 - 1) * (max2 - 1)

# Can instead just sort the array and pick the first 2 elements. The array is guaranteed to be at least length 2.
# O(NlgN) due to sort
# O(1) space if the sort is done in place. list.sort() is in place while sorted(list) is not.
def maxProductSort(nums) -> int:
    nums.sort(reverse=True)
    return (nums[0]-1) * (nums[1]-1)
 
print(maxProductSort([3,7]))