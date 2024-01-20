class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        """
        attempt 1: 
        - Assume 頭尾都可放一個 empty spot `0`
        - 在 iterate 時，inplace地 把 `1` 放入可以放的地方
        """
        canFlowered = 0
        f = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)+1):
            if f[i-1] == 0 and f[i+1] == 0 and f[i] == 0:
                f[i] = 1
                canFlowered += 1
        
        return canFlowered >= n