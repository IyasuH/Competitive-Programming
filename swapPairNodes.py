# 2 trial 15 min
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addAtEnd(self, node, val):
        if node is None:
            node=ListNode(val, None)
            return node
        while node.next:
            node=node.next
        node.next=ListNode(val, None)

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        swap=[]
        # print(lis)
        i=1
        while i<len(lis):
            if i%2==1:
                swap.append(lis[i])
                swap.append(lis[i-1])
            i+=1
        if len(lis)%2==1:
            swap.append(lis[-1])
        if len(swap)>0:
            node=ListNode(swap[0], None)
            for x in swap[1:]:
                self.addAtEnd(node,x) 
            return node
        return ListNode('', None)