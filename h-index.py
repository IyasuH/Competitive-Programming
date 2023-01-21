class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        arr=[]
        if len(citations)==1 and citations[0]==0:
            return 0
        elif len(citations)==1:
            return 1
        for x in range(len(citations)):
            if citations[x]>=x+1:
                arr.append(x+1)
            else:
                break
        if len(arr)>0:
            return arr[-1]
        else:
            return 0 