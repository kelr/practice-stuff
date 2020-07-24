def get_permutations(string):
    # Generate all permutations of the input string
    out = set()
    backtrack([], list(string), len(string), out)
    return out


def backtrack(curr, source, targetLen, out):
    # Add to the output set if the string is at its target length
    if len(curr) == targetLen:
        out.add("".join(curr))
        return
    
    
    for i, char in enumerate(source):
        # Add the current char from the input and delete it from the possible characters
        curr.append(char)
        
        # Deep copy the input string list and remove the currently added char
        charsLeft = source[:]
        del charsLeft[i]
        
        backtrack(curr, charsLeft, targetLen, out)
        
        # pop off current char
        curr.pop()