
# 23 ish
# Check if the array len is divisible by k. If not, theres no way
# that it can create k subarrays with matching lengths.
# Build a frequency map. 
# For each possible subarray, find the minimum num value in the
# freq array. Check that the values between minVal and minVal+k
# exist in the array. If not, then return False. If there is, subtract
# from the freq array until the freq is 0. If a freq is 0, delete the entry.
# O(N^2) time, O(N) to build the map + O(N) * O(N/K * K) = O(N^2) time to find the min and loop through values.
# O(N) space, there are N elements in total across all subarrays.
def isPossibleDivide(nums, k: int) -> bool:
    if len(nums) % k != 0:
        return False
    
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for _ in range(len(nums)//k):
        minVal = min(freq.keys())
        for _ in range(k):
            if minVal not in freq:
                return False
            
            freq[minVal] -= 1
            
            if freq[minVal] == 0:
                del(freq[minVal])
                
            minVal += 1
    return True

# Same idea as above, but don't search for the min key each time, just sort it once.
# O(N + MlgM*K) where M is the number of unique numbers in nums and N is len of nums.
# O(N) space.
def isPossibleDivide(nums, k: int) -> bool:
    if len(nums) % k != 0:
        return False
    
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num in sorted(freq.keys()):
        if freq[num] > 0:
            for offset in range(k)[::-1]:
                if num + offset not in freq:
                    return False

                freq[num + offset] -= freq[num]

                if freq[num + offset] < 0:
                    return False
    return True


# Need to take into account a followup if K is a huge number.