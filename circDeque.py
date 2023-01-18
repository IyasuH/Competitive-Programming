# takes time round 17minute 1 trial
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue=[]
        self.k=k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue)==self.k:
            return False
        else:
            self.queue.insert(0, value)
            return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue)==self.k:
            return False
        else:
            self.queue.append(value)
            return True
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.queue)>0:
            self.queue.pop(0)
            return True
        else:
            return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.queue)>0:
            self.queue.pop(len(self.queue)-1)
            return True
        else:
            return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.queue)>0:
            return self.queue[0]
        else:
            return -1


    def getRear(self):
        """
        :rtype: int
        """
        if len(self.queue)>0:
            return self.queue[len(self.queue)-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if len(self.queue)==0:
            return True
        else:
            return False
        
    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue)==self.k:
            print('self len queue: ',len(self.queue))
            return True
        else:
            print('self k', self.k)
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()