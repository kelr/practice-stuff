# Infect the neighbors of row, col. Newly infected is marked with 2.
def infect(grid, row, col):
    # Infect left
    if row - 1 >= 0:
        if grid[row - 1][col] != 1:
            grid[row - 1][col] = 2 

    # Infect right
    if row + 1 < len(grid):
        if grid[row + 1][col] != 1:
            grid[row + 1][col] = 2 

    # Infect top
    if col - 1 >= 0:
        if grid[row][col - 1] != 1:
            grid[row][col - 1] = 2

    # Infect bottom
    if col + 1 < len(grid[0]):
        if grid[row][col + 1] != 1:
            grid[row][col + 1] = 2 

# Check every person in the grid, return true if everyone is infected
def isAllInfected(grid):
    allInfected = True
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                grid[row][col] = 1
            if grid[row][col] == 0:
                allInfected = False
    return allInfected

def printGrid(grid):
    for row in range(len(grid)):
        print(grid[row])
    print()

# Infect any neighbors of a zombie. Check if everyone is infected.
# O(N*M*D) where N is number of rows and M is number of cols. N*M iterations to determine if 
# all are infected + N*M iterations to mark new infected * D days
# O(1) space.
# 14 mins.
def minHours(grid):
    if not grid or not grid[0]:
        return 0

    days = 0
    while not isAllInfected(grid):
        days += 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    infect(grid, row, col)

    return days

grid = [[0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1, 0, 1]]

assert(minHours(grid) == 5)

from collections import deque
# Find all initial zombies and put them in a queue. Dequeue each zombie
# and infect potential neighbors if valid and queue the new zombies. 
# Continue until there are no more humans.
# More efficient than the brute force since it doesn't have to check every person per day.
# O(N*M) where N is number of rows and M is number of cols. 
# N*M to determine initial zombies + N*M elements passing through the queue.
# 19m
def minHoursBFS(grid):
    if not grid:
        return -1

    # Initialize days to -1 since if there are no zombies, its impossible to infect everyone.
    days = -1
    queue = deque()

    # Append initial zombies
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                queue.append((row, col))

    while queue:
        # Process all the zombies queued up so far for this day
        zombiesToProcess = len(queue)
        for _ in range(zombiesToProcess):
            row, col = queue.popleft()
            infectBFS(grid, row, col, queue)
        days += 1
    return days

def infectBFS(grid, row, col, queue):
    # Infect left
    if row - 1 >= 0:
        if grid[row - 1][col] == 0:
            grid[row - 1][col] = 1 
            queue.append((row - 1, col))

    # Infect right
    if row + 1 < len(grid):
        if grid[row + 1][col] != 1:
            grid[row + 1][col] = 1 
            queue.append((row + 1, col))

    # Infect top
    if col - 1 >= 0:
        if grid[row][col - 1] != 1:
            grid[row][col - 1] = 1
            queue.append((row, col - 1))

    # Infect bottom
    if col + 1 < len(grid[0]):
        if grid[row][col + 1] != 1:
            grid[row][col + 1] = 1 
            queue.append((row, col + 1))


grid2 = [[0, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1, 0, 1]]


assert(minHoursBFS(grid2) == 5)