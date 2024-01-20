class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        """
        idea 2: get the zeros and count the available flowered spots

        start ptr: point the 0 right after 1s, flowerbed[start] = 0 
        last ptr: point the last flowerbed[i(last)] = 0
        last - start + 1 is the amount of 0s
        (the amount of 0s - 1) // 2 = the amount of 1s can be palaced
        """

        length = len(flowerbed)

        # a little speed up but not necessary

        # if n == 0:  # special case: no need to plant any flower
        #     return True
        
        # if length == 1: # special case: only one spot in the flowerbed
        #     return flowerbed[0] == 0 and n <= 1

        canFlower = 0
        i = 0

        while i < length:
            if flowerbed[i] == 0:
                start = i
                while i < length and flowerbed[i] == 0:
                    i += 1
                end = i

                # Calculate the length of the sequence of zeros
                zeroCount = end - start

                # sequence at the beginning or end
                if start == 0:
                    zeroCount += 1
                if end == length:
                    zeroCount += 1
                
                canFlower += (zeroCount - 1) // 2
            
            else:
                i += 1

        return canFlower >= n