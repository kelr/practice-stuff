# Array strats
# Sorting
# Auxillary array/map, only when O(1) is not neccesary
# Runner pointers
# Binary search if looking for something or O(lgN) time is needed


# 1.1
# O(N) time, N is chars in string, single pass
# O(N) space, 1 entry in map per character if all are unique
def isUnique(string: str) -> bool:
    char_map = {}
    for char in string:
        if char in char_map:
            return False
        char_map[char] = True
    return True

assert isUnique("")
assert isUnique("abcdefghijklmnopqrstuvwxyz")
assert not isUnique("aaaaaaaaaaaa")
assert not isUnique("asdklfjlskdjfllsdfjksldkfj")
assert isUnique("12345asdf")
assert isUnique("aA")

# O(N^2) time since total operations in worst case is N(N-1)/2
# O(1) space
def isUniqueBrute(string: str) -> bool:
    char_map = {}
    for i, char in enumerate(string):
        for j in range(i+1, len(string)):
            if char == string[j]:
                return False
    return True

assert isUniqueBrute("")
assert isUniqueBrute("abcdefghijklmnopqrstuvwxyz")
assert not isUniqueBrute("aaaaaaaaaaaa")
assert not isUniqueBrute("asdklfjlskdjfllsdfjksldkfj")
assert isUniqueBrute("12345asdf")
assert isUniqueBrute("aA")

# Ask what character set, ASCII extended ASCII or Unicode. Can instead make an array where each char correspondes to an index in the array.
# Technically O(1) time since if length exceeds number of chars in the character set then the string cannot be unique.
# Can use bit vector too.
# Can sort in nlgn and then linearly check. Better than O(n^2)

#############
# 1.2

# O(N+M) where N is length of str1 and M is length of str2 so linear.
# O(N) since each character adds an entry into the map. Could be O(1) since the number of entires cannot exceed the character space.
def isPermutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    char_map = {}
    for char in s1:
        if char not in char_map:
            char_map[char] = 1
        else:
            char_map[char] += 1

    for char in s2:
        if char not in char_map:
            return False
        char_map[char] -= 1
        if char_map[char] < 0:
            return False
    return True

assert isPermutation("a", "a")
assert isPermutation("abba", "abab")
assert not isPermutation("abc", "abd")
assert not isPermutation("a", "aaaaaa")
assert not isPermutation("", "a")
assert not isPermutation("a", "")
assert isPermutation("", "")
assert isPermutation("123abc", "abc123")
assert isPermutation("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")
assert not isPermutation("abcdefghijklmnopqrstuv1xyz", "nopqrstuvwxyzabcdefghijklm")

# Need to know if case sensitive, and white space. Can just use an array mapping like 1.1 but you need to know the character set.


###########
# 1.3

# Two refs to the ending index in the string. Move front until its no longer whitespace. 
# Then copy the character at front to end. If front finds a space now, add %20 at end.
# O(N) since front traverses the array in one pass. 
# O(1) space, replacement is done inplace.
def urlify(s, trueLen: int) -> str:
    front = len(s) - 1
    end = len(s) - 1

    while s[front] == " ":
        front -= 1

    while front >= 0:
        if s[front] == " ":
            s[end] = "0"
            s[end - 1] = "2"
            s[end - 2] = "%"
            end -= 3
        else:
            s[end] = s[front]
            end -= 1
        front -= 1


instr = list("Mr John Smith    ")
urlify(instr, 13)
assert(instr == list("Mr%20John%20Smith"))


#######
# 1.4

# Get the frequency count of all chars in s, then check that there is at most 1 odd frequency count
# Since a palindrome can have 1 odd character count max, it goes in the middle.
# O(N) time since a pass to build the freq table and one pass through the freq table. Freq table has at most N entries.
# O(N) space as there is at most N entires in the freq table (all even counts)
# Can use a bit vector instead to map the 26 characters to bits. 
def isPalindromePermutation(s: str) -> bool:
    return checkAtMostOneOdd(buildFreqTable(s))

def buildFreqTable(s: str) -> dict:
    if not s:
        return {}
    freqTable = {}
    for char in s:
        if char not in freqTable:
            freqTable[char] = 1
        else:
            freqTable[char] += 1
    return freqTable

def checkAtMostOneOdd(freqTable: dict) -> bool:
    if not freqTable:
        return True
    one_odd = False
    for char in freqTable:
        if freqTable[char] % 2 != 0:
            if not one_odd:
                one_odd = True
            else:
                return False
    return True

assert isPalindromePermutation("tactcoapapa")
assert isPalindromePermutation("")
assert isPalindromePermutation("a")
assert not isPalindromePermutation("tactcopapa")


######
# 1.5

# If the strings are the same length, iterate through both of them simultaniously and check each character
# against the other string. False if more than 1 difference exists.
# If the strings are 1 char apart, build a freq table with the shorter one and have the larger one subtract from it
# Return false if there are more than one difference.
# O(N) time as replace will at worst iterate through the length either of the strings. 
# Insert will iterate through both strings seperately for at most N + N-1 iterations. 
# O(1) space if the strings are the same length, O(N) if they are one apart since a freq table is made.
def isOneAway(s1: str, s2: str) -> bool:
    len_s1 = len(s1)
    len_s2 = len(s2)

    # If the length difference is beyond one, no way it could be one edit away
    if abs(len_s1 - len_s2) > 1:
        return False

    if len_s1 == len_s2:
        return isOneAwayReplace(s1, s2)
    elif len_s1 < len_s2:
        return isOneAwayInsertNoTable(s1, s2)
    else:
        return isOneAwayInsertNoTable(s2, s1)

def isOneAwayReplace(s1: str, s2: str) -> bool:
    foundDiff = False
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            if foundDiff:
                return False
            foundDiff = True
    return True

def isOneAwayInsertNoTable(shorter: str, longer: str) -> bool:
    foundDiff = False
    idx1 = 0
    idx2 = 0
    while (idx1 < len(shorter) and idx2 < len(longer)):
        if shorter[idx1] != longer[idx2]:
            if foundDiff:
                return False
            foundDiff = True
        else:
            idx1 += 1
        idx2 += 1
    return True

def isOneAwayInsert(shorter: str, longer: str) -> bool:
    freqTable = buildFreqTable(shorter)
    diffs = 0
    for char in longer:
        if char in freqTable:
            freqTable[char] -= 1
            if freqTable[char] < 0:
                diffs += 1
                if diffs > 1:
                    return False
        else:
            diffs += 1
            if diffs > 1:
                return False
    return True

def buildFreqTable(s: str) -> dict:
    if not s:
        return {}
    freqTable = {}
    for char in s:
        if char not in freqTable:
            freqTable[char] = 1
        else:
            freqTable[char] += 1
    return freqTable

assert isOneAway("pale", "ple")
assert isOneAway("pales", "pale")
assert isOneAway("pale", "bale")
assert not isOneAway("pale", "bake")
assert isOneAway("pale", "pale")
assert isOneAway("", "")
assert isOneAway("", "e")
assert isOneAway("a", "")
