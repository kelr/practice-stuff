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
