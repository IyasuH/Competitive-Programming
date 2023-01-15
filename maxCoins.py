class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        x=1
        my=0
        alice=[]
        mine=[]
        bob=[]
        if len(piles)>1:
            bob=piles[:int(len(piles)/3)]
        newArr=piles[int(len(piles)/3):]
        i=0
        while i<len(newArr):
            if (i%2==0):
                mine.append(newArr[i])
            else:
                alice.append(newArr[i])
            i+=1

        # for x in newArr:
        #     if newArr.index(x)%2==0:
        #         mine.append(x)
        #     else:
        #         alice.append(x)
        for x in mine:
            my+=x
        return my