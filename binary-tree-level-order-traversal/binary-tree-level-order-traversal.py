# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [(root, 0)] if root else None
        prevLevel = -1
        traversal = []
        
        while queue:
            node, currLevel = queue.pop(0)
            
            if currLevel != prevLevel:
                traversal.append([])
            
            traversal[currLevel].append(node.val)
            
            prevLevel = currLevel
            
            for child in [node.left, node.right]:
                if child:
                    queue.append((child, currLevel+1))
        
        return traversal
            