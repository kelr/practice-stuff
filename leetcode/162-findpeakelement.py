# Binary search the array for the property A[i] < A[i+1] for any i with local maxima.
# We can return any of the peaks.
# O(lgn) time O(1) space
def findPeakElement(nums) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left