"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def bfsconnecthelper(node, level):
            if not node:
                return
            
            queue = [(node, level)]
            while queue:
                pop = queue.pop(0)
                peek = queue[0] if queue else None
                
                if not peek or pop[1] != peek[1]:
                    pop[0].next = None
                elif pop[1] == peek[1]:
                    pop[0].next = peek[0]
                
                if pop[0].left:
                    queue.append((pop[0].left, pop[1]+1))
                if pop[0].right:
                    queue.append((pop[0].right, pop[1]+1))
                    
        bfsconnecthelper(root, 0)
        return root