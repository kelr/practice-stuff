
# Push open parens onto stack, pop if a close is found.
# If the stack is empty, add to the count needed to make valid. As they are closing parens without an open.
# If there are elements in the stack afterwards, those are unclosed open parens and should be added to the count
# O(N) time, single pass through the string
# O(N) space, worst case is a string of all open parens with N elements in the stack.
def minAddToMakeValid(S: str) -> int:
    if not S:
        return 0
    stack = []
    count = 0
    
    for char in S:
        if char == "(":
            stack.append("(")
        elif not stack:
            count += 1
        else:
            stack.pop()
    count += len(stack)
    return count

# Same as above but uses an int as a pseudo stack.
# If diff ever dips below 0, means that there are closing parens with no corresponding open.
# Diff at the end will have the number of opens without closes.
# O(N) single pass
# O(1) space
def minAddToMakeValidNoStack(S: str) -> int:
    if not S:
        return 0

    diff = 0
    count = 0
    
    for char in S:
        if char == "(":
            diff += 1
        else:
            diff -= 1
        if diff < 0:
            diff += 1
            count += 1

    return diff + count