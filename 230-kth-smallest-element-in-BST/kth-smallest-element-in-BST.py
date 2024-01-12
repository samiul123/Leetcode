from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthSmallest = -1
        count = 0

        def recurse(node):
            nonlocal kthSmallest
            nonlocal count
            if not node or kthSmallest > -1:
                return
            recurse(node.left)
            count += 1
            if count == k:
                kthSmallest = node.val
                return
            recurse(node.right)
        recurse(root)
        return kthSmallest

