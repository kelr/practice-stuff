# Loop through the string, output non vowel characters.
# O(N) time, loops through entire input string
# O(N) space, output string could be N chars if input has no vowels.
def removeVowels(S) -> str:
    out = []
    for char in S:
        if char not in ["a", "e", "i", "o", "u"]:
            out.append(char)
    return "".join(out)

# One lineeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeer
def removeVowels(S) -> str:
    return "".join([char for char in S if char not in "aeiou"])