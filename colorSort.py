class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=1
        while(i<len(nums)):
            temp = a[i]
            j = i-1
            while(j>=0 and a[j]>temp):
                a[j+1] = a[j]
                j-=1
            a[j+1] = temp
            i+=1
        return nums
