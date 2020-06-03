# Sort the time points then calculate each time difference. Since time is circular, need to compare the first and last elements as well.
# O(NlgN), NlgN for the sort + N comparisons
# O(1) space since the sort is in place
def findMinDifference(timePoints) -> int:
    curr_min = float("inf")
    timePoints.sort()
    for i in range(len(timePoints)-1):
        diff = calcDifference(timePoints[i], timePoints[i+1])
        if diff < curr_min:
            curr_min = diff
    # Compare the first and last times as they may be closer
    diff = calcDifference(timePoints[0], timePoints[-1])
    if diff < curr_min:
        curr_min = diff
    return curr_min 

# Helper function to find the minute difference between two timepoints
def calcDifference(p1: str, p2: str) -> int:
    h1, m1 = p1.split(":")
    h2, m2 = p2.split(":")
    time1 = int(h1) * 60 + int(m1)
    time2 = int(h2) * 60 + int(m2)
    diff = abs(time1 - time2)
    return min(diff, 24*60 - diff)

# Same as previous solution but all the time points are converted to minutes since midnight ints.
# O(N) space instead since a new sorted array is created
def findMinDifferenceConvFirst(timePoints) -> int:
    curr_min = float("inf")
    converted = sorted(map(convertTime, timePoints))
    for i in range(len(timePoints) - 1):
        diff = minDiff(converted[i], converted[i+1])
        if diff < curr_min:
            curr_min = diff
    # Compare the first and last times as they may be closer
    diff = minDiff(converted[0], converted[-1])
    if diff < curr_min:
        curr_min = diff
    return curr_min 

def minDiff(t1: int, t2: int) -> int:
    diff = abs(t1 - t2)
    return min(diff, 24 * 60 - diff)

def convertTime(time: str) -> int:
    return int(time[:2]) * 60 + int(time[3:])

assert 1 == findMinDifferenceConvFirst(["13:06", "07:14", "23:59", "00:00"])
assert 30 == findMinDifferenceConvFirst(["13:06", "07:14", "23:59", "13:36"])
