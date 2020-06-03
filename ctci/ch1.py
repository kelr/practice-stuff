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

########################
# 1.6

# Check if the current char is the previous char, if not append to the output string.
# Increment count of the current char each time
# Return original string if the output is equal or larger.
# O(N) if string concatentation does not create a new string object each time otherwise O(N + k^2. Single pass to count the chars. Could probably just join on a list.
# O(N) space as the most the output string can be is 2N.
def compress(s :str) -> str:
    if not s:
        return ""
    count = 0
    prev = s[0]
    out = ""
    for char in s:
        if prev != char:
            out += prev + str(count)
            count = 0
            prev = char
        count += 1
    out += prev + str(count)
    print(out)           
    return s if len(out) >= len(s) else out

assert "a2b1c5a3" == compress("aabcccccaaa")
assert compress("aaabbdndddskkkklsss") == "a3b2d1n1d3s1k4l1s3"

#####################
# 1.7

# Create a new NxN image and fill it with the rotated positions.
# O(N^2) due to having to iterate through N^2 values
# O(N^2) due to creation of a new image
def rotate(img, N):
    out = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(N):
        for j in range(N):
            out[j][N-i-1] = img[i][j]
    return out

# Swap elements layer by layer in a clockwise fashion.
# O(N^2) due to having to iterate through N^2 values
# O(1) space, swap is done in place
def rotateInPlace(img, N):
    for layer in range(N//2):
        first = layer
        last = N - 1 - layer
        for i in range(first, last):
            offset = i - first
            # Save top layer for later
            top = img[first][i]
            # Put left on top
            img[first][i] = img[last-offset][first]
            # Put Bottom on left
            img[last-offset][first] = img[last][last-offset]
            # Put right on bottom
            img[last][last-offset] = img[i][last]
            # Put top on right
            img[i][last] = top
img = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
result = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]  
rotateInPlace(img,4)

for i in range(4):
    for j in range(4):
        assert img[i][j] == result[i][j]

########################
# 1.8

# Find values in the matrix where they are 0 and add them to a rows or cols list. Iterate through the list and zero those rows and cols.
# O(N*M) time, N*M to iterate through matrix + at worst N*M rows and at worst N*M cols (if they are already all zeroes).
# O(N+M) space, N potential rows, M potential cols.
# Could use O(1) space if you use the first row and first col as the rows and cols. Just mark seperately if they themselves need to be zeroed.
def zero(matrix):
    if not matrix or not matrix[0]:
        return False
    N = len(matrix)
    M = len(matrix[0])
    rows = []
    cols = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    for row in rows:
        for j in range(M):
            matrix[row][j] = 0
    for col in cols:
        for i in range(N):
            matrix[i][col] = 0 

img = [[1,2,0,4],[5,6,7,8],[9,10,11,0],[13,14,15,16]]
zero(img)
print(*img, sep='\n')

######################
# 1.9

# Find a rotation point in s1 where the split strings are substrings in s2.
# O(N^2) time since N iterations of N length slices.
# O(N^2) space since slices of total length N must be created for each of the N iterations
def rotation(s1: str, s2:str) -> bool:
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    for i in range(0, len(s1)):
        if s1[0:i] in s2 and s1[i+1:] in s2:
            return True
    return False

# Better way to do it is that s2 will always be a substring of s1 + s1
# O(N) assuming substring is O(A+B) where A and B are string lengths.
# O(N) space since a new string of length 2 & s1 is created/
def rotation2(s1: str, s2: str) -> bool:
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False
    return s2 in s1 + s1
    

assert rotation("waterbottle", "erbottlewat")
assert rotation("waterbottle", "rbottlewate")
assert not rotation("waterbottle", "bottlewattr")
assert not rotation("","")

assert rotation2("waterbottle", "erbottlewat")
assert rotation2("waterbottle", "rbottlewate")
assert not rotation2("waterbottle", "bottlewattr")
assert not rotation2("","")
