from collections import deque

# Just follow the prompt algorithm, loop through queries, find the index of that value in perm
# Append that to the result list, then remove that value in perm and stick it in the front.
# O(N*M) time where N is length of query and M is m or how large perm will be.
# Can probably be worst case O(N^2) since N is can be at most M.
# O(N) space as a result array is created with N values. 
def processQueries(queries, m):
    perm = list(range(1,m+1))
    out = []
    index = 0

    for query in queries:
        for i,p in enumerate(perm):
            if query == p:
                out.append(i)
                index = i
                break
        perm.insert(0, perm.pop(index))

    return out

# Using a deque to remove and append to the front is faster than a vanilla list.
def processQueriesDeque(queries, m):
    perm = deque(list(range(1, m+1)))
    out = []

    for val in queries:
        out.append(perm.index(val))
        perm.remove(val)
        perm.appendleft(val)
    
    return out

# Could probably do better with a Fenwick tree, O(nlgn) apparently.

print(processQueriesDeque([4,1,2,2], 4))