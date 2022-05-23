class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    self.traverse(row, col, grid)
                    numIslands += 1
        return numIslands
        
    
    def traverse(self, row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
            return
        
        if grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
                                                                            
        self.traverse(row+1, col, grid)
        self.traverse(row-1, col, grid)
        self.traverse(row, col+1, grid)
        self.traverse(row, col-1, grid)