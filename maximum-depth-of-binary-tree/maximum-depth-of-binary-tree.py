# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:    
        return self.maxDepthHelper(root, 0)
    
    
    def maxDepthHelper(self, node, depth):
        if not node:
            return 0
        
        leftSubTreeDepth = self.maxDepthHelper(node.left, depth+1)
        rightSubTreeDepth = self.maxDepthHelper(node.right, depth+1)
        
        return max(leftSubTreeDepth, rightSubTreeDepth) + 1