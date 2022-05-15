# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root, root]
        
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        
        return True
            
    
#     RECURSIVE O(N) Time O(N) Space
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         return self.isSymmetricHelper(root.left, root.right)
    
    
#     def isSymmetricHelper(self, left, right):
#         if not left and not right:
#             return True
        
#         if not left or not right:
#             return False
        
#         isSymmetric = left.val == right.val
        
#         return isSymmetric and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
    
    