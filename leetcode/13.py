

# O(N) time where N is the size of the string as it makes one pass. O(1) space.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        prev_char = ""
        for char in s:
            if char == "V" and prev_char == "I":
                total += 3
            elif char == "X" and prev_char == "I":
                total += 8
            elif char == "L" and prev_char == "X":
                total += 30
            elif char == "C" and prev_char == "X":
                total += 80
            elif char == "D" and prev_char == "C":
                total += 300
            elif char == "M" and prev_char == "C":
                total += 800
            else:
                total += values[char]
            prev_char = char
            
        return total
