
# Have two pointers, on at the beginning, other at the halfway point.
# Add to the output array one after the other.
# O(N) time, N/2 iterations
# O(N) space, output array is the same size as input array
def shuffle(nums, n):
    first = 0
    second = n
    output = 0
    out = [0] * 2 * n

    while second < len(nums):
        out[output] = nums[first]
        output += 1

        out[output] = nums[second]
        output += 1

        first += 1
        second += 1
        
    return out