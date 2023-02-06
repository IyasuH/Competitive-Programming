# 3 trials 15 min
class MedianFinder(object):

    def __init__(self):
        self.heap=[]
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.heap.append(num)

        

    def findMedian(self):
        """
        :rtype: float
        """
        # if it is even
        # print("median for: ", self.heap)
        self.heap.sort()
        if len(self.heap)%2==0:
            low=self.heap[int(len(self.heap)/2)]
            up=self.heap[int((len(self.heap)-1)/2)]
            # print((low+up)/2.0)
            return (low+up)/2.0
        else:
            # print(self.heap[int(len(self.heap)/2)])
            return self.heap[int(len(self.heap)/2)]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()