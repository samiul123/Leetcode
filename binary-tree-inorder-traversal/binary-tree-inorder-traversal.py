# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root else []
        traversal = []
        visited = []
        
        while stack:
            parent = stack[-1]
            
            if parent.left in visited or parent.left is None:
                traversal.append(parent.val)
                visited.append(parent)
                stack.pop(-1)
                
                if parent.right:
                    stack.append(parent.right)
            
            elif parent.left:
                stack.append(parent.left)
            
        return traversal