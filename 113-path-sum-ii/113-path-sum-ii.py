# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        all_paths = []
        
        def recurse(node, sum, path):
            if not node:
                return
            
            sum += node.val
            path.append(node.val)
            
            if sum == targetSum and not node.left and not node.right:
                all_paths.append(path.copy())
            
            recurse(node.left, sum, path)
            recurse(node.right, sum, path)
            
            sum -= path.pop()
            
        recurse(root, 0, [])
        return all_paths