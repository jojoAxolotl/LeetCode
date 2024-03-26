# 649. Dota2 Senate

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq = deque()
        dq = deque()
        n = len(senate)
        for idx, char in enumerate(senate):
            if char == 'R':
                rq.append(idx)
            else:
                dq.append(idx)
        # print(rq, dq)
        while not(len(rq) == 0 or len(dq) == 0):
            curR = rq.popleft()
            curD = dq.popleft()
            if curR > curD:
                dq.append(curD + n)
            else:
                rq.append(curR + n)
        if len(rq) == 0:
            return 'Dire'
        else:
            return 'Radiant'