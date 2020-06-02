# Sort a copy of the array then compare each element with the corresponding other one
# Increment out per mismatch
# O(NlgN) since sort is NlgN + N iterations for comparison
# O(N) space since a copy of the array is created when sorting
def heightCheckerBrute(heights) -> int:
    correctOrder = sorted(heights)
    out = 0
    for i in range(0, len(heights)):
        if correctOrder[i] != heights[i]:
            out += 1
    return out

# Create a freqency table with a 101 length array since height values are limited from 1 to 100.
# Freq table indicies are heights, values are the number of times that height appears.
# Then loop through each value of the height while incrementing curr which is what value the height should be.
# If the value of height differs from what it should be, increment out by one.
# O(N) time, N iterations to fill the freq table, and N with a constant amount of iterations for curr to compare.
# O(1) space since freq is limited to 101 elements. 
def heightCheckerFreq(heights) -> int:
    # Use 101 and just skip 0 to keep the indexes not confusing.
    freq = [0] * 101
    out = 0
    curr = 1
    for val in heights:
        freq[val] += 1
    for val in heights:
        while freq[curr] == 0:
            curr += 1
            if curr > len(freq) - 1:
                print("inner")
                return out
        freq[curr] -= 1
        if curr != val:
            out += 1
    return out


print(heightCheckerFreq([5,1,2,3,4]))
