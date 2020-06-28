# 6:53
# Use a map to record each timestamp's hit values.
# O(1) time hit, but the O(N) space can easily grow unbounded.
# O(1) time and space getHits 
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.history:
            self.history[timestamp] = 1
        else:
            self.history[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        totalHits = 0
        for time in range(timestamp-299, timestamp+1):
            if time in self.history:
                totalHits += self.history[time]
        return totalHits

# Use a deque along with a map. Map still contains frequencies but
# it's values that have expired are deleted from the list by the queue.
# The queue contains only valid timestamps.
# Each prune happens on each getHits call, but can be done multithreaded with protections on queue and map.
# O(1) time O(1) space hit
# O(1) time O(1) space getHits, prune will take 300 iterations max.
from collections import deque
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = {}
        self.queue = deque()

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.history:
            self.history[timestamp] = 1
            self.queue.append(timestamp)
        else:
            self.history[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.queue and self.queue[0] < timestamp - 299:
            del(self.history[self.queue.popleft()])
        totalHits = 0
        for time in self.queue:
            totalHits += self.history[time]
        return totalHits


# Use 300 buckets and modulo the timestamp to maintain constant space.
# Each bucket contains the number of hits and the timestamp.
# If a bucket gets reused and the timestamp is different, the original value must be stale.
# Else, just incremebnt it
# getHits will check every bucket for non-expired timestamps.
# O(1) time and space.
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # History is lists of frequency, timestamp
        self.history = [(0,0)] * 300

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        time = timestamp % 300
        
        # Multiple calls for the same timestamp
        if self.history[time][1] == timestamp:
            self.history[time] = (self.history[time][0] + 1, timestamp)
        else:
            # Reuse the previous slot as the previous timestamp must have expired.
            self.history[time] = (1, timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        totalHits = 0
        for entry in self.history:
            if timestamp - entry[1] < 300:
                totalHits += entry[0]
        return totalHits