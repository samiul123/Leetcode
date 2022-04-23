# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        mergedHead = lists[0]
        
        for i in range(1, len(lists)):
            head2 = lists[i]
            mergedHead = self.getMergedHead(mergedHead, head2)
            
        return mergedHead
    
    
    def getMergedHead(self, head1, head2):
        mergedHead = ListNode(0)
        prev = mergedHead
        
        temp1 = head1
        temp2 = head2
        
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                prev.next = temp1
                temp1 = temp1.next
            else:
                prev.next = temp2
                temp2 = temp2.next
            prev = prev.next
        prev.next = temp1 or temp2
        return mergedHead.next