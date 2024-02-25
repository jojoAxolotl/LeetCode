class Solution(object):
    def largestSquareArea(self, bottomLeft, topRight):
        """
        :type bottomLeft: List[List[int]]
        :type topRight: List[List[int]]
        :rtype: int
        """
        n = len(bottomLeft)
        largest_area = 0

        # Function to find intersection of two rectangles
        def intersect(rec1, rec2):
            bl_x = max(rec1[0][0], rec2[0][0])
            bl_y = max(rec1[0][1], rec2[0][1])
            tr_x = min(rec1[1][0], rec2[1][0])
            tr_y = min(rec1[1][1], rec2[1][1])

            if bl_x < tr_x and bl_y < tr_y:  # If rectangles intersect
                return [[bl_x, bl_y], [tr_x, tr_y]]
            else:
                return None

        # Check all pairs for intersection and calculate the largest possible square
        for i in range(n):
            for j in range(i+1, n):
                rec1 = [bottomLeft[i], topRight[i]]
                rec2 = [bottomLeft[j], topRight[j]]
                intersection = intersect(rec1, rec2)

                if intersection:
                    width = intersection[1][0] - intersection[0][0]
                    height = intersection[1][1] - intersection[0][1]
                    side_length = min(width, height)
                    largest_area = max(largest_area, side_length**2)

        return largest_area