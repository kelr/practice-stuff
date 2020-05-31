# Since any subarray of arr can be reversed, we can reverse length 2 arrays. That is basically swapping values.
# Since we can reverse any number of times, any number can be swapped to another numbers position with enough swaps.
# Therefore, if the freqs of both arrays are the same since they are the same length, then arr can be sub array reversed to target.
# O(N) time since 2N iterations to single pass target and arr.
# O(1) space since the ints in target and arr are between 1 and 1000
def canBeEqual(target, arr) -> bool:
    # 1001 since 0 isnt used, could offset by 1 instead but it might be more confusing
    freq = [0] * 1001
    for num in arr:
        freq[num] += 1
    for num in target:
        freq[num] -= 1
        if freq[num] < 0:
            return False
    return True