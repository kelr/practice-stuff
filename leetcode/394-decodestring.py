# Loop through the string, determine the repeat number then 
# extract the substring from outer brackets. Call this recursively with the sub str.
# O(N) time, single pass through the string
# O(N) space, potentially could have a N-3 length substring, also each 
# recursive call is space on the call stack with one call per bracket.
def decodeString(s: str) -> str: 
    out = ""
    i = 0
    while i < len(s):
        if isInt(s[i]):
            # Get and convert the number of repeats
            repeats = s[i]
            subStr = ""
            i += 1
            while isInt(s[i]):
                repeats += s[i]
                i += 1
            repeatNum = int(repeats)
            
            # Extract the substring within the outer brackets
            openBrackets = 0
            while i < len(s):
                if s[i] == '[':
                    openBrackets += 1
                    if openBrackets > 1:
                        subStr += s[i] 
                elif s[i] == ']':
                    if openBrackets > 1:
                        subStr += s[i]
                    openBrackets -= 1
                else:
                    subStr += s[i]
                if openBrackets == 0:
                    break
                i += 1
                
            out += decodeString(subStr) * repeatNum
        else:
            out += s[i]
        i += 1
    return out
            

def isInt(i: int) -> bool:
    try:
        int(i)
    except:
        return False
    else:
        return True

assert "aaabcbc" == decodeString("3[a]2[bc]")
assert "accaccacc" == decodeString("3[a2[c]]")
assert "abcabccdcdcdef" == decodeString("2[abc]3[cd]ef")
assert "abccdcdcdxyz" == decodeString("abc3[cd]xyz")
assert "aaabFFFFcbFFFFc" == decodeString("3[a]2[b4[F]c]")

