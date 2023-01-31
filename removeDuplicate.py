# 20 min 5 trial
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addAtEnd(self, nd, val):
        if nd is None:
            nd=ListNode(val, None)
            return
        while nd.next:
            nd=nd.next
        nd.next=ListNode(val, None)
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lis=[]
        while head:
            lis.append(head.val)
            head=head.next
        dic={}
        for i in lis:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        nw=[]
        for ky in dic:
            if dic[ky]==1:
                nw.append(ky)
        nw.sort()
        print(nw)
        if len(nw)>=1:
            nd=ListNode(nw[0], None)
            for x in nw[1:]:
                self.addAtEnd(nd, x)
            return nd
        return ListNode('', None)