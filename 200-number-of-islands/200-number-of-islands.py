class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        
        visited = [[False for col in range(len(grid[row]))]for row in range(len(grid))]
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1' and not visited[row][col]:
                    self.traverse(row, col, grid, visited)
                    numIslands += 1
        return numIslands
        
    
    def traverse(self, row, col, grid, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        
        if grid[row][col] == '0':
            return
        
        if visited[row][col]:
            return
        
        visited[row][col] = True
                                                                            
        self.traverse(row+1, col, grid, visited)
        self.traverse(row-1, col, grid, visited)
        self.traverse(row, col+1, grid, visited)
        self.traverse(row, col-1, grid, visited)