
# Create a stack for keeping track of temps that havent found a higher temp yet.
# Compare the current temp with values in the stack. If the current is larger, 
# pop the stack and set it's position in the output array to the distance between the twot emps.
# If its not larger, append it to the stack.
# O(N^2) time, where N is the length of T. The stack may grow to be N elements worst case when T is reverse sorted.
# O(N) space, N elements in stack + N elements in output array.
def dailyTemperatures(self, T):
    stack = []
    out = [0] * len(T)
    for i, val in enumerate(T):
        for head in reversed(stack):
            if val > head[1]:
                out[head[0]] = i - head[0]
                stack.pop()
            else:
                stack.append([i, val])
                break
        # Append on an empty stack
        if not stack:
            stack.append([i, val])

    # Any leftover temps must be 0 as there are no more higher temps
    while stack:
        val = stack.pop()
        out[val[0]] = 0

    return out

# More compact solution. Leftover temps dont need to be 0 since they were initialized to 0.
# Can just store the index in the stack since we can just reference T with the index for the value.
def dailyTemperaturesCompact(self, T):
    stack = []
    out = [0] * len(T)
    for i, val in enumerate(T):
        while stack and T[stack[-1]] < val:
            head_idx = stack.pop()
            out[head_idx] = i - head_idx
        stack.append(i)

    return out