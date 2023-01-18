# around 12-15 min 1 trial
class MinStack(object):

    def __init__(self):
        self.arr=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.arr.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.arr)>0:
            self.arr.pop(len(self.arr)-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.arr)>0:
            return self.arr[len(self.arr)-1]

    def getMin(self):
        """
        :rtype: int
        """
        min = self.arr[0]
        for x in self.arr:
            if x<min:
                min =x
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()