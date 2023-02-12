# 3 trials 35 min
class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        arr=cardPoints[-k:]+cardPoints[:k]
        winSum=sum(arr[:k])
        maxSum=winSum
        print("ini maxSum:", maxSum)
        print(arr)
        for i in range(len(arr)-k):
            winSum=winSum-arr[i]+arr[i+k]
            maxSum=max(maxSum, winSum)
        return maxSum