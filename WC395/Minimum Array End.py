# 100282. Minimum Array End
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        nums = [x]
        current = x

        while len(nums) < n:
            next_num = current + 1
            # 保持 next_num 的所有 x 中的位不變，並逐步增加最小可能值
            while (next_num & x) != x:
                next_num += 1
            nums.append(next_num)
            current = next_num

        return nums[-1]
    
    # Time Limit Exceeded 
    # Last executed input: 6715154 7193485