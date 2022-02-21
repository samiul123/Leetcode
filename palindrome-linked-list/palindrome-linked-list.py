# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        length = self.getLength(head)
        # print(length)
        # print(length % 2)
        
        secondHalf = head
        currIdx = 1
        while currIdx <= length // 2:
            secondHalf = secondHalf.next
            currIdx += 1
        
        # print(currIdx)
        # print(secondHalf.val)
            
        if length % 2 == 1: 
            secondHalf = secondHalf.next
            
        
        currIdx = 2
        curr = head.next
        temp = head
        
        while currIdx <= length // 2:
            if curr:
                temp.next = curr.next
                curr.next = head
                head = curr
                currIdx += 1
                curr = temp.next


        curr = head
        while secondHalf:
            if curr.val != secondHalf.val:
                return False
            curr = curr.next
            secondHalf = secondHalf.next
        
        return True
        
        
        
#         currIdx = 1
#         curr = head
#         while currIdx <= length // 2:
#             checkIdx = length - currIdx + 1
#             temp = curr
#             idx = currIdx
            
#             while idx < checkIdx:
#                 temp = temp.next
#                 idx += 1
            
#             if temp.val != curr.val:
#                 return False
            
#             curr = curr.next
#             currIdx += 1
        
#         return True
        
    
    def getLength(self, head):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        return length
        