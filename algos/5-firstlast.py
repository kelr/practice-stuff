"""
Given a sorted array and a target int, find the first and 
last indicies of the number

Ex:
[1, 3, 3, 5, 7, 8, 9, 9, 15], target = 9

return [6, 7]

"""
""" 
Planning:
    Array is sorted, use binary search 
        pass low index and high index
    Find curr = middleindex, 
    if len(array) == 1:
        if curr == target:

        else:    
            return []
    if curr == target:
        while(arr[middleindex] == target):
            middleindex--
        
    recurse on left subarray if curr > target, recurse right if curr < target


Complexity

"""
class Solution:
    def get_range(self, arr, target):
        return self.get_range_recursive(arr, target, 0, len(arr)-1)

    # O(lgN) where N is the size of the array. O(1) space.
    def get_range_recursive(self, arr, target, low, high):
        start_index = -1
        end_index = -1

        # Not found
        if high < low:
            return [start_index, end_index]

        mid = low + (high - low) // 2

        # Search for the first element if we found one of them
        if arr[mid] == target:
            # Find the first occurance
            while(arr[mid] == target and mid != 0):
                mid -= 1

            # Compensate if the beginning is not a target number
            if mid > -1 and arr[mid] != target:
                mid += 1
            start_index = mid

            # Find the last occurance
            while(arr[mid] == target and mid != high):
                mid += 1

            # Compensate if the end is a target number
            if mid < high + 1 and arr[mid] != target:
                mid -= 1
            end_index = mid

            return [start_index, end_index]

        # Recurse right
        if target > arr[mid]:
            return self.get_range_recursive(arr, target, mid+1, high)
        # Recurse left
        else:
            return self.get_range_recursive(arr, target, low, mid)


    # O(N) where N is size of the array. O(1) space.
    def get_range_brute_force(self, arr, target):
        start_index = -1
        end_index = -1
        for i, num in enumerate(arr):
            if num == target:
                if start_index == -1:
                    start_index = i
                else:
                    end_index = i
        return [start_index, end_index]

arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
print(Solution().get_range(arr, 15))
#assert Solution().get_range(arr, 16) == [6, 8]
assert Solution().get_range_brute_force(arr, 9) == [6, 8]