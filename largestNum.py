from itertools import permutations
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        i=1
        while i<len(nums):
            tempN=nums[i]
            temp=int(str(nums[i])[0])
            j=i-1
            while (j>=0 and int(str(nums[j])[0])>temp):
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=tempN
            i+=1
        x=1
        while x<len(nums):
            j=x-1
            if int(str(nums[x])[0])==int(str(nums[j])[0]):
                if len(str(nums[x]))==2 and len(str(nums[j]))==1 and int(str(nums[x])[0])>int(str(nums[x])[1]):
                    temp=nums[x]
                    nums[x]=nums[j]
                    nums[j]=temp
            x+=1
        larg=''
        x=1
        while x<=len(nums):
            larg=larg+str(nums[-x])
            x+=1
        return larg