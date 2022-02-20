# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         Iterative
#         temp = head
        
#         if temp is None:
#             return head
        
#         while temp.next is not None:
#             remove = temp.next
#             temp.next = temp.next.next
#             remove.next = head
#             head = remove
        
#         return head


#         Recursive
        if head is None or head.next is None:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
        