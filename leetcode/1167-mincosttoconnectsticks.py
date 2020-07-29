# The minimum current cost is to combine the two smallest sticks available.
# Sort the sticks and combine the two smallest. Append the combined stick back into the list.
# O(NlgN), sorts the sticks once, then does N-1 binary inserts on the sorted sticks. Sticks remains sorted
# after removal of the 2 smallest elements.
# O(1), sorting, removal of the smallest stick and the re-insertion of the new stick are all done in place.
class Solution:
    def connectSticks(sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        
        sticks.sort()
        totalCost = 0
        while len(sticks) > 1:
            smallest = sticks.pop(0) + sticks.pop(0)
            totalCost += smallest
            binaryInsert(sticks, smallest)
        return totalCost

# Iteratively finds the index that value can be inserted into in a sorted array.
def binaryInsert(array, value):
    lo = 0
    hi = len(array)

    while lo < hi:
        mid = (lo + hi) // 2

        if array[mid] < value: 
            lo = mid + 1
        else: 
            hi = mid
            
    array.insert(lo, value)
            

# Min Heap solution. Min-heapify the sticks and pop off the smallest 2 sticks. Then push back the combined stick.
# O(NlgN) time, there will be N-1 * 3lgN pushes/pops
# O(1) space, heap is created inplace and no extra memory is used.
import heapq
def connectSticksHeap(sticks) -> int:
    if len(sticks) == 1:
        return 0
    
    heapq.heapify(sticks)
    minCost = 0
    while len(sticks) > 1:
        current = heapq.heappop(sticks) + heapq.heappop(sticks)
        heapq.heappush(sticks, current)
        minCost += current
            
    return minCost