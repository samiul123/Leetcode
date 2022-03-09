# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        self.levelOrderHelper(root, 0, levels)
        
        return levels
    
    
    def levelOrderHelper(self, currentNode, level, levels):
        if len(levels) == level:
            levels.append([])
            
        levels[level].append(currentNode.val)
        
        if currentNode.left:
            self.levelOrderHelper(currentNode.left, level+1, levels)
        
        if currentNode.right:
            self.levelOrderHelper(currentNode.right, level+1, levels)
    
        
        