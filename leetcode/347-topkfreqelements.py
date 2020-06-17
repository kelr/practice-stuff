import heapq

# Create create a frequency map of all the numbers. Create a max heap priority queue
# and push [frequency, number] into the pq. Pop out and return the first k elements from the pq.
# O(NlgN+KlgN) time, N is the number of elements, k is how many top elements we want.
# N iterations to build the freq map, NlgN to insert into the heap, KlgN to pop from the heap.
# O(N) space, N elements for the freq map, N elements for the heap.
def topKFrequent(nums, k: int):
    heap = []
    heapq.heapify(heap)
    
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num in freq:
        # Multiply freq by -1 to use max heap instead of min heap
        heapq.heappush(heap, [freq[num] * -1, num])
        
    out = []
    for _ in range(k):
        out.append(heapq.heappop(heap)[1])
    return out

# Satisfy the less than O(NlgN) runtime by only maintaining k elements in the heap.
def topKFrequentFaster(nums, k: int)
    # If k equals the length of the array, every element must be unique
    # So every element is part of the k most freq elements.
    if k == len(nums):
        return nums
    
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 

    return heapq.nlargest(k, freq.keys(), key=freq.get) 