# Check each location in the grid if it's a land. If it is a land, perform DFS from that point and mark all
# attached lands as visited while incrmenting the number of islands by 1.
# O(N*M) time, checks N*M cells + DFS in the worst case will visit N*M cells in the case the entire grid is "1".
# O(N*M) space, recursion stack in the worst case will be N*M calls.
def numIslands(grid) -> int:
    if not grid or not grid[0]:
        return 0
    
    numIslands = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '1':
                dfs(x, y, grid)
                numIslands += 1
                
    return numIslands
                    
# Perform DFS at the given x, y for all adjacent cells that are lands.
# Mark visited locations in the grid as 2.
def dfs(x, y, grid):
    if grid[x][y] == '1':
        maxX = len(grid)
        maxY = len(grid[0])
        
        # Set this location as visited
        grid[x][y] = '2'
        
        if x + 1 < maxX:
            dfs(x + 1, y, grid)
        if x - 1 >= 0:
            dfs(x - 1, y, grid)
        if y + 1 < maxY:
            dfs(x, y + 1, grid)
        if y - 1 >= 0:
            dfs(x, y - 1, grid)
            
# Faster version to use a set to check visited locations instead of marking them in the grid.
# This prevents recursive calls to previously visited locations at the trade off of more space
# O(N*M) time
# O(N*M) space, N*M calls on the stack in the worst case + N*M visited entries.
def numIslands(grid) -> int:
    if not grid or not grid[0]:
        return 0
    numIslands = 0
    visited = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '1' and (x, y) not in visited:
                dfs(x, y, grid, visited)
                numIslands += 1
                
    return numIslands
                    
# Perform DFS at the given x, y for all adjacent cells that are lands.
# Mark visited locations in the grid as 2.
def dfs(x, y, grid, visited):
    if grid[x][y] == '1':
        maxX = len(grid)
        maxY = len(grid[0])
        
        # Set this location as visited
        visited.add((x, y))
        
        if x + 1 < maxX and (x + 1, y) not in visited:
            dfs(x + 1, y, grid, visited)
        if x - 1 >= 0 and (x - 1, y) not in visited:
            dfs(x - 1, y, grid, visited)
        if y + 1 < maxY and (x, y + 1) not in visited:
            dfs(x, y + 1, grid, visited)
        if y - 1 >= 0 and (x, y - 1) not in visited:
            dfs(x, y - 1, grid, visited)