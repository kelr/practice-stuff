# Binary search the array since the property A[i] < A[i+1] only holds true for
# one continuous portion of the array. 
# O(lgn) time O(1) space
def peakIndexInMountainArray(A) -> int:
    left = 0
    right = len(A) - 1
    
    while left < right:
        mid = (left + right) // 2
        if A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            right = mid
            
    return left