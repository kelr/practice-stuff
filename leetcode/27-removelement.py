
# Start from the first elem and swap it with the last elem if the first is the value.
# If the last element is the value already, decrement return length and decrement the pointer.
# Increment the starting pointer until it is ahead of the end
# O(N) time where N is the number of elements since pointers will move at most N times
# O(1) space as removal is done in place
def removeElement(nums, val:int) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return 0 if nums[0] == val else 1

    count = 0
    start = 0
    end = len(nums) - 1

    while start <= end:
        if nums[end] == val:
            count += 1
            end -= 1
        else:
            if nums[start] == val:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
            start += 1

    return len(nums) - count

print(removeElement([2,2], 2))