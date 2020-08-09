# For each element inside the array except the first and last, check to see
# if it is greater than both of its neighbors. If it is, expand outwards from its neighbors
# to find the full extent of the mountain. Return the max of these lengths.
# O(N) one pass of N, at most finding the length of the mountain takes an additional N
# O(1) space
def longestMountain(A) -> int:
    # A mountain cannot exist if length is less than 3
    if len(A) < 3:
        return 0
    
    maxPeakLen = 0
    for i in range(1, len(A) - 1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            currPeakLen = 3
            
            left = i - 2
            while left >= 0 and A[left] < A[left + 1]:
                currPeakLen += 1
                left -= 1
                
            right = i + 2
            while right < len(A) and A[right] < A[right - 1]:
                currPeakLen += 1
                right += 1
                
            maxPeakLen = max(maxPeakLen, currPeakLen)
            
    return maxPeakLen