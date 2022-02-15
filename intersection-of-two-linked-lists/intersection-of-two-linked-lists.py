# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA = self.getLength(headA)
        lengthB = self.getLength(headB)
        
        diff = lengthA - lengthB
        
        startA, startB = self.getPointerToStart(headA, headB, diff)
        
        while startA and startB:
            if startA == startB:
                return startA
            startA = startA.next
            startB = startB.next
            
        return None
        
    
    def getLength(self, head: ListNode) -> int:
        length = 0
        temp = head
        while temp is not None:
            length += 1
            temp = temp.next
        return length
    
    
    def getPointerToStart(self, headA, headB, diff):
        tempA, tempB = headA, headB
        
        if diff < 0:
            loop = 0
            while loop < abs(diff):
                tempB = tempB.next
                loop += 1
        
        elif diff > 0:
            loop = 0
            while loop < diff:
                tempA = tempA.next
                loop += 1
        
        return (tempA, tempB)