# 1 trial 10 minu
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import OrderedDict
class Solution(object):
    def insertAtEnd(self, data, nw):
        if nw is None:
            nw=ListNode(data, None)
            return
        while nw.next:
            nw=nw.next
        nw.next=ListNode(data, None)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return
        listr=[]
        while head:
            listr.append(head.val)
            head=head.next
        rty=list(OrderedDict.fromkeys(listr))
        new=ListNode(rty[0], None)
        for x in rty[1:]:
            self.insertAtEnd(x, new)
        return (new)