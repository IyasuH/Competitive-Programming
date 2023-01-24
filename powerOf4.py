# 1 trial 5 minute
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0 or n<0:
            return False
        if n==1:
            return True
        if n>4 and n%4==0:
            return (self.isPowerOfFour(n/4))
        elif n%4==0:
            return True
        else:
            return False