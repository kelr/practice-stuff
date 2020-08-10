# Consider the set of all possible largest sums. The smallest possible sum is the
# largest number in the array, since all elements in the array are non-negative.
# The largest possible sum is the sum of all the elements in the array.
# If we check all the values between these two values, the smallest possible largest sum must be one of them.
# Since this array is monatonically increasing, we can use binary search to find the minimum
# possible largest sum for an array split into at most m subarrays.

# O(N * lg(sum(N)-max(N))) time. Each threshold check takes N time where N is the length of nums.
# Binary search takes lg(sum of all values in N - max value in N) time.
# O(1) space.
def splitArray(nums, m) -> int:
    # Minimum possible largest sum is the largest value in the array since array is all non-negative
    start = max(nums)
    
    # Maximum possible largest sum is the sum of the entire array
    end = sum(nums)
    
    # Linear search version
    #for threshold in range(start, end):
    #    # The first threshold that works for m subarrays is the minimum largest sum.
    #    if canSplitForThreshold(nums, threshold, m):
    #        return threshold
    
    while start < end:
        mid = start + (end - start) // 2
        if canSplitForThreshold(nums, mid, m):
            end = mid
        else:
            start = mid + 1
        
    return start
        
        
# Greedily determine if it possible create at most maxSubarrays subarrays where the largest sum is at most threshold.
def canSplitForThreshold(nums, threshold, maxSubarrays) -> bool:
    numSubarrays = 1
    subarraySum = 0
    
    for num in nums:
        # If threshold has been passed, put this number in the next subarray instead.
        if subarraySum + num > threshold:
            subarraySum = num
            numSubarrays += 1
            
            # Impossible to maintain threshold sum with this amount of subarrays
            if numSubarrays > maxSubarrays:
                return False
        else:
            subarraySum += num
            
    return True


# Brute force recursive solution
# O(N^M) time
# O(1) space
def splitArray(nums, m) -> int:
    if not nums:
        return 0
    if m == 1:
        return sum(nums)

    minLargestSum = float('inf')
    for i in range(1, len(nums) + 1):
        left = sum(nums[:i])
        right = self.splitArray(nums[i:], m-1)
        minLargestSum = min(minLargestSum, max(left, right))

    return minLargestSum