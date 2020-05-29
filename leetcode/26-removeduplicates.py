# Use fast/slow runner pointers. Fast always increments. Slow only increments if fast and slow are not equal
# If not equal, increment slow first then move the fast number to the slow number.
# Array must be sorted for this to work.
# O(N) time, worst case is when every number is unique then this alg keeps swapping the same element with itself.
# O(1) space as no new data structures are created
def removeDuplicates(nums) -> int:
    if len(nums) == 0:
        return 0
    slow = 0
    for fast in nums:
        if fast != nums[slow]:
            slow += 1
            nums[slow] = fast
    return slow + 1
