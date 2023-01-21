class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        op=[0]*len(temperatures)
        stack=[]
        for i, x in enumerate(temperatures):
            while len(stack)>0 and stack[-1][1]<x:
                idx,val=stack.pop()
                op[idx]=i-idx
            stack.append([i, x])
        return op