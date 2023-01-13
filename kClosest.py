import math
class Solution(object):
    def findDist(self, arr):
        return (math.sqrt(arr[0]**2+arr[1]**2))
    def insertSort(self, arr):
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

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        minDict={}
        for x in points:
            minDict[self.findDist(x)]=x
        dist=list(minDict.keys())
        dist=self.insertSort(dist)
        print(dist)
        sorted_dist={}
        for i in dist:
            sorted_dist[i]=minDict[i]
        print(sorted_dist)
        sorted_points=list(sorted_dist.values())
        return(sorted_points[:k])