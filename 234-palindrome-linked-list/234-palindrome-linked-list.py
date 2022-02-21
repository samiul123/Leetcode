# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         ONE PASS REVERSE FIRST HALF
        
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            # print("SLOW: ", slow)
            # print("FAST: ", fast)
            # print("PREV: ", prev)
            fast = fast.next.next
            slow.next, slow, prev = prev, slow.next, slow
            # temp = slow
            # slow = slow.next
            # temp.next = prev
            # prev = temp
        
        if fast:
            slow = slow.next
            
        while slow:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        
        return True
        
#         STACK O(N)-Time O(N)-Space


#         if not head.next:
#             return True
#         stack = []
#         curr = head
        
#         while curr:
#             stack.append(curr)
#             curr = curr.next
            
#         curr = head
#         while curr:
#             if curr.val != stack.pop().val:
#                 return False
#             curr = curr.next
#         return True
        
    
    
#         4 PASS O(N)-Time O(1)-Space
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
        