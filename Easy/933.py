# 933. Number of Recent Calls

from collections import deque
class RecentCounter:

    def __init__(self):
        # Initializes the counter with zero recent requests.
        self.counter = deque()
        

    def ping(self, t: int) -> int:
        self.counter.append(t)
        while True:
            cur = self.counter.popleft()
            if cur >= t - 3000:
                self.counter.appendleft(cur)
                break
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)