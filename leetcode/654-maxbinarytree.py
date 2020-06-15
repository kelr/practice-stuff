class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Find the maximum value in the tree, create a node with it,
# then recursively call itself with the left slice and the right slice.
# O(N^2) time, if the array is sorted then there are N(N-1)/2 comparisons to find each maximum number
# O(N^2) space, if the array is sorted there are N recursive calls on the stack. Each slice of the array also creates a new array.
# Worst case, this will be a new array with 1 less element for N(N-1)/2 in total.
def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    maxIdx = 0
    for i, _ in enumerate(nums):
        if nums[i] > nums[maxIdx]:
            maxIdx = i
    currNode = TreeNode(nums[maxIdx])
    currNode.left = constructMaximumBinaryTree(nums[0:maxIdx])
    currNode.right = constructMaximumBinaryTree(nums[maxIdx + 1:])
    return currNode


# Same as above but passes start and end index of the original array
# To prevent array copies from slicing.
# O(N^2) time, if the array is sorted then there are N(N-1)/2 comparisons to find each maximum number
# O(N) space, if the array is sorted there are N recursive calls on the stack.
def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    return build(nums, 0, len(nums))

def build(nums, start, end):
    if start >= end:
        return None
    maxIdx = start
    for i in range(start, end):
        if nums[i] > nums[maxIdx]:
            maxIdx = i
    currNode = TreeNode(nums[maxIdx])
    currNode.left = build(nums, start, maxIdx)
    currNode.right = build(nums, maxIdx+1, end)
    return currNode


# Use a stack to keep track of the largest values. Push the first node onto the stack.
# If the curr value is < than the head, set curr as the head's right node and push it onto the stack.
# If the curr value is > than the head keep popping the stack until curr is < than head or the stack is empty.
# Set each popped value to be the left of the current node. Then push the curr node onto the stack.
# O(N) time, single pass through the array
# O(N) space, decending order sort has N stack elements.
def constructMaximumBinaryTreeOptimal(nums):
    stack = [TreeNode(nums[0])]
    for num in nums[1:]:
        currNode = TreeNode(num)
        if num < stack[-1].val:
            stack[-1].right = currNode
        else:
            while stack and stack[-1].val < num:
                currNode.left = stack.pop()
            if stack:
                stack[-1].right = currNode
        stack.append(currNode)
    return stack[0]