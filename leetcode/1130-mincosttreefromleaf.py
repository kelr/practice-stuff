# Find the minimum leaf node and determine which of its left or right neighbors
# is smaller. Current leaf * min neightbor allows for the minimum possible cost
# for that node. Add that cost to the total and remove the current leaf from the array.
# Continue until there is only 1 leaf left.
# O(N^2) time, finding the min takes N + N-1 + N-2 + ... + 1 = N(N-1)/2 time.
# O(N) space, each neighbor slice creates at least an array of size 1, leading to N space.
def mctFromLeafValues(arr) -> int:
    out = 0
    while len(arr) > 1:
        # Find min
        minIdx = 0
        for i in range(len(arr)):
            if arr[i] < arr[minIdx]:
                minIdx = i

        # Slice the left and right sides to get a 0 or 1 length arrays
        # containing the neighbors. Concat the lists together and find the
        # minimum val.
        # leftVal = arr[minIdx - 1:minIdx]
        # rightVal = arr[minIdx + 1:minIdx + 2]
        # minVal = min(leftVal + rightVal)

        # Non slice implementation for O(1) space
        if minIdx == 0:
            minVal = arr[minIdx + 1]
        elif minIdx == len(arr) - 1:
            minVal = arr[minIdx - 1]
        else:
            minVal = min(arr[minIdx - 1], arr[minIdx + 1])

        # Minimum cost is the minimum neighbor * the current value. 
        out +=  minVal * arr.pop(minIdx)
    return out

# Create a stack, iterate through arr. If stack head is <= the current arr,
# pop off the head and multiply it with the smaller of the new head or the current arr.
# Always push the new current value.
# If there is more than 1 value not including inf in the stack,
# pop the head off and multiply it with the new head.
# O(N) time, N iterations to iterate through arr, potentially stack has N+1 elements.
# O(N) space, potentially the stack can have N+1 elements.
def mctFromLeafValues(arr) -> int:
    res = 0
    stack = [float('inf')]
    for num in arr:
        while stack[-1] <= num:
            mid = stack.pop()
            res += mid * min(stack[-1], num)
        stack.append(num)
    while len(stack) > 2:
        res += stack.pop() * stack[-1]
    return res