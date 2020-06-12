
# Loop through the array and circular search each subsequent element for
# the next greater element.
# O(N^2) time, worst case N^2 comparisons if every element is the same
# O(N) space, output array has N elements
def nextGreaterElements(nums):
    out = [-1] * len(nums)
    for i, num in enumerate(nums):
        j = (i + 1) % len(nums)
        while j != i:
            if nums[j] > num:
                out[i] = nums[j]
                break
            j = (j + 1) % len(nums)
    return out
                
# Loop through indicies of the array twice. Push the index to a stack if
# the element of the curr index is less than or equal than the stack head's element.
# Pop the element if the current is greater than the head.
# The two pass lets you handle circular search.
# O(N) time, 2N iterations through 2 copies of the indicies
# O(N) space, output array has N elements.
def nextGreaterElementsOptimal(nums):
    stack = []
    out = [-1] * len(nums)
    iterRange = list(range(len(nums))) * 2
    for i in iterRange:
        while stack and (nums[stack[-1]] < nums[i]):
            out[stack.pop()] = nums[i]
        stack.append(i)
    return out