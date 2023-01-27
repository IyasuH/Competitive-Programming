# Definition for singly-linked list.
 # class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertSort(self, arr):
        for i in range(1, len(arr)):
            j=i-1
            temp=arr[i]
            while j>=0 and arr[j]>temp:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=temp
        return arr

    def addAtEnd(self, data, llist):
        if llist is None:
            llist=ListNode(data, None)
            return
        while llist.next:
            llist=llist.next
        llist.next=ListNode(data, None)

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lit=[]
        while head:
            lit.append(head.val)
            head=head.next
        print("lit:", lit)
        sortL=self.insertSort(lit)
        new=ListNode(sortL[0], None)
        print("sortL: ",sortL)
        for x in sortL[1:]:
            self.addAtEnd(x, new)
        return new