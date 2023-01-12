class Solution(object):
    def inserSort(self, arr):
        i=1
        while(i<len(arr)):
            temp = arr[i]
            j = i-1
            while(j>=0 and arr[j]>temp):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = temp
            i+=1
        return arr
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arry=[]
        for x in nums:
            arry.append(x)
        arr=self.inserSort(nums)
        idxArr=[]
        for x in arry:
            idxArr.append(arr.index(x))
        return(idxArr)