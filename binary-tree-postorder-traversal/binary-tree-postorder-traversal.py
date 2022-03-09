# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root] if root else []
        visited = []
        traversal = []
        
        while stack:
            parent = stack[-1]
            
            if parent.left and parent.left not in visited:
                stack.append(parent.left)
            
            elif parent.right and parent.right not in visited:
                stack.append(parent.right)
            
            else:
                visited.append(parent)
                traversal.append(parent.val)
                stack.pop(-1)
                
        return traversal