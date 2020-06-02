# Create frequency tables for each string, if the running sum ever turns negative, no way S2 can break S1.
# O(N) time, 2N iterations to build the freq tables, O(1) to compare since character set is limited to lowercase ascii.
# O(1) space since freq table size is limited to lowercase ascii (26 chars).
def checkIfCanBreak(s1: str, s2: str) -> bool:
    freqS1 = [0] * 26
    freqS2 = [0] * 26
    for char in s1:
        freqS1[offsetCtoI(char)] += 1
    for char in s2:
        freqS2[offsetCtoI(char)] += 1

    return (checkFreqs(freqS1, freqS2) or checkFreqs(freqS2, freqS1))

def checkFreqs(f1, f2) -> bool:
    curr_sum = 0
    for i in range(0, len(f1)):
        curr_sum += f1[i] - f2[i]
        if curr_sum < 0:
            return False
    return True
   
def offsetCtoI(char: str) -> int:
    return ord(char) - ord('a')



assert checkIfCanBreak("abe", "axy")
assert not checkIfCanBreak("abe", "acd")
assert checkIfCanBreak("leetcodee", "interview")
