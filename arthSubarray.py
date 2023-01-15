class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        boool=[]
        for x in range(m):
            fr=(nums[l[x]:r[x]+1])
            fr.sort()
            # print(fr)
            dif=fr[1]-fr[0]
            i=1
            chk=True
            while i<len(fr):
                if fr[i]-fr[i-1]!=dif:
                    chk=False
                i+=1
            if chk==True:
                boool.append(True)
            else:
                boool.append(False)
        print(boool)
        return boool

