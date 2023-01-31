# 3 trial 20 min
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros=0
        while 0 in nums:
            nums.remove(0)
            zeros+=1
        # for x in nums:
        #     if x==0:
        #         nums.remove(0)
        #         zeros+=1
        for i in range(zeros):
            nums.append(0)

        print(nums)