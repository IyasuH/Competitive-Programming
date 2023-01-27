# 1 trial 15 min
# EG EH
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertAtEnd(self, data, new):
        if new is None:
            new=ListNode(data, None)
            return
        while new.next:
            new=new.next
        new.next=ListNode(data, None)
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list11=[]
        list22=[]
        while list1:
            list11.append(list1.val)
            list1=list1.next
        while list2:
            list22.append(list2.val)
            list2=list2.next
        totList=list11+list22
        totList.sort()
        if len(totList)>=1:
            new=ListNode(totList[0], None)
            for x in totList[1:]:
                self.insertAtEnd(x, new)
            return new
        else:
            return ListNode('',None)