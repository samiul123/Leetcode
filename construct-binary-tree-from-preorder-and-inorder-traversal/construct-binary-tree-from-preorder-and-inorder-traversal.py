# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            
            val = preorder.pop(0)
            idx = treeMap[val]
            root = TreeNode(val)
            root.left = helper(left, idx-1)
            root.right = helper(idx+1, right)
            
            return root
        
        treeMap = {val:idx for idx,val in enumerate(inorder)}
        return helper(0, len(inorder)-1)
            