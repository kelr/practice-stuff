# Create a history map where usernames are mapped to a list of website-timestamp tuples.
# For each user's history, sort their history by timestamp.
# Then generate all 3-sequences possible from the history and store them in a seqFreq map which
# maps 3-sequences to their frequency.
# Finally, sort the seqFreq map by descending frequency values, and by ascending key values.
# O(N^min(3, N-3)) time, total number of 3-Sequences is N choose 3 where N is the length of the website array. N choose 3 devolves to O(N^3)
# O(N^min(3, N-3)) space, total number of 3-Sequences is N choose 3 where N is the length of the website array. There are this many elements in
# the seqFreq map.
def mostVisitedPattern(username, timestamp, website):
    history = createHistory(username, timestamp, website)

    seqFreq = {}
    for user in history:
        # Cant make a 3-sequence if the user didn't visit at least 3 sites.
        if len(history[user]) < 3:
            continue
            
        # Sort this user's history by timestamp
        history[user].sort(key = lambda x: x[1])
        
        # Strip timestamps
        currHistory = [h[0] for h in history[user]]

        # Create all 3-sequences from a user's history as tuples, store them in the seqFreq map with their frequency.
        seqs = generate3Seqs(currHistory)
        for seq in seqs:
            if seq not in seqFreq:
                seqFreq[seq] = 1
            else:
                seqFreq[seq] += 1

    # Sort the seqFreq map by decending frequency values, then by lexographic key names if tied.
    sortedSeqs = sorted(seqFreq.items(), key=lambda x: (-x[1], x[0]))
    
    # Return the key of the most visited 3-sequence
    return sortedSeqs[0][0]
    
def createHistory(username, timestamp, website):
    # Create a map of usernames to their browsing history
    history = {}
    for i in range(len(website)):
        if username[i] not in history:
            history[username[i]] = [(website[i], timestamp[i])]
        else:
            history[username[i]].append((website[i], timestamp[i]))
    return history

# Generates a set of all length 3 sequences from array
def generate3Seqs(array):
    output = set()
    backtrack(array, [], output, 0, 3)
    return output
    
def backtrack(array, currSeq, output, currIdx, seqLen):
    if len(currSeq) == seqLen:
        output.add(tuple(currSeq))
        return
    
    if currIdx >= len(array):
        return
    
    currSeq.append(array[currIdx])
    backtrack(array, currSeq, output, currIdx + 1, seqLen)
    currSeq.pop()
    backtrack(array, currSeq, output, currIdx + 1, seqLen)