import re
# Filter out non alphanumeric characters from the lowercased string and compare it to the reversed version.
# O(N), N to lower the string, N to remove alphanumeric chars, N to reverse the string and N to compare them.
# O(N), filtered and reversed string takes N space
def isPalindrome(s: str) -> bool:
    cleanString = re.sub('[^a-z0-9]', '', s.lower())
    return cleanString == cleanString[::-1]

# Two pointer solution. Ignore non alphanumeric characters.
# O(N), iterates N/2 times
# O(1) space
def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:

        # Make left skip non alpha numeric chars
        while left < right and not s[left].isalnum():
            left += 1

        # Make right skip non alpha numeric chars
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True