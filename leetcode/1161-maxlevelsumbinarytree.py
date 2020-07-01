from collections import deque

# BFS with levels to find the sum of each level.
# Return the smallest level that has the maximum sum
# O(N) time, N to BFS + N to find the max worst case when N == height of tree
# O(N) space, (N+1)/2 queue max elems if perfect tree which are the leaf nodes, N size of levelSums worst case when N == height of tree
class Solution:
    def maxLevelSum(root) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append((root, 1,))
        levelSums = [0]
        
        while queue:
            node, level = queue.popleft()
            
            if len(levelSums) <= level:
                levelSums.append(node.val)
            else:
                levelSums[level] += node.val
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        maxLevel = 1
        for level, s in enumerate(levelSums):
            if s > levelSums[maxLevel]:
                maxLevel = level
        return maxLevel

# Optimized BFS
# O(N) time, N to BFS.
# O(N) space, queue has (N+1)/2 queue max elems for a perfect tree, since the most the queue will get
# is the number of leaf nodes.
def maxLevelSum(root) -> int:
    if not root:
        return 0
    
    queue = [root]
    levelMax = 1
    currLevel = 1
    currMax = 0
    
    while queue:
        currSum = sum([node.val for node in queue])
        if currSum > currMax:
            currMax = currSum
            levelMax = currLevel

        queue = [child for node in queue for child in [node.left, node.right] if child]
        currLevel += 1

    return levelMax

