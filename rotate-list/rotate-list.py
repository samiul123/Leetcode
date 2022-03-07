# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        old_head = head
        length = 1
        
        while old_head.next:
            old_head = old_head.next
            length += 1
        
        old_head.next = head
        
        new_tail= head
        
        for i in range(length - k%length -1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        new_tail.next = None
        
        return new_head