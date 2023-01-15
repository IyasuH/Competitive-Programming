class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        numInt=[]
        for x in nums:
            numInt.append(int(x))        
        numInt.sort()
        return(str(numInt[-k]))