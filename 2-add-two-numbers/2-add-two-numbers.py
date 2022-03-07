# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        prev = ListNode(0)
        result = prev
        
        while p1 or p2 or carry:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            sum = v1 + v2 + carry
            remainder = sum % 10
            carry = sum // 10
            
            newNode = ListNode(remainder)
            prev.next = newNode
            prev = newNode
            
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        
        return result.next
            
            
            