# Iterate through nums, if a zero is found, swap it with the first non zero value it can find.
# If it can't find any non zero values, all the zeroes must be at the end already, or there aren't any.
# Somewhere between O(N) and O(N^2) maybe?? If all zeroes, then N iterations, same with 1 non zero at the end. 
# If all non zeroes, then N iterations.
# Half non zeroes..depends on the positioning. Its probably O(N).
# O(1) space, movement is inplace.
def moveZeroes(nums) -> None:
    if not nums:
        return
    if len(nums) == 1:
        return

    for i,num in enumerate(nums):
        if num == 0:
            for j in range(i+1, len(nums)):
                if nums[j] != 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    break
            else:
                # If the inner loop completed fully, there aren't any non zero values to swap left
                return

# Use two runner pointers that start at the first element. Increment fast until it finds a non zero, then swap it with the slow pointer.
# Increment the slow pointer.
# O(N) single pass of nums
# O(1) space
def moveZeroesRunner(nums) -> None:
    if not nums:
        return
    if len(nums) == 1:
        return

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1


val = [0,1,0,3,12]
moveZeroesRunner(val)
assert val == [1,3,12,0,0]
