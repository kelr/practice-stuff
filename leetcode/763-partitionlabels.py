
# Create a freq array for each char. Maintain an open dict for all the characters we've opened and are 
# keeping track of. Iterate through S and subtract from the freq array for that char.
# If frequency drops to 0, delete that character from the open dict. 
# If the open dict is empty, we've closed all characters we opened and can output the count
# to the out list.
# O(N) time, N iterations to build freq array, N iterations to partition
# O(1) space, out array in the worst case will have at most 26 elements, frequency array has a constant 26 elements.
# and the open map will have at most 26 elements as once a char is removed it will not return as the freq array is empty.
def partitionLabels(S):
    freq = [0] * 26
    for char in S:
        freq[ord(char) - ord('a')] += 1

    count = 0
    out = []
    currOpen = {}
    for char in S:
        if char not in currOpen:
            currOpen[char] = 1

        freq[ord(char) - ord('a')] -= 1
        count += 1

        if freq[ord(char) - ord('a')] == 0:
            del(currOpen[char])

        if not currOpen:
            out.append(count)
            count = 0

    return out

# Build a map of each char and their right-most index.
# Iterate through the string, maintain the rightmost index of the current char
# Update the rightmost if a new char has a further index.
# If the index arrives at the rightmost index, end this partition.
# O(N) time, N iters to build the map, N iters to partition
# O(1) space, rightmost map and output array are bounded by character space of 26 chars.
def partition_labels(S):
    rightmost = {c:i for i, c in enumerate(S)}
    left, right = 0, 0

    result = []
    for i, letter in enumerate(S):

        # Update right pointer if the current char's rightmost index is more right-er
        right = max(right, rightmost[letter])
    
        # If the current index hits the rightmost, output this partition and move to the next.
        if i == right:
            result += [right - left + 1]
            left = i + 1

    return result