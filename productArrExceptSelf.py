# 5 trails 45 min
class Solution(object):
    def multArr(self, arr):
        mul=1
        for x in arr:
            mul*=x
        return mul

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mulR=[]
        if 0 in nums:
            zero=0
            for x in nums:
                if x==0:
                    zero+=1
            if zero>1:
                mulR=[0]*len(nums)
            else:
                mulR=[0]*len(nums)
                i=nums.index(0)
                arr=nums[:i]+nums[i+1:]
                mulR[i]=self.multArr(arr)
            return mulR
        mull=self.multArr(nums)
        for i in range(len(nums)):
            mulR.append(mull//nums[i])
        return mulR