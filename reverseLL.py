# 1 trial 14 min
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertAtEnd(self, data, nw):
        if nw is None:
            nw=ListNode(data, None)
            return
        while nw.next:
            nw=nw.next
        nw.next=ListNode(data, None)

    def reverseList(self, head):
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
        listr.reverse()
        new=ListNode(listr[0], None)
        for x in listr[1:]:
            self.insertAtEnd(x, new)
        return(new)
        