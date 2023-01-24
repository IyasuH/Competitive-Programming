import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0 or n<0:
            return False
        if n==1:
            return True
        if n>3 and n%3==0:
            return (self.isPowerOfThree(n/3))
        elif n%3==0:
            return True
        else:
            return False