# Iterate through the grid and push rotting oranges to a queue and count fresh oranges.
# For each rotted orange in the queue, rot its neighbors if they exist.
# O(M*N) where M is the number of rows and N is the number of cols. M*N for the initial pass +
# up to M*N oranges will pass through the rotQueue.
# O(M*N) space, up to M*N oranges will pass through the rotQueue. Worst case is the entire grid is rotten.
def orangesRotting(grid) -> int:
    freshCount = 0
    minutes = 0
    rotQueue = deque()
    rotQueue.append([])
    rowLen = len(grid)
    colLen = len(grid[0])
    
    # Iterate through grid, push rotten oranges to the queue and count the fresh ones
    for row in range(rowLen):
        for col in range(colLen):
            if grid[row][col] == 2:
                rotQueue[0].append((row, col))
            if grid[row][col] == 1:
                freshCount += 1
    
    # If there are not rotting oranges and there are some fresh oranges, impossible to have no fresh oranges
    if not rotQueue and freshCount > 0:
        return -1
    
    # If there are no fresh oranges, it's already solved
    if freshCount == 0:
        return minutes
    
    while rotQueue[0]:
        currentMinute = rotQueue.popleft()
        rotQueue.append([])
        for row, col in currentMinute:
            # Find the rotting orange's neighbors
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                # Only rot it if its within the grid and if the neighbor is fresh
                if i >= 0 and i < rowLen and j >= 0 and j < colLen and grid[i][j] == 1:
                    grid[i][j] = 2
                    freshCount -= 1
                    rotQueue[0].append((i, j))
        minutes += 1
    
    if freshCount > 0:
        return -1
    
    return minutes - 1

# Nicer solution with a delimiter instead of a list inside the queue
def orangesRotting(grid) -> int:
    rotQueue = deque()
    rowLen = len(grid)
    colLen = len(grid[0])
    freshCount = 0
    
    # Iterate through grid, push rotten oranges to the queue and count the fresh ones
    for row in range(rowLen):
        for col in range(colLen):
            if grid[row][col] == 2:
                rotQueue.append((row, col))
            if grid[row][col] == 1:
                freshCount += 1
     
    # Append the first delimiter
    rotQueue.append((-1, -1))
    
    # If there are no fresh oranges, it's already solved
    if freshCount == 0:
        return 0

    minutes = -1
    while rotQueue:
        row, col = rotQueue.popleft()
        
        if row == -1 and col == -1:
            minutes += 1
            # Add a delimiter for the next minute if there are still more oranges to process
            if rotQueue:
                rotQueue.append((-1, -1))
        else:
            for i, j in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if i >= 0 and i < rowLen and j >= 0 and j < colLen and grid[i][j] == 1:
                    grid[i][j] = 2
                    freshCount -= 1
                    rotQueue.append((i, j))
    
    return -1 if freshCount > 0 else minutes

# Interesting solution of creating sets of all rotten and fresh oranges.
# O((MN)^2), since the worst case is if every orange except 1 is rotten. 
# The while loop checks every fresh orange until it finds neighbors that are rotten.
# On average it performs better than BFS though.
# O(MN) space.
def orangesRotting(grid) -> int:
    rottenSet = set()
    freshSet = set()
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                freshSet.add((x,y))
            if grid[x][y] == 2:
                rottenSet.add((x,y))
    
    minutes = 0
    while len(freshSet) > 0:
        newlyRotted = set()
        for x, y in freshSet:
            if (x+1, y) in rottenSet or (x-1, y) in rottenSet or (x, y+1) in rottenSet or (x, y-1) in rottenSet:
                newlyRotted.add((x,y))
                
        if len(newlyRotted) == 0:
            return -1
        
        # Remove newly rotted oranges from the fresh ones
        freshSet.difference_update(newlyRotted)

        # Add any newly rotted oranges to the rotten set
        rottenSet.update(newlyRotted)

        minutes += 1

    return minutes