# Sort the array and use 3 pointers, have the 2 subsequent pointers converge on each other towards 0.
# O(N^2) time, converging left and right is O(N), called N times
# O(1) space if output is not counted, O(N) if so
def threeSum(nums):
    output = []
    nums.sort()
    
    for i in range(len(nums)):
        # Skip duplicate i values
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # If the value at i is ever > 0, everything after it must be positive and will never sum to 0
        if nums[i] > 0:
            break
            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            
            if currSum < 0:
                # Increment the left pointer to increase the sum closer to 0
                left += 1
            elif currSum > 0:
                # Decrement right pointer to decrease the sum closer to 0
                right -= 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return output