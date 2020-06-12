
# Preallocate a history array of 10k ints since the calls are bounded to 10k.
# Two pointers newest and oldest. Add a new ping in order by index to the history.
# If the oldest is older than the newest by 3000, increm oldest until it is no longer the case.
# Return the difference between the two pointers.
# O(1) time, since the most oldest shifts possible will be 3000 since each ping is
# strictly increasing.
# O(1) space, preallocated 10k elements.
class RecentCounter:
    def __init__(self):
        self.history = [0] * 10000
        self.newest = 0
        self.oldest = 0

    def ping(self, t: int) -> int:
        self.history[self.newest] = t
        self.newest += 1
        
        while self.history[self.newest-1] - self.history[self.oldest] > 3000:
            self.oldest += 1
        
        return self.newest - self.oldest

