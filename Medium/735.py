# 735. Asteroid Collision

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = [] # FILO LIFO
        for n in asteroids:
            # stack is empty or 
            # last item in stack is negative or 
            # the current item is positive
            if not stack or stack[-1] < 0 or n > 0:
                stack.append(n)
                continue
            
            # stack is not empty and
            # last item in stack is positive and
            # the current item is negative

            # while stack is not empty and last item in stack is positive
            while stack and stack[-1] > 0:
                if stack[-1] > abs(n):
                    break
                x = stack.pop()
                if x + n == 0:
                    break
            else:
                stack.append(n)
        return stack