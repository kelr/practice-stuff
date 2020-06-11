# Loop through the range of 1-n and compare each with the current target val.
# If it matches, the op should be push then go to the next target
# If it does not match, the op is push pop and stay on the target
# O(N) where N is n. 
# O(N) output array is at most 2N-1 elements (target is a single element == n)
def buildArray(target, n:int)
    out = []
    t = 0
    for i in range(1, n+1):
        if t >= len(target):
            return out

        if i == target[t]:
            out.append("Push")
            t += 1
        else:
            out.append("Push")
            out.append("Pop")
    return out