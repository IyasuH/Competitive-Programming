class Solution(object):
    
    def inserSort(self, arr):
        # this method sorts and returns it using insert sort
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

    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices=[]
        sorted=self.inserSort(nums)
        for x in range(len(sorted)):
            if target==sorted[x]:
                indices.append(x)
        return indices