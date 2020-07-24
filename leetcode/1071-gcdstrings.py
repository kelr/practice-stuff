
# Find all common factors of the lengths of the 2 strings. The potential gcdstring must be of length
# of the gcd of the lengths of the strings.
# O(N+M) time, where N is the length of str1 and M is the length of str2.
# O(N) space, where N is the larger length of the 2 strings.
def gcdOfStrings(str1: str, str2: str) -> str:
    # If the strings are equal length and they are the same, the divisor must be one of them.
    if len(str1) == len(str2):
        if str1 == str2:
            return str1
        else:
            return ""
        
    len1 = len(str1)
    len2 = len(str2)
    commonFactors = []
    
    # Find all common factors between the lengths
    larger = max(len1, len2)
    for i in range(1, larger + 1):
        if len1 % i == 0 and len2 % i == 0:
            commonFactors.append(i)
    
    # Find the gcd of the lengths
    gcd = max(commonFactors)
    
    # Determine the potential gcd string
    substring = str1[:gcd]
    
    # Rebuild the intial strings
    sub1 = substring * (len1 // gcd)
    sub2 = substring * (len2 // gcd)
    
    # If the built strings do not match, there is no gcd
    if sub1 == str1 and sub2 == str2:
        return substring
    return ""


# GCD algorithm imitation. If the longer string is prefixed with the shorter string
# cut off the prefix of the longer string until its empty. The leftover is the gcd string.
# If the longer string is not prefixed by the shorter, theres no gcd.
# O(N^2) time
# O(N^2) space
def gcdOfStrings(str1: str, str2: str) -> str:
    if not str1 or not str2:
        return str1 if str1 else str2
    elif len(str1) < len(str2):
        return gcdOfStrings(str2, str1)
    elif str1[: len(str2)] == str2:
        return gcdOfStrings(str1[len(str2) :], str2)
    else:
        return ''