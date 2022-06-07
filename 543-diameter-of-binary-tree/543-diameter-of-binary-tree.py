# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(root):
            if not root:
                return 0

            leftHeight = recurse(root.left)
            rightHeight = recurse(root.right)

            self.diameter = max(self.diameter, leftHeight + rightHeight)

            return 1+max(leftHeight, rightHeight)
        
        recurse(root)
        return self.diameter