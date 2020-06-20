
# Create a list of nums in binary form with leading zeroes to match the length of the max value in the array.
# Create a binary trie and insert all the binary nums into it.
# Iterate through the nums and find the max xor value possible by choosing nodes opposite of the current bit.
# O(N) time. It takes N*L iterations to insert all binary nums into the trie and N*L iterations to find the max xor in the trie.
# L is determined by the number of bits it takes to represent the largest value in the array.
# At most this value is 32 as the maximum value for num is 2^31 - 1, making L a constant.
# O(1) space, maximum nodes used is 2^L.
def findMaximumXOR(nums) -> int:
    # Subtract 2 since bin prepends '0b' onto the bit string
    L = len(bin(max(nums))) - 2
    
    # Take each num and create a bit array out of it of length L, prepend leading zeroes as needed
    vals = []
    for num in nums:
        bits = []
        for pos in range(L):
            bits.insert(0, (num >> pos) & 1)
        vals.append(bits)

    # Build the trie
    trie = {}
    for num in vals:
        currNode = trie
        for bit in num:
            if bit not in currNode:
                currNode[bit] = {}
            currNode = currNode[bit]
    
    # Loop through vals, find max xor in the trie 
    currMax = 0
    for num in vals:
        currXor = 0
        currNode = trie
        for bit in num:
            toggled_bit = 1 - bit
            if toggled_bit in currNode:
                # Take the opposite node
                currNode = currNode[toggled_bit]
                # Shift a 1 onto the max since the xor value is 1.
                currXor = (currXor << 1) | 1
            else:
                # Forced to take available node
                currNode = currNode[bit]
                # Shift a 0 onto the max since the xor value is 0.
                currXor = (currXor << 1)
                
        currMax = max(currMax, currXor)
    return currMax