# Exceeds time. 1:18:31
# I dunno man just use cumsum. Brute force is O(N^3) if you calculate sum per iteration.
# Using cumsum its O(N^2).
def subarraySum(self, nums: List[int], k: int) -> int:
    self.memo = {}
    self.precompute(nums)
    out = 0
    for i in range(len(nums)):
        for j in range (i+1, len(nums)+1):
            if self.sum(i, j, nums) == k:
                out += 1
    return out

def precompute(self, nums):
    j = 2
    self.memo[(0,1,)] = nums[0]
    while j < len(nums)+1:
        self.memo[(0,j,)] = self.memo[(0,j-1,)] + nums[j-1]
        j += 1

def sum(self, i, j, nums):   
    if (i,j,) in self.memo:
        return self.memo[(i,j,)]
    self.memo[(i,j,)] = self.memo[(0,j,)] - self.memo[(0,i,)]
    return self.memo[(i,j,)]


# Make a map that stores all the cumulative sums seen, initialize with a sum of 0 to 1.
# Iterate through nums and generate a cumulative sum s. If s - k appears in the cumsum map,
# that means we are currently (at s) a distance of k away from that cumsum, increment count by how many
# times that cumsum has appeared.
# O(N) time single pass
# O(N) space, N elements in map
def subarraySum(self, nums: List[int], k: int) -> int:
    count = 0
    s = 0
    m = {0:1}
    for i in range(len(nums)):
        s += nums[i]
        if s - k in m:
            count += m[s - k]
        
        if s in m:
            m[s] += 1
        else:
            m[s] = 1
            
    return count