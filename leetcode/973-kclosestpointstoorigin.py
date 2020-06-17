import heapq

# Create a minheap of tuples of (distance, point). Pop off K tuples and build a list of points of length K.
# O(N+KlgN) time, N iterations to create the tuples, heapify is linear, K iterations of logN pops.
# O(N) space, N elements of distance tuples, heapify is in place.
def kClosest(points, K):
    out = []
    dist = [(distance(point[0], point[1]), point) for point in points]
    heapq.heapify(dist)
    for _ in range(K):
        out.append(heappop(dist)[1])
    return out

def distance(x: int, y: int) -> int:
    return x**2 + y**2

# Faster to just heapsort the array in place.
def kClosest(points, K):
    return heapq.nsmallest(K, points, lambda x : (x[0]**2 + x[1]**2))