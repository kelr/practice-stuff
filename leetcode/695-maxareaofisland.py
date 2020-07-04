# Loop through every element in the grid. Add visited points to a set.
# Don't visit points we've visited. If a point is 1, search all its neighbors for more ones.
# Keep track of the max area of ones.
# O(N*M) time where N is number of rows and M is number of columns.
# O(N*M) space, every node is visited and included in the set + N*M recursive calls in worst case..
def maxAreaOfIsland(grid):
    visited = set()
    maxArea = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            area = search(x, y, grid, visited)
            if area > maxArea:
                maxArea = area
    return maxArea
    
def search(x, y, grid, visited):
    if (x, y) in visited:
        return 0
    
    # Check for edges of the grid
    if x < 0 or x >= len(grid):
        return 0
    if y < 0 or y >= len(grid[0]):
        return 0
    
    if grid[x][y] == 0:
        return 0
    
    area = 1
    visited.add((x,y))

    # Visit all neighbors
    area += search(x+1, y, grid, visited)
    area += search(x-1, y, grid, visited)
    area += search(x, y+1, grid, visited)
    area += search(x, y-1, grid, visited)

    return area


# Same as above but uses less space by setting visited points to 0.
# Only works if input grid is mutable.
# O(N*M) time.
# O(N*M) space since there are N*M recursive calls if every point is 1.
def maxAreaOfIsland(grid):
    maxArea = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            area = search(x, y, grid)
            if area > maxArea:
                maxArea = area
    return maxArea
        
def search(x, y, grid):
    # Check for edges of the grid
    if x < 0 or x >= len(grid):
        return 0
    if y < 0 or y >= len(grid[0]):
        return 0
    
    if grid[x][y] == 0:
        return 0
    
    area = 1
    grid[x][y] = 0

    # Visit all neighbors
    area += search(x+1, y, grid)
    area += search(x-1, y, grid)
    area += search(x, y+1, grid)
    area += search(x, y-1, grid)

    return area