
# Check every number from 0 to num inclusive. Count how many 1 bits there are.
# Add that value to the output array.
# O(N*size(N)) time N+1 iterations multiplied by how many bits that value has.
# O(N) size, output array has N elements.
def countBits(num: int):
    out = [0] * (num + 1)

    for i in range(num+1):
        for bit in bin(i)[2:]:
            if bit == "1":
                out[i] += 1
    return out


# Use previous values to calculate the next values.
# For each range inbetween powers of two, the next sequence is
# The previous sequence, then the previous sequence + 1.
# O(N) time, single pass through N elements
# O(N) space, N output elements
def countBits(num: int):
    out = [0] * (num + 1)
    power = 0
    offset = 0
    for i in range(1, num+1):
        if i == 1:
            out[i] = 1
            continue
        
        if isPowerTwo(i):
            out[i] = 1
            offset =  2 ** power
            base = offset
            power += 1

        if offset-base < base:
            out[i] = out[offset]
        else:
            out[i] = out[offset-base] + 1

        offset += 1
        
    return out
    
    
def isPowerTwo(x):
    return (x and (not(x & (x - 1))) ) 