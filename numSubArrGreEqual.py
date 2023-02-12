# 2 trials 20 min
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sumWin=sum(arr[:k])
        avgWin=sumWin/k
        count=0
        if avgWin>=threshold:
            count+=1
        for i in range(len(arr)-k):
            sumWin=sumWin-arr[i]+arr[i+k]
            avgWin=sumWin/k
            if avgWin>=threshold:
                count+=1
        return count