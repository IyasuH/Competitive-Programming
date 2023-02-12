# 3 trial 25 min
class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        if len(chalk)==1:
            return 0

        tot=sum(chalk)
        min=k
        while min-tot>0:
            min=min-tot
        rt=0
        for i in range(len(chalk)):
            if min-chalk[i]<0:
                rt=i
                break
            min=min-chalk[i]
        return rt