# 5:29
# Just make a freq map and find the one thats greater than 1
# O(N) time N to build, N to find
# O(N) space, N-1 elements in the map.
def findDuplicate(nums) -> int:
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num in freq:
        if freq[num] > 1:
            return num

# 1 hour something
# Reduce the problem to finding cycles in a linked list. If you start from
# the first element and make the next index the value of the current element,
# if there is a duplicate number there will be a cycle in the list.
# Use two runners to find the intersection point of the cycle. 
# Then reset the slow runner to the beginning and make the fast runner go at the same pace.
# Where they intersect the second time is the entrance of the cycle and the dupe element.
# This works since the elements are from [1, n], so no element can go back to the 0th index.
# O(N) time, fast will catch back up to slow in at least N iterations. 
# O(1) space
def findDuplicate(nums) -> int:
        slow, fast = 0, 0
        
        # Find the intersection node in the cycle.
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # Reset slow to the beginning and make fast move at 1 node per iter
        # When they meet this time, this is the entrance to the cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow