# Find the first element, mark its index, then keep going untill the element is no longer found marking the end index
# as the array is iterated. 
# O(N) time since the entire array is iterated through once.
# Could end the search early if no longer found. Still linear.
# O(1) space
def searchRangeBrute(nums, target):
    out = [-1, -1]
    found = False

    for i, num in enumerate(nums):
        if num == target:
            if not found:
                found = True
                out[0] = i
            out[1] = i
    return out

# Use binary search to find the target value, if found search around for its start and end index.
# O(lgN) time since each search reduces the size of the array to search by half
# O(lgN) space since each recursive call adds to the call stack, one call per halving of the array.
def searchRange(nums, target):
    # Handle empty input
    return [-1, -1] if not nums else searchHelper(nums, target, 0, len(nums) - 1)

def searchHelper(nums, target, start, end):
    out = [-1, -1]

    # Single element base case
    if start == end:
        return out if nums[start] != target else [start, end]

    mid = (end+start) // 2

    # If the target is found, search around for the endings
    if target == nums[mid]:
        start = mid
        end = mid
        curr = mid

        # Find left index
        curr = mid - 1
        while curr >= 0:
            if nums[curr] == target:
                start = curr
            curr -= 1

        # Find right index
        curr = mid + 1
        while curr < len(nums):
            if nums[curr] == target:
                end = curr
            curr += 1

        return [start, end]

    # Recurse left if target is less than the mid, right if it is greater
    elif target < nums[mid]:
        out = searchHelper(nums, target, start, mid)
    else:
        out = searchHelper(nums, target, mid+1, end)
    return out

print(searchRange([1,1,2], 1))