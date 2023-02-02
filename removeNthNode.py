# 15 min 2 trial
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addAtEnd(self, node, val):
        if node is None:
            node=ListNode(val, None)
            return
        while node.next:
            node=node.next
        node.next=ListNode(val, None)
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        lis.pop(-n)
        if len(lis)>0:
            nd=ListNode(lis[0], None)
            for x in lis[1:]:
                self.addAtEnd(nd, x)
            return nd
        return ListNode("",None)

        