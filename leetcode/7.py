
# O(N) time, where N is the number of digits. O(1) space.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        int32_max = 2**31
        output = ""
        is_neg = False
        if x < 0:
            is_neg = True
            x *= -1
        
        num_digits = len(str(x))
            
        # Extract most sig to least sig digits, append to output list
        for i in range(0, num_digits):
            val = (x // 10**i) % 10
            output += str(val)
        
        result = int(output)

        # Reapply sign if needed
        if is_neg:
            result *= -1
            
        # Bounds checking
        if result > int32_max-1 or result < -int32_max:
            result = 0
        return result
        
