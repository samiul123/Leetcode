# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse(curr_node):
            if not curr_node:
                return False
            left = recurse(curr_node.left)
            right = recurse(curr_node.right)
            mid = curr_node == p or curr_node == q

            if int(left) + int(right) + int(mid) >= 2:
                self.ans = curr_node

            return left or right or mid
        
        recurse(root)
        return self.ans
    
            
            