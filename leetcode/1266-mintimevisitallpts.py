# Moving diagonally is the fastest compared to only by x or only by y. An optimal move can be described as
# diagonal moves + horizontal or vertical moves. Since horizontal or vertical moves will only be done once either x or y is 
# already at the target value, the total number of moves is just the larger value between the absolute differences between x,y of 1 point and the x,y of the other.
# O(N) time where N is number of points, since we iterate N-1 times over the input array.
# O(1) space.
def minTimeToVisitAllPoints(points) -> int:
    moves = 0
    for i in range(1, len(points)):
        x = abs(points[i][0] - points[i-1][0])
        y = abs(points[i][1] - points[i-1][1])
        moves += max(x,y)
    return moves


print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
