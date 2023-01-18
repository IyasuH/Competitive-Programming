class MyQueue(object):

    def __init__(self):
        self.arr=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)
        return(self.arr)

    def pop(self):
        """
        :rtype: int
        """
        if self.arr != []:
            return(self.arr.pop(0))
        
    def peek(self):
        """
        :rtype: int
        """
        if self.arr != []:
            return(self.arr[0])
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.arr == []:
            return(True)
        else:
            return (False)
