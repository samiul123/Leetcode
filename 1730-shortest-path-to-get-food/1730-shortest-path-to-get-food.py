class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        start_row, start_col = -1, -1
        
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] != '*':
#                     continue
#                 start_row, start_col = i, j
#                 break
        
#         minLength = math.inf
        
#         def findPath(s_row, s_col, grid, path):
#             nonlocal minLength
            
#             if s_row < 0 or s_row >= m or s_col < 0 or s_col >= n:
#                 return
            
#             if grid[s_row][s_col] == 'X':
#                 return
            
#             path.append((s_row, s_col))
            
#             if grid[s_row][s_col] == '#':
#                 minLength = min(minLength, len(path))
#                 path.pop()
#                 return
#             else:
#                 grid[s_row][s_col] = 'X'
            
#             for d_row, d_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#                 findPath(s_row + d_row, s_col + d_col, grid, path)
                
#             # grid[s_row][s_col] = '*' if (s_row, s_col) == (start_row, start_col) else 'O' 
#             grid[s_row][s_col] = 'O'
#             path.pop()
                
        
#         # print(start_row, start_col, path)
#         findPath(start_row, start_col, grid, [])
#         # print(path)
#         return minLength - 1 if minLength != math.inf else -1
            
            
            
            
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '*':
                    continue
                start_row, start_col = i, j
                break
            
        queue = [(start_row, start_col)]
        result = 0
        while len(queue) > 0:
            # print(queue)
            length = len(queue)
            result += 1
            
            for i in range(length):
                curr_row, curr_col = queue.pop(0)

                for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row = curr_row + d_row
                    next_col = curr_col + d_col

                    if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                        continue

                    if grid[next_row][next_col] != 'X':
                        if grid[next_row][next_col] == '#':
                            return result
                        grid[next_row][next_col] = 'X'
                        queue.append((next_row, next_col))
        
        return -1