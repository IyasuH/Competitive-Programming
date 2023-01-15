class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i=0
        j=len(nums)-1
        if len(nums)>0:
            max=nums[0]+nums[len(nums)-1]
        while i<len(nums):
            if (nums[i]+nums[j]>max):
                max=nums[i]+nums[j]
            i+=1
            j-=1
        return (max)