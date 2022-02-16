# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         TWO PASS

#         temp = head
#         length = 0
        
#         while temp is not None:
#             temp = temp.next
#             length += 1
            
#         if n > length:
#             return head
#         elif n == length:
#             head = head.next
#             return head
        
#         temp = head
#         counter = 1
#         while counter < (length - n):
#             temp = temp.next
#             counter += 1

#         if temp.next is not None:
#             temp.next = temp.next.next
        
#         return head

#         ONE PASS
        slow = head
        fast = head
        
        while n > 0:
            fast = fast.next
            n -= 1
        
        if fast is None:
            head = head.next
            return head
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head
    