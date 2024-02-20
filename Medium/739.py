# 739. Daily Temperatures
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature
        *******************************************************************************
        解法：https://medium.com/tomsnote/leetcode-739-daily-temperatures-70e003af6116
        List 語法：https://docs.python.org/zh-tw/3/tutorial/datastructures.html
        Monotonic Stack：https://www.geeksforgeeks.org/introduction-to-monotonic-stack-data-structure-and-algorithm-tutorials/
        """
        '''
        output = [0]*len(temperatures)
        stack = [] # [[temperature, index of the temp in temperatures], ...]
        for idx_temp, temp in enumerate(temperatures):
            # Problem 1: the enumeratation of stack is affected by stack.pop(idx_stack)
            # Solution: 
            # https://stackoverflow.com/questions/38546951/remove-element-from-list-when-using-enumerate-in-python
            for idx_stack, item in enumerate(stack):
                if item[0] < temp:
                    output[item[1]] = idx_temp - item[1] 
                    # item[1] is the index of the item's temp
                    stack.pop(idx_stack)
            # 可以解決問題 Problem 1，但是會衍生 Problem 2。
            # Problem 2: Time complexity O(n^2) Runtime Error
            idx_stack = 0
            while idx_stack < len(stack):
                item = stack[idx_stack]
                if item[0] < temp:
                    output[item[1]] = idx_temp - item[1] 
                    # item[1] is the index of the item's temp
                    stack.pop(idx_stack)
                else:
                    idx_stack += 1
            stack.append([temp, idx_temp])
        return output
        '''
        # ChatGPT Result
        output = [0]*len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                output[prev_idx] = idx - prev_idx
            stack.append(idx)
        return output