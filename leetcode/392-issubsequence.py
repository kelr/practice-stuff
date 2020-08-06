# Check if s is a subsequence of t.
# Maintain the current position inside s. Iterate through t.
# If the char at t is found in s, increment the position until the entire string s is traversed.
# If s is completely traversed, then s must be a subsequence of t.
# O(T) time, where T is the length of t.
# O(1) space
def isSubsequence(s: str, t: str) -> bool:
    # Empty string is always a subsequence of another string.
    if not s:
        return True
    
    sequenceIndex = 0
    for char in t:
        if s[sequenceIndex] == char:
            sequenceIndex += 1

        if sequenceIndex == len(s):
            return True
    return False