import heapq

# Create a max heap from the nums array. Pop off k elements and return the
# last popped element.
# O(NlgN) time, NlgN to create the heap, KlgN to pop from the heap, however k can be at most N.
# O(N) space, heap has at most N elements.
def findKthLargest(nums, k: int) -> int:
    heap = []
    heapq.heapify(heap)
    
    # Multiply the value by -1 to use max heap
    for num in nums:
        heapq.heappush(heap, -1 * num)
    
    val = 0
    curr = 0
    while curr != k:
        val = heapq.heappop(heap)
        curr += 1
    return val * -1

# Can technically make it faster by only keeping at most k elements in the heap.
# O(NlgK) time to create the max heap. Becomes O(NlgN) if k = N.
# O(K) space, heap has most K elements. Becomes O(N) if k = N.
def findKthLargestOneLine(nums, k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

# Use quick select for O(N) average and O(N^2) worst time.