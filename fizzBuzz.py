class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rtype = []
        for x in range(n):
            if ((x+1)%5==0 and (x+1)%3==0):
                rtype.append("FizzBuzz")
            elif (x+1)%3==0:
                rtype.append("Fizz")
            elif (x+1)%5==0:
                rtype.append("Buzz")
            else:
                rtype.append(str(x+1))
        return(rtype)