# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
# here for level-wise storingg the item, list is used which takes linear time to insert at the head
# updated version used deque which takes constant time to insert item at the head
        traversal = []
        queue = [(root, 0)] if root else None
        prevLevel = -1
        
        while queue:
            node, currLevel = queue.pop(0)
            
            if currLevel != prevLevel:
                traversal.append(deque())
            
            if currLevel % 2 == 0:
                traversal[currLevel].append(node.val)
            else:
                traversal[currLevel].appendleft(node.val)
            
            prevLevel = currLevel 
            
            if node.left:
                queue.append((node.left, currLevel+1))
            if node.right:
                queue.append((node.right, currLevel+1))

        return traversal
                
        
        
        