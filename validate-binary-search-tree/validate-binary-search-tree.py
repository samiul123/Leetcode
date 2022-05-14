# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -math.inf, math.inf)
    
    def isValidBSTHelper(self, node, min, max):
        if not node:
            return True
        isValid = node.val > min and node.val < max
        return isValid and self.isValidBSTHelper(node.left, min, node.val) and self.isValidBSTHelper(node.right, node.val, max) 
        