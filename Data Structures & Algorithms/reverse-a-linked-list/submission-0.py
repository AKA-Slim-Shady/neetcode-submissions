# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        ret = ListNode(0)
        start = ret
        comp = []

        while curr != None:
            comp.append(curr.val)
            curr = curr.next
            

        for i in comp[::-1]:
            t = ListNode(i)
            ret.next = t
            ret = ret.next
        
        
        return start.next