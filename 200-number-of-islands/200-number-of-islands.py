class LandInfo:
	def __init__(self, currentSize):
		self.currentSize = currentSize;


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in row]for row in grid]
        numberOfIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                landInfo = LandInfo(0)
                self.traverse(i, j, visited, grid, landInfo)
                if landInfo.currentSize > 0:
                    numberOfIslands += 1
        return numberOfIslands
    
    
    def traverse(self, i, j, visited, grid, landInfo):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[i]):
            return
        if visited[i][j]:
            return
        visited[i][j] = True
        if grid[i][j] == "0":
            return
        landInfo.currentSize += 1
        self.traverse(i+1, j, visited, grid, landInfo)
        self.traverse(i-1, j, visited, grid, landInfo)
        self.traverse(i, j-1, visited, grid, landInfo)
        self.traverse(i, j+1, visited, grid, landInfo)
