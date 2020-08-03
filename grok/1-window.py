
# Sum up subarrays of size k within arr. Save the largest one.
# All values in arr are positive and k is positive.
# If K > len(arr), will return 0.
# O(N*K) time, N-K subarrays are built each of length K.
# O(1) space
def maxSubarrayOfSizeK(k, arr):
    currMax = 0

    for i in range(len(arr) - k + 1):
        currSum = 0
        for j in range(i, i + k):
            currSum += arr[j]
        currMax = max(currSum, currMax)

    return currMax

# Create a size k sliding window.
# O(N) time, single pass through the array.
# O(1) space
def maxSubarrayOfSizeKLinear(k, arr):
    currMax = 0
    start = 0
    currSum = 0
    for i in range(len(arr)):
        currSum += arr[i]

        windowSize = i - start + 1
        # Output then move the window when the size hits k
        if windowSize >= k:
            currMax = max(currMax, currSum)
            currSum -= arr[start]
            start += 1

    return currMax

# Loop through all sizes from 1 to N. 
# For each possible size, create sliding window subarrays of that size and determine the sum.
# If the sum is >= than s, return the size. If none exist, return 0.
# O(N^2), N sizes possible, checking each subarray of a particular size takes O(N) time.
# O(1) space
def smallest_subarray_with_given_sum(s, arr):
    for size in range(1, len(arr) + 1):
        currSum = 0
        start = 0
        for i in range(len(arr)):
          currSum += arr[i]
          if i - start + 1 >= size:
              if currSum >= s:
                return size
              currSum -= arr[start]
              start += 1
    return 0

# Single pass version. Build a variable sized sliding window until the sum is >= s.
# Then shrink the window until it is no longer the case. Maintain the smallest window size where
# sum >= s. Return that smallest size or 0 if no sum is >= s.
# O(N) time, worst case is a size N window is built, then shrunk N times leading to N+N.
# O(1) space
def smallest_subarray_with_given_sum(s, arr):
    minSize = float('inf')
    currSum = 0
    start = 0
    for i in range(len(arr)):
        currSum += arr[i]

        while currSum >= s:
            minSize = min(minSize, i - start + 1)
            currSum -= arr[start]
            start += 1

    if minSize == float('inf'):
        return 0
    return minSize

# Create a sliding window and add characters into a frequency map as they appear.
# If the length of the freq map exeeds k, the current window has more than k distinct chars.
# So delete chars from the front of the window and shrink it until the freq map no longer has
# more than k chars.
# Save the longest length thus far where there is less than k distinct chars.
# O(N) time. String is iterated through once, deletions only happen once per char for N+N total.
# O(K) space, freq map stores up to k characters.
def longest_substring_with_k_distinct(string, k):
    freq = {}
    maxLen = 0
    start = 0
    for i in range(len(string)):
        # Add the current char into the freq map or increment its count
        if string[i] not in freq:
            freq[string[i]] = 0
        freq[string[i]] += 1

        while len(freq) > k:
            freq[string[start]] -= 1
            if freq[string[start]] == 0:
                del freq[string[start]]
            start += 1

        maxLen = max(maxLen, i - start + 1)

    return maxLen

# Create a set of all the characters in the current sliding window.
# Add characters to the charSet if it is not already there and keep track of the maximum length so far.
# If a new character already exists in the set, pop off chars in the charSet from the start
# of the sliding window until that character no longer exists in the set. 
# O(N) time, N iterations through the string with N-1 pop-offs for N + N-1 which is O(N)
# O(1) space, the size of the charset is number of distinct chars in the string.
# If the string is lowercase english letters only there will be a maximum of 26
# elements in the charSet, thus using constant space.
def non_repeat_substring(string):
    charSet = set()
    maxLen = 0
    start = 0
    for i in range(len(string)):
        # Remove chars from the set from the start of the sliding window until the new char
        # no longer shows up in the charset.
        while string[i] in charSet:
            charSet.remove(string[start])
            start += 1

        if string[i] not in charSet:
            charSet.add(string[i])
            maxLen = max(maxLen, len(charSet))

    return maxLen

# Create a sliding window and add chars occurances into a freq map.
# Keep track of how many times the most repeated character in the window occurs.
# If the size of the window - most repeats is ever > than K, we need to shrink the window.
# O(N) single pass through the string
# O(1), if the charset is only lowercase english letters the size of the freq map will be limited to 26.
def length_of_longest_substring(string, k):
    freq = {}
    maxLen = 0
    start = 0
    maxRepeat = 0
    for i in range(len(string)):
        windowSize = i - start + 1

        # Add the current char into the freq map or increment its count
        if string[i] not in freq:
            freq[string[i]] = 0
        freq[string[i]] += 1

        # Keep track of how many times the most repeated letter repeats.
        maxRepeat = max(maxRepeat, freq[string[i]])

        # If the size of the window - the occurances of the most repeated letter 
        # is larger than k, we need to shrink the window since we cannot replace more than k chars.
        if (windowSize - maxRepeat) > k:
            freq[string[i]] -= 1
            start += 1
            windowSize -= 1

        maxLen = max(maxLen, windowSize)
    return maxLen

# Create a sliding window and count the number of zeroes seen.
# If the number of zeroes ever exeeds K, shrink the sliding window until the number of zeroes returns under K.
# Keep track of the longest length where the number of zeroes is <= k.
# O(N) time, iterate through the string once with N iterations + at most there can be N additional pops.
# O(1) space.
def length_of_longest_substring(arr, k):
    numZeroes = 0
    start = 0
    maxLen = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            numZeroes += 1

        while numZeroes > k:
            if arr[start] == 0:
                numZeroes -= 1
            start += 1

        maxLen = max(maxLen, i - start + 1)
    return maxLen