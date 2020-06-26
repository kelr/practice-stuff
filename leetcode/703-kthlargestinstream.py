class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums, reverse=True)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.append(val)
        # In place sort
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]



# Use a min-heap of size k built from nums. The kth largest element is the head.
# If a value larger than the head comes along, pop the head and push the new element.
# If the heap is smaller than size k, push values in.
# O(NlgK), NlgK to create the heap, each add is O(lgK).
# O(K), heap is at most size k. Can be O(1) if you re-use nums.
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            # Heapreplace is just a heappop followed by a heappush. Its more efficient.
            # See: https://docs.python.org/3.8/library/heapq.html#heapq.heapreplace
            heapq.heapreplace(self.nums, val)
        return self.nums[0]