# Iterative binary search. 
# O(lgN), O(1)
def search(nums, target) -> int:
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

# Recursive binary search. 
# O(lgN), O(lgN)
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)
    
def binarySearchHelper(array, target, lo, hi):
    if lo > hi:
        return -1
    
    mid = (lo + hi) // 2
    
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarySearchHelper(array, target, lo, mid - 1)
    else:
        return binarySearchHelper(array, target, mid + 1, hi)