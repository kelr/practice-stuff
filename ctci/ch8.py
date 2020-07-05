#################### 
#8.1

# Use Bottom Up DP with backtrack to determine how many ways to run up.
# Maintain a current step count. If the step count matches the goal N,
# this is a valid solution. If it overshoots, then it is invalid.
# If it undershoots, try adding 1 2 or 3 steps again.
# O(3^N) time, each recursion depth can choose from 3 choices.
# O(3^N) space, 3^N nodes in the recursive tree.
def countBottomUp(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return rec(n, 0)

def rec(n, curr):
    if curr == n:
        return 1
    if curr > n:
        return 0
    cnt = 0
    for i in range(1,4):
        curr += i
        cnt += rec(n, curr)
        curr -= i
    return cnt

# assert countBottomUp(-1) == 0
# assert countBottomUp(0) == 1
# assert countBottomUp(1) == 1
# assert countBottomUp(2) == 2
# assert countBottomUp(3) == 4
# assert countBottomUp(4) == 7
# print(countBottomUp(25))

# Use top down DP. The last step was either from a 1 2 or 3 step.
# Add the recursive subtrees of each step. 
# O(3^N) time
# O(N) space, most N recursive calls on the stack at once.
def countTopDown(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return countTopDown(n-3) + countTopDown(n-2) + countTopDown(n-1)

# Top down DP with memo. 
# O(N) time, each subproblem count(N) is computed and stored once.
# O(N) space, memo will have size N + at most N recursive calls on the stack at once.
memo = {
    0: 1
}
def countMemo(n):
    if n < 0:
        return 0

    if n in memo:
        return memo[n]

    memo[n] = countMemo(n-3) + countMemo(n-2) + countMemo(n-1)
    return memo[n]

# assert countMemo(-1) == 0
# assert countMemo(0) == 1
# assert countMemo(1) == 1
# assert countMemo(2) == 2
# assert countMemo(3) == 4
# assert countMemo(4) == 7
# print(countMemo(2993))

#################### 
# 8.2

# Bottom up DP with backtrack. Can either only go +1 x or +1 y.
# O(2^N+M) time, where N is length of x and M is length of y. For each point, there are two choices.
# O(N+M) space, output path if it exists will always be of length N+M.
def robotGrid(grid):
    if not grid or len(grid) == 0:
        return []

    output = []

    rec(0, 0, grid, output)

    return output

def rec(x, y, grid, output) -> bool:
    xMax = len(grid) - 1
    yMax = len(grid[0]) - 1

    # If we exceed boundaries, there is obviously no path.
    if x > xMax or y > yMax:
        return False

    # If the current point is traversable, add it to the path list.
    if grid[x][y] == 1:
        output.append((x, y))

        # Found the end, return True
        if x == xMax and y == yMax:
            return True

        # Havent found the end yet, but if a recursive call did then forward it's success.
        if rec(x+1, y, grid, output) or rec(x, y+1, grid, output):
            return True

        # If we're here, this path doesn't lead to the goal, pop off the current point.
        output.pop()

    return False

grid = [[1, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1]]
print(robotGrid(grid))

# Topdown DP with Memo.
# Start from the goal and check adjacent paths.
# Continue recursing as long as the new point is not out of bounds, not visited before and is traversable.
# If the starting point is reached, return True up the recursion stack and add to the path along the way.
# O(N*M) time, each point is visited only once.
# O(N*M) space, potentially each point could be visited and added to visited but in reality it would be less.
# also N+M space for the output path.
def robotGridTopDown(grid):
    if not grid or len(grid) == 0:
        return []

    path = []
    recTopDown(len(grid)-1, len(grid[0])-1, grid, path, set())

    return path

def recTopDown(x, y, grid, path, visited):
    # Out of bounds
    if x < 0 or y < 0:
        return False

    # Visisted before
    if (x, y) in visited:
        return False

    # Point is not traversable
    if grid[x][y] == 0:
        return False

    # Reached the starting point
    if x == 0 and y == 0:
        visited.add((x, y))
        path.append((x,y))
        return True

    visited.add((x, y))

    if recTopDown(x-1, y, grid, path, visited) or recTopDown(x, y-1, grid, path, visited):
        path.append((x,y))
        return True

    return False

grid = [[1, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 0, 1, 1]]
print(robotGridTopDown(grid))

#################### 
# 8.3

# Use binary search to find the magic index.
# O(lgN) time, each call reduces the problem space by half.
# O(1) space
def magicIndex(start, end, nums):
    if not nums:
        return -1
    if end < start:
        return -1
   
    mid = (end + start) // 2

    if nums[mid] == mid:
        return mid

    if nums[mid] > mid:
        return magicIndex(0, mid, nums)

    return magicIndex(mid, end, nums)

nums = [-40,-20,-1,1,2,3,5,7,9,12,13]
print(magicIndex(0, len(nums)-1, nums))

# If the values in the array are not distinct, search both sides of the array but
# skip values that cannot possibly be magic indexes.
# O(N) time, worst case it searches the entire array like brute force.
# O(1) space.
def magicIndexNonDistinct(start, end, nums):
    if not nums:
        return -1
    if end < start:
        return -1
   
    mid = (end + start) // 2

    if nums[mid] == mid:
        return mid

    leftIdx = min(mid - 1, nums[mid])
    left = magicIndex(0, leftIdx, nums)
    if left >= 0:
        return left

    rightIdx = min(mid - 1, nums[mid])
    return magicIndex(0, rightIdx, nums)

nums = [-10,-5,2,2,2,3,4,7,9,12,13]
print(magicIndexNonDistinct(0, len(nums)-1, nums))