# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeInfo:
	def __init__(self, isBalanced, height):
		self.isBalanced = isBalanced
		self.height = height	
	

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        treeInfo = self.getTreeInfo(root)
        return treeInfo.isBalanced
    
    
        
    def getTreeInfo(self, tree):
        if tree is None:
            return TreeInfo(True, -1)

        leftSubtreeInfo = self.getTreeInfo(tree.left)
        rightSubtreeInfo = self.getTreeInfo(tree.right)

        isBalanced = bool(leftSubtreeInfo.isBalanced 
                          and rightSubtreeInfo.isBalanced 
                          and abs(leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1)
        height = 1 + max(leftSubtreeInfo.height, rightSubtreeInfo.height)
        return TreeInfo(isBalanced, height)

        