# 1 trail 25 min
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addAtEnd(self, nod, val):
        if nod is None:
            nod=ListNode(val, None)
            return
        while nod.next:
            nod=nod.next
        nod.next=ListNode(val, None)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lis=[]
        for nd in lists:
            while nd:
                lis.append(nd.val)
                nd=nd.next
        if len(lis)==0:
            return ListNode('', None)
        lis.sort()
        nd=ListNode(lis[0], None)
        for x in lis[1:]:
            self.addAtEnd(nd,x)
        return nd