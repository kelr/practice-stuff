# Loop through the string and place characters in their corresponding spots in the output.
# O(N) time, single pass through s.
# O(N) space, output list takes N elements.
def restoreString(s, indices):
    outputString = [None] * len(indices)
    
    for i, char in enumerate(s):
        outputString[indices[i]] = char
        
    return "".join(outputString)