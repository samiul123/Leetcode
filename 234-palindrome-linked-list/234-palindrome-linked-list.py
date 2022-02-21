# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        stack = []
        curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next
            
        curr = head
        while curr:
            if curr.val != stack.pop().val:
                return False
            curr = curr.next
        return True
        
#         4 pass
#         if not head.next:
#             return True
        
#         length = self.getLength(head)
        
#         secondHalf = head
#         currIdx = 1
#         while currIdx <= length // 2:
#             secondHalf = secondHalf.next
#             currIdx += 1
                
#         if length % 2 == 1: 
#             secondHalf = secondHalf.next
            
        
#         currIdx = 2
#         curr = head.next
#         temp = head
        
#         while currIdx <= length // 2:
#             if curr:
#                 temp.next = curr.next
#                 curr.next = head
#                 head = curr
#                 currIdx += 1
#                 curr = temp.next


#         curr = head
#         while secondHalf:
#             if curr.val != secondHalf.val:
#                 return False
#             curr = curr.next
#             secondHalf = secondHalf.next
        
#         return True
        
        
#     def getLength(self, head):
#         length = 0
#         temp = head
#         while temp:
#             length += 1
#             temp = temp.next
#         return length
        