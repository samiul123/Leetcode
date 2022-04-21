"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visitedMap = {}
        
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]': 
        if not head:
            return head
        
        if head in self.visitedMap:
            return self.visitedMap[head]
        
        node = Node(head.val, None, None)
        self.visitedMap[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node