# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        counter = 1
        start = head
        end = head
        temp = head
        lastLast = None
        
        
        while temp:
            # print("TEMP: {}, COUNT: {}".format(temp, counter))
            if counter == k:
                currHead = start
                temp1 = start
                
                # print("START: {}, END: {}".format(start, end))
                while temp1.next and currHead != end:
                    remove = temp1.next
                    temp1.next = remove.next
                    remove.next = currHead
                    currHead = remove
                if lastLast:
                    lastLast.next = currHead
                if temp1 and temp1 == head:
                    head = currHead
            
                lastLast = temp1
                counter = 1
                start = temp1.next
                temp = start
                # print("START: {}".format(start))
                end = start
            else:
                counter += 1
                end = temp.next
                # print("TEMP: {}".format(temp))
                temp = temp.next
        return head