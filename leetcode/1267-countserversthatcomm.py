
# Maintain the amount of servers seen on each row and column.
# If a specified row and column each have 1 server, and their intersection point
# has a server, that server must be isolated.
# Return the total number of servers - isolated servers.
# O(N*M) where N is the number of rows and M is the number of cols. 
# Since N*M to build the count lists + N*M to iterate through them.
# O(N*M) space, N elements for rows and M elements for cols.
def countServers(grid) -> int:
    rowCount = [0] * len(grid)
    colCount = [0] * len(grid[0])
    
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                rowCount[row] += 1
                colCount[col] += 1
                
    isolated = 0
    for i, row in enumerate(rowCount):
        for j, col in enumerate(colCount):
            if row == 1 and col == 1 and grid[i][j] == 1:
                isolated += 1

    return count - isolated