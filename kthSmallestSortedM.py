# 1 trial 5 min
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        sum=[]
        for x in matrix:
            sum+=x
        sum.sort()
        print(sum)
        return sum[k-1]