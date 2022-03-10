# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

PREORDER = 0
MODIFIED_PREORDER = 1
INVALID = -999

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    
        if root.left and root.right:
            leftTraversal = []
            rightTraversal = []
            self.getTraversal(root.left, PREORDER, leftTraversal)
            self.getTraversal(root.right, MODIFIED_PREORDER, rightTraversal)
            
            if len(leftTraversal) != len(rightTraversal):
                return False
            
            for i in range(len(leftTraversal)):
                if leftTraversal[i] != rightTraversal[i]:
                    return False 
                
            return True
        
        elif root and not root.left and not root.right:
            return True
        
        return False
    
    
    def getTraversal(self, node, type, traversal):
        if not node:
            traversal.append(INVALID)
            return
        
        traversal.append(node.val)
        if type == PREORDER:
            self.getTraversal(node.left, type, traversal)
            self.getTraversal(node.right, type, traversal)
        
        else:
            self.getTraversal(node.right, type, traversal)
            self.getTraversal(node.left, type, traversal)