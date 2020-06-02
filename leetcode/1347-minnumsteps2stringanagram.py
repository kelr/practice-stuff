def minSteps(s: str, t: str) -> int:
    freq = [0] * 26
    count = 0
    for char in s:
        freq[ord(char) - ord('a')] += 1
    for char in t:
        i = offsetCtoI(char)
        if freq[i] == 0:
            count += 1
        else:
            freq[i] -= 1

    return count

def minSteps2(s: str, t:str) -> int:
    freq = [0] * 26
    count = 0
    for i in range(0, len(s)):
        freq[offsetCtoI(s[i])] += 1
        freq[offsetCtoI(t[i])] -= 1
    print(freq)
    for char in freq:
       count += abs(char)

    return count // 2

def offsetCtoI(char: str) -> int:
   return ord(char) - ord('a') 

print(minSteps2("leetcode", "practice"))
