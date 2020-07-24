# Split the logs into digs and lets. Sort the lets by payload then identifier. Join the two lists in the end.
# O(NlgN) time, worst case is that all the logs are lets which takes NlgN to sort.
# O(N) space, num elements of Digs + lets is N + concatination at the end is another N.
def reorderLogFiles(logs):
    if not logs:
        return []
    
    digs = []
    lets = []
    
    for log in logs:
        splitLog = log.split(" ")
        if splitLog[1].isdigit():
            digs.append(log)
        else:
            lets.append(log)
    
    # Sort the lets by log payload, then by identifier on ties
    lets.sort(key = lambda x: (x.split(" ")[1:], x.split(" ")[0]))
    
    return lets + digs