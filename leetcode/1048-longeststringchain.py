
# 1:04:00
# Create a map of string lengths to lists of sorted strings with that length.
# For each length, determine the maximum possible depth it can chain
# This is done by deleting a character from the string and checking if that character exists 
# In the sorted string map for that length. If it exists, the chain increases by 1. Keep track of the max chain.
# Use memoization to remember precomputed string depth values if that string is encountered again.
# O(N1 * N2 * N3 * N4...) where N1 is the number of elements of that length.
# O(N) total number of strings in the string map is N which is the number of words.
def longestStrChain(words) -> int:
    freq = {}
    for s in words:
        if len(s) not in freq:
            freq[len(s)] = ["".join(sorted(s))]
        else:
            freq[len(s)].append("".join(sorted(s)))

    memo = {}
    keys = sorted(freq.keys())
    maxDepth = 0
    for i in range(keys[-1], keys[0], -1):
        for s in freq[i]:
            depth = rec(s, freq, memo)
            if depth > maxDepth:
                maxDepth = depth
    return maxDepth + 1

def rec(s, freq, memo):
    if (len(s) == 1) or (len(s) - 1 not in freq):
        return 0
    if s in memo:
        return memo[s]
    maxLen = 0
    for i in range(len(s)):
        newStr = s[:i] + s[i+1:]
        out = 0
        for match in freq[len(s)-1]:
            if match == newStr:
                out += 1
                out += rec(newStr, freq, memo)
                if newStr not in memo:
                    memo[s] = out
                if out > maxLen:
                    maxLen = out
            out = 0
    return maxLen


# Sort the words by length, and iterate.
# Create a memo of words and their chain length.
# For each word, generate possible previous words by deleting a character.
# If the previous word is in the memo, the current word's chain length is 1+ the previous.
def longestStrChain(words) -> int:
    memo = {}
    for word in sorted(words, key=len):
        memo[word] = 1
        for i in range(len(word)):
            prevWord = word[:i] + word[i+1:]
            if prevWord in memo:
                memo[word] = max(memo[prevWord] + 1, memo[word])
    return max(memo.values())