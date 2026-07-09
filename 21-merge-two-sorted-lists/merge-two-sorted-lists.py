# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head=ListNode()
        dum=head
        l1=list1
        l2=list2
        while(l1 and l2):
            if(l1.val>l2.val):
                dum.next=l2
                l2=l2.next
            else:
                dum.next=l1
                l1=l1.next
            dum=dum.next
        if l1:
            dum.next=l1
        else:
            dum.next=l2
        
        return head.next
        