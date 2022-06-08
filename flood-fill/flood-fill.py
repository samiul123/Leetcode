class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startingPixelColor = image[sr][sc]
        
        queue = collections.deque([(sr, sc)])
        visited = {(sr, sc)}
        image[sr][sc] = newColor
        
        while queue:
            current_row, current_col = queue.popleft()
            for row, col in [(current_row+1, current_col), (current_row-1, current_col), (current_row, current_col+1), (current_row, current_col-1)]:
                if row < 0 or col < 0 or row >= len(image) or col >= len(image[row]):
                    continue
                cellColor = image[row][col]
                if (row, col) not in visited and cellColor == startingPixelColor:
                    image[row][col] = newColor
                    queue.append((row, col))
                    visited.add((row, col))
        
        return image