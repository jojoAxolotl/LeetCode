# 841. Keys and Rooms
from typing import List

# # Recursion Way
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         checked = [False]*len(rooms)
#         def checkRoom(room_num: int):
#             if checked[room_num]:
#                 return
#             checked[room_num] = True
#             for room_id in rooms[room_num]:
#                 checkRoom(room_id)
#             return
#         checkRoom(0)
#         return all(checked)

# While Way
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        checked = [False] * len(rooms)
        stack = [0]
        while stack:
            room_num = stack.pop()  # 取出當前房間號
            checked[room_num] = True  # 標記為已檢查
            for room_id in rooms[room_num]:  # check 可看房間
                if not checked[room_id]:  # 只有未檢查的房間才需加入 stack
                    stack.append(room_id)
        return all(checked)