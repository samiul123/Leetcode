# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        stack = [(root, 0)] if root else None
        # currLevel = 0
        prevLevel = -1
        
        while stack:
            node, currLevel = stack.pop(0)
            # print(node)
            # print(currLevel)
            if currLevel != prevLevel:
                traversal.append([])
            
            # if traversal[currLevel]:
            if currLevel % 2 == 0:
                traversal[currLevel].append(node.val)
            else:
                traversal[currLevel].insert(0, node.val)
            # print(traversal)
            # else:
            #     traversal.append([])
            prevLevel = currLevel 
            
            # if (currLevel + 1) % 2 == 1:
            # if node.right:
            #     stack.append((node.right, currLevel+1))
            if node.left:
                stack.append((node.left, currLevel+1))
            if node.right:
                stack.append((node.right, currLevel+1))
            # else:
            #     if node.left:
            #         stack.append((node.left, currLevel+1))
            #     if node.right:
            #         stack.append((node.right, currLevel+1))
        return traversal
                
        
        
        