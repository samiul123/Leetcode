class Island:
    def __init__(self, isConnectedToBorder):
        self.isConnectedToBorder = isConnectedToBorder
        

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for col in row] for row in grid]
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    continue
                if visited[row][col]:
                    continue
                    
                island = Island(False)
                
                self.traverse(row, col, grid, visited, island)
                
                if not island.isConnectedToBorder:
                    count += 1
        
        return count
    
    
    
    def traverse(self, row, col, grid, visited, island):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        
        if grid[row][col] == 1:
            return
        
        if visited[row][col]:
            return
        
        visited[row][col] = True
    
        
        if row == 0 or row == len(grid) - 1 or col == 0 or col == len(grid[0]) - 1:
            island.isConnectedToBorder = True
            
        
        self.traverse(row + 1, col, grid, visited, island)
        self.traverse(row - 1, col, grid, visited, island)
        self.traverse(row, col + 1, grid, visited, island)
        self.traverse(row, col - 1, grid, visited, island)
    
        
    