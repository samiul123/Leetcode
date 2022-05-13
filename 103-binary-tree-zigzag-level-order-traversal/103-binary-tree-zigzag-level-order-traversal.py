# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         here
        traversal = []
        queue = [(root, 0)] if root else None
        prevLevel = -1
        
        while queue:
            node, currLevel = queue.pop(0)
            
            if currLevel != prevLevel:
                traversal.append([])
            
            if currLevel % 2 == 0:
                traversal[currLevel].append(node.val)
            else:
                traversal[currLevel].insert(0, node.val)
            
            prevLevel = currLevel 
            
            if node.left:
                queue.append((node.left, currLevel+1))
            if node.right:
                queue.append((node.right, currLevel+1))

        return traversal
                
        
        
        