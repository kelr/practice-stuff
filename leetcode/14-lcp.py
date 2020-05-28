

# Match the character at a certain index amongst all strings in strs until a mismatch occurs 
# or if the index exceeds the length of a string.
# O(n * m) time, where n is number of strings and m is the length of the shortest string
# O(1) space
def lcp_brute(strs) -> str:
    result = ""
    if len(strs) == 0:
        return result
    if len(strs) == 1:
        return strs[0]

    for i in range(0, len(strs[0])):
        char = match_char(strs, i)
        if char == "":
            return result
        result += char
    return result

# Returns the char if all strings in strs have a matching char at that index
# Returns empty string if mismatch or the index is beyond the length of a string
# Assumes strs has at least one string
def match_char(strs, index):
    curr_char = strs[0][index]
    for string in strs:
        if index >= len(string):
            return ""
        if curr_char != string[index]:
            return ""
    return curr_char




print(lcp_brute(["aa","a"]))


