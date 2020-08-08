# Define start points and endpoints. Add numbers in spiral order by going right, down, left and upward layer by layer.
# After a layer is complete, shrink the layers to access the inner layer.
# O(N*M) time, all elements in the matrix are accessed once
# O(N*M) space, output array is of size N*M.
def spiralOrder(matrix):
    if not matrix:
        return []
    output = []

    # Define startpoints and endpoints
    startRow = 0 
    startCol = 0 
    endRow = len(matrix) - 1 
    endCol = len(matrix[0]) - 1 

    while startRow <= endRow and startCol <= endCol:
        # Move rightward along the start row
        for col in range(startCol, endCol + 1):
            output.append(matrix[startRow][col])

        # Move downward along the end col
        for row in range(startRow + 1, endRow + 1):
            output.append(matrix[row][endCol])

        # Move leftward along the end row
        for col in reversed(range(startCol, endCol)):
            # If there was only one row in the middle, don't double count it since the first loop already did.
            if startRow == endRow:
                break
            output.append(matrix[endRow][col])

        # Move upward along the start row
        for row in reversed(range(startRow + 1, endRow)):
            # If there was only one col in the middle, don't double count it since the first loop already did.
            if startCol == endCol:
                break
            output.append(matrix[row][startCol])

        startRow += 1
        startCol += 1

        endRow -= 1
        endCol -= 1

    return output