class LandInfo:
	def __init__(self, currentSize):
		self.currentSize = currentSize;


class Solution:
#     Sol#1 (DFS)
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = [[False for i in row]for row in grid]
#         numberOfIslands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 landInfo = LandInfo(0)
#                 self.traverse(i, j, visited, grid, landInfo)
#                 if landInfo.currentSize > 0:
#                     numberOfIslands += 1
#         return numberOfIslands
    
    
#     def traverse(self, i, j, visited, grid, landInfo):
#         if i < 0 or i >= len(grid):
#             return
#         if j < 0 or j >= len(grid[i]):
#             return
#         if visited[i][j]:
#             return
#         visited[i][j] = True
#         if grid[i][j] is "0":
#             return
#         landInfo.currentSize += 1
#         self.traverse(i+1, j, visited, grid, landInfo)
#         self.traverse(i-1, j, visited, grid, landInfo)
#         self.traverse(i, j-1, visited, grid, landInfo)
#         self.traverse(i, j+1, visited, grid, landInfo)
# 
#     Sol#2 (DFS-without visited array)
#     def numIslands(self, grid: List[List[str]]) -> int:
#         numberOfIslands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 landInfo = LandInfo(0)
#                 self.traverse(i, j, grid, landInfo)
#                 if landInfo.currentSize > 0:
#                     numberOfIslands += 1
#         return numberOfIslands
    
    
#     def traverse(self, i, j, grid, landInfo):
#         if i < 0 or i >= len(grid):
#             return
#         if j < 0 or j >= len(grid[i]):
#             return
#         if grid[i][j] is "0":
#             return
#         grid[i][j] = "0"
#         landInfo.currentSize += 1
#         self.traverse(i+1, j, grid, landInfo)
#         self.traverse(i-1, j, grid, landInfo)
#         self.traverse(i, j-1, grid, landInfo)
#         self.traverse(i, j+1, grid, landInfo)
# 
#     Sol#3
    def numIslands(self, grid: List[List[str]]) -> int:
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] is "1":
                    self.traverse(i, j, grid)
                    numberOfIslands += 1
        return numberOfIslands
    
    
    def traverse(self, i, j, grid):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        # if grid[i][j] is "0":
        #     return
        grid[i][j] = "0"
        if i+1 < len(grid) and grid[i+1][j] is "1":
            self.traverse(i+1, j, grid)
        if i-1 >= 0 and grid[i-1][j] is "1":
            self.traverse(i-1, j, grid)
        if j-1 >= 0 and grid[i][j-1] is "1":
            self.traverse(i, j-1, grid)
        if j+1 < len(grid[i]) and grid[i][j+1] is "1":
            self.traverse(i, j+1, grid)