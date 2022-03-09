# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         visited = []
#         stack = [root] if root else []
#         traversal = []
#         while len(stack) > 0:
#             parent = stack[-1]
#             # print(parent.val)
#             if parent not in visited:
#                 visited.append(parent)
#                 traversal.append(parent.val)
            
#             if parent.left not in visited and parent.left is not None:
#                 stack.append(parent.left)
#             elif parent.right not in visited and parent.right is not None:
#                 stack.append(parent.right)
#             elif (parent.left is None and parent.right is None) or (parent.left in visited and (parent.right in visited or parent.right is None)) or (parent.right in visited and (parent.left in visited or parent.left is None)):
#                 stack.pop(-1)
#         return traversal
        stack = [root] if root else []
        traversal = []
        
        while stack:
            parent = stack.pop()
            
            if parent:
                traversal.append(parent.val)
                if parent.right:
                    stack.append(parent.right)
                if parent.left:
                    stack.append(parent.left)
        return traversal
                