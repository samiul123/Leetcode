# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            rootVal = postorder.pop()
            index = treeMap[rootVal]

            root = TreeNode(rootVal)
            root.right = helper(index+1, right)
            root.left = helper(left, index-1)

            return root
        
        treeMap = {val:idx for idx,val in enumerate(inorder)}
        return helper(0,len(inorder) - 1)