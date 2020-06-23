# Create a freq map, find the key with a value of 1.
# O(N) time, N iterations to build, N/3 to find.
# O(N) space, N/3 + 1 elements in the freq map since each number except one appears 3 times.
def singleNumber(nums) -> int:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num in freq:
        if freq[num] == 1:
            return num

# How is anyone supposed to come up with this.
# Use two bitmaps, xor the num with the bitmaps, the number that 
# appears in seen once only appears once.
# This is due to the fact that xor is communative, ie:
# num = num ^ 3, num = num ^ 2 yields num = 1. num = num ^ 2, num = num ^ 3 will return 0.
# A number xored with a specific number an odd number of times will remove itself from the xor and
# not affect other numbers xored with it.
# You can implement the infamous swap with no tmp:
# a = 1
# b = 2
# a = a^b # a is now a xor b
# b = a^b # b is now a xor b xor b or just a
# a = a^b # a is now a xor b xor a or just b
def singleNumber(nums) -> int:
    seen_once = 0
    seen_twice = 0
    
    for num in nums:
        # first appearance: 
        # add num to seen_once 
        # don't add to seen_twice because of presence in seen_once
        
        # second appearance: 
        # remove num from seen_once 
        # add num to seen_twice
        
        # third appearance: 
        # don't add to seen_once because of presence in seen_twice
        # remove num from seen_twice
        seen_once = ~seen_twice & (seen_once ^ num)
        seen_twice = ~seen_once & (seen_twice ^ num)

    return seen_once