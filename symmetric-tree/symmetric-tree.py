# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricHelper(root.left, root.right)
    
    
    def isSymmetricHelper(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        
        isSymmetric = left.val == right.val
        
        return isSymmetric and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
    
    