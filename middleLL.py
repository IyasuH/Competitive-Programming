# 2 trial about 30 min
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

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # first insert all values to list
        self.head = head
        if self.head is None:
            return
        itr=self.head
        listr=[]
        while itr:
            listr.append(itr.val)
            itr=itr.next

        half=listr[len(listr)/2:]
        new=ListNode(half[0], None)
        for x in half[1:]:
            self.insertAtEnd(x, new)
        return(new)