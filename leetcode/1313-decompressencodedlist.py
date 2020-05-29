def decompressRLElist(nums):
    out = []
    for i in range(0, len(nums), 2):
        for j in range(0, nums[i]):
            out.append(nums[i+1])
    return out

# Iterate every 2 elements in nums, create a new list depending on [freq, num] and append that to the out list.
# O(N) time since the loop over the list takes N/2 iterations, but since nums is limited in length its technically O(1)
# O(N) space since a linear amount of new list elements are created at output which is O(N*F). This is basically O(N^2) if F and N are both large and are of
# similar magnitude. F is capped at 100 though, so its just O(N).
# Technically O(1) since nums is limited in length.
def decompressRLElistcomp(nums):
    out = []
    # Concatting a list comp is much faster than individual appends
    for i in range(0, len(nums), 2):
        out += [nums[i+1] for _ in range(0, nums[i])]
    return out